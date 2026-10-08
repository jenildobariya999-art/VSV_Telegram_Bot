#!/usr/bin/env python3
"""
TBC-Lite panel: run MANY Telebot-Creator (TPY) bots on your own server with a web dashboard.
  python tbc_panel.py        (needs PANEL_PASSWORD in .env or environment)
"""
import hashlib, os, sys, json, time, threading, types, secrets, hmac, re, sqlite3, traceback, io, shutil, tempfile
try:
    import requests
    from flask import Flask, request, redirect, session, render_template, abort, Response, url_for, flash
    from jinja2 import DictLoader
except ImportError as _e:
    sys.exit("Missing Python package (%s). Run:  pip install -r requirements.txt   (or: pip install flask requests waitress)" % _e)

HERE = os.path.dirname(os.path.abspath(__file__))
def _load_env():
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
_load_env()

HOST = os.environ.get("PANEL_HOST", "0.0.0.0")
APP_TITLE = os.environ.get("PANEL_TITLE", "My Telebot Panel")
PORT = int(os.environ.get("PANEL_PORT") or os.environ.get("SERVER_PORT") or os.environ.get("PORT") or "2222")
PUBLIC_URL = os.environ.get("PUBLIC_URL", "").rstrip("/")
WORKERS_PER_BOT = int(os.environ.get("WORKERS_PER_BOT", "4"))

def _pick_data_dir():
    want = os.path.abspath(os.environ.get("DATA_DIR", os.path.join(HERE, "data")))
    for d in (want, os.path.join(tempfile.gettempdir(), "tbc_panel_data")):
        try:
            os.makedirs(os.path.join(d, "bots"), exist_ok=True)
            t = os.path.join(d, ".w"); open(t, "w").write("x"); os.remove(t)
            if d != want: print("WARNING: %s is not writable, using %s (data may be lost on restart!)" % (want, d), flush=True)
            return d
        except Exception: continue
    sys.exit("Cannot write to any data folder. Set DATA_DIR to a writable path.")
DATA_DIR = _pick_data_dir()
BOTS_DIR = os.path.join(DATA_DIR, "bots")

PASSWORD = os.environ.get("PANEL_PASSWORD", "")
_PWFILE = os.path.join(DATA_DIR, "panel_password.txt")
PW_GENERATED = False
if len(PASSWORD) < 8:                      # never crash: make a strong password and show it in the logs
    if os.path.exists(_PWFILE): PASSWORD = open(_PWFILE).read().strip()
    else:
        PASSWORD = secrets.token_urlsafe(12); open(_PWFILE, "w").write(PASSWORD)
    PW_GENERATED = True
RUNTIME_PATH = os.path.join(HERE, "tbc_runtime.py")
RUNTIME_CODE = compile(open(RUNTIME_PATH, encoding="utf-8").read(), RUNTIME_PATH, "exec")

# ------------------------------------------------------------------ panel database
_pdb = sqlite3.connect(os.path.join(DATA_DIR, "panel.sqlite3"), check_same_thread=False, isolation_level=None, timeout=30)
_pdb.row_factory = sqlite3.Row
_plock = threading.RLock()
_pdb.execute("""CREATE TABLE IF NOT EXISTS bots(id INTEGER PRIMARY KEY AUTOINCREMENT, token TEXT UNIQUE,
    name TEXT, username TEXT, enabled INTEGER DEFAULT 0, created REAL, note TEXT DEFAULT '')""")
_pdb.execute("CREATE TABLE IF NOT EXISTS settings(k TEXT PRIMARY KEY, v TEXT)")
_pdb.execute("CREATE TABLE IF NOT EXISTS hourly(hour INTEGER, bot_id INTEGER, n INTEGER, PRIMARY KEY(hour,bot_id))")
for _c, _d in (("pinned", "INTEGER DEFAULT 0"), ("error_chat", "TEXT DEFAULT ''"), ("miniapp_secret", "TEXT DEFAULT ''"), ("tg_id", "INTEGER")):
    try: _pdb.execute("ALTER TABLE bots ADD COLUMN %s %s" % (_c, _d))
    except Exception: pass
def q(sql, args=()):
    with _plock: return _pdb.execute(sql, args).fetchall()
def q1(sql, args=()):
    r = q(sql, args); return r[0] if r else None
def x(sql, args=()):
    with _plock: return _pdb.execute(sql, args)

def bot_dir(bid):
    d = os.path.join(BOTS_DIR, str(int(bid))); os.makedirs(d, exist_ok=True); return d
def cmd_file(bid): return os.path.join(bot_dir(bid), "commands.json")
def db_file(bid): return os.path.join(bot_dir(bid), "data.sqlite3")

_cmdlocks = {}
def _lock_for(bid): return _cmdlocks.setdefault(int(bid), threading.RLock())

def load_cmds_file(bid):
    try: return json.load(open(cmd_file(bid), encoding="utf-8"))
    except Exception: return {}
def save_cmds_file(bid, cmds):
    tmp = cmd_file(bid) + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f: json.dump(cmds, f, ensure_ascii=False)
    os.replace(tmp, cmd_file(bid))

def parse_commands_text(txt):
    txt = txt.replace("\r\n", "\n")
    if re.search(r"(?m)^=== .+? ===$", txt):
        parts = re.split(r"(?m)^=== (.+?) ===$", txt)
        return {n.strip(): c.strip("\n") for n, c in zip(parts[1::2], parts[2::2])}
    if re.search(r"(?m)^# COMMAND: .+$", txt):
        parts = re.split(r"(?m)^# COMMAND: (.+)$", txt)
        return {n.strip(): re.sub(r"(?m)^#={20,}\s*$", "", c).strip("\n") for n, c in zip(parts[1::2], parts[2::2])}
    try:
        d = json.loads(txt)
        if isinstance(d, dict): return {str(k): str(v) for k, v in d.items()}
    except Exception: pass
    return {}

# ------------------------------------------------------------------ bot runners
RUNNERS = {}          # bid -> Runner
WEBHOOKS = {}         # secret -> Runner

class Runner:
    def __init__(self, bid, token):
        self.bid, self.token = int(bid), token
        self.mod = None; self.thread = None; self.err = ""; self.cmds = None; self.want = False
    @property
    def alive(self): return bool(self.thread and self.thread.is_alive())
    @property
    def state(self):
        if self.alive:
            return "running" if (self.mod and self.mod.BOT_INFO.get("bot_id")) else ("stopping" if self.mod and self.mod.STOP.is_set() else "starting")
        return "error" if self.err else "stopped"
    def start(self):
        if self.alive: return
        self.err = ""; self.want = True
        with _lock_for(self.bid):
            self.cmds = load_cmds_file(self.bid)
        cfg = {"token": self.token, "dir": bot_dir(self.bid), "db_path": db_file(self.bid), "commands": self.cmds,
               "workers": WORKERS_PER_BOT, "tag": "#%d" % self.bid, "shared_webhook": True,
               "public_url": PUBLIC_URL or "http://127.0.0.1:%d" % PORT,
               "error_chat": (q1("SELECT error_chat FROM bots WHERE id=?", (self.bid,))["error_chat"] or setting("error_chat") or "").strip()}
        try:
            mod = types.ModuleType("tbcbot_%d" % self.bid)
            mod.__dict__["CONFIG"] = cfg; mod.__dict__["__file__"] = RUNTIME_PATH
            exec(RUNTIME_CODE, mod.__dict__)
        except Exception as e:
            self.err = "load failed: %s" % e; return
        self.mod = mod; WEBHOOKS[mod.WEBHOOK_SECRET] = self
        self.thread = threading.Thread(target=self._run, daemon=True, name="bot-%d" % self.bid); self.thread.start()
    def _run(self):
        try: self.mod.main()
        except SystemExit as e: self.err = str(e.code)
        except Exception as e: self.err = str(e)[:300]
    def stop(self, wait=False):
        self.want = False
        if self.mod: self.mod.STOP.set()
        if wait and self.thread: self.thread.join(timeout=45)
    def restart(self):
        def job():
            self.stop(wait=True); self.start()
        threading.Thread(target=job, daemon=True).start()

def runner(bid):
    r = RUNNERS.get(int(bid))
    if r is None:
        row = q1("SELECT token FROM bots WHERE id=?", (int(bid),))
        if not row: return None
        r = RUNNERS[int(bid)] = Runner(bid, row["token"])
    return r

def get_cmds(bid):
    r = RUNNERS.get(int(bid))
    if r and r.alive and r.cmds is not None: return r.cmds
    return load_cmds_file(bid)

def apply_cmd_change(bid, name, code):
    """code=None -> delete. Persists to disk and hot-reloads a running bot."""
    with _lock_for(bid):
        r = RUNNERS.get(int(bid))
        live = r.cmds if (r and r.alive and r.cmds is not None) else None
        cmds = live if live is not None else load_cmds_file(bid)
        if code is None: cmds.pop(name, None)
        else: cmds[name] = code
        if r and r.mod:
            r.mod._compiled.pop(name, None)
        save_cmds_file(bid, cmds)

def replace_cmds(bid, new, merge):
    with _lock_for(bid):
        r = RUNNERS.get(int(bid))
        live = r.cmds if (r and r.alive and r.cmds is not None) else None
        cmds = live if live is not None else load_cmds_file(bid)
        if not merge: cmds.clear()
        cmds.update(new)
        if r and r.mod: r.mod._compiled.clear()
        save_cmds_file(bid, cmds)
    return len(cmds)

def fetch_me(token):
    try:
        j = requests.get("https://api.telegram.org/bot%s/getMe" % token, timeout=15).json()
        if j.get("ok"): return True, j["result"]
        return False, j.get("description", "invalid token")
    except Exception as e:
        return False, "network error: %s" % e

# ------------------------------------------------------------------ settings, password
def setting(k, default=""):
    r = q1("SELECT v FROM settings WHERE k=?", (k,)); return r["v"] if r else default
def set_setting(k, v): x("INSERT OR REPLACE INTO settings VALUES(?,?)", (k, v))

def _hash_pw(pw, salt=None):
    salt = salt or secrets.token_hex(8)
    return salt + "$" + hashlib.pbkdf2_hmac("sha256", pw.encode(), salt.encode(), 120000).hex()
def check_pw(pw):
    h = setting("pw_hash")
    if h:
        salt, _ = h.split("$", 1); return hmac.compare_digest(_hash_pw(pw, salt), h)
    return hmac.compare_digest(pw, PASSWORD)

# ------------------------------------------------------------------ per-bot sqlite helpers
SCHEMA = ["CREATE TABLE IF NOT EXISTS bot_data(name TEXT PRIMARY KEY, value TEXT)",
    "CREATE TABLE IF NOT EXISTS user_data(user TEXT, name TEXT, value TEXT, PRIMARY KEY(user,name))",
    "CREATE TABLE IF NOT EXISTS res(scope TEXT, user TEXT, name TEXT, value REAL, PRIMARY KEY(scope,user,name))",
    "CREATE TABLE IF NOT EXISTS waits(user TEXT PRIMARY KEY, command TEXT, options TEXT)",
    "CREATE TABLE IF NOT EXISTS users(user TEXT PRIMARY KEY, first_seen REAL, last_seen REAL, blocked INTEGER DEFAULT 0)",
    "CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY, run_at REAL, command TEXT, options TEXT, user TEXT, ctx TEXT)",
    "CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT)",
    "CREATE TABLE IF NOT EXISTS errors(id INTEGER PRIMARY KEY AUTOINCREMENT, ts REAL, command TEXT, user TEXT, etype TEXT, msg TEXT, line INTEGER, ctx TEXT, tb TEXT)",
    "CREATE TABLE IF NOT EXISTS broadcasts(id TEXT PRIMARY KEY, ts REAL, text TEXT, total INTEGER, ok INTEGER, err INTEGER, status TEXT)"]
def dbc(bid):
    c = sqlite3.connect(db_file(bid), timeout=30); c.execute("PRAGMA journal_mode=WAL")
    for s in SCHEMA: c.execute(s)
    try: c.execute("ALTER TABLE users ADD COLUMN blocked INTEGER DEFAULT 0")
    except Exception: pass
    return c

_cache = {}
def cached(key, ttl, fn):
    v = _cache.get(key)
    if v and time.time() - v[0] < ttl: return v[1]
    val = fn(); _cache[key] = (time.time(), val); return val

def user_stats(bid):
    def f():
        z = dict(total=0, a24=0, a7=0, a30=0, n24=0, n7=0, n30=0, blocked=0, last=0)
        if not os.path.exists(db_file(bid)): return z
        try:
            c = sqlite3.connect(db_file(bid), timeout=10); n = time.time()
            a = (n - 86400, n - 7 * 86400, n - 30 * 86400)
            try:
                r = c.execute("SELECT COUNT(*),SUM(last_seen>?),SUM(last_seen>?),SUM(last_seen>?),SUM(first_seen>?),SUM(first_seen>?),SUM(first_seen>?),SUM(COALESCE(blocked,0)),MAX(last_seen) FROM users", a + a).fetchone()
            except Exception:
                r = list(c.execute("SELECT COUNT(*),SUM(last_seen>?),SUM(last_seen>?),SUM(last_seen>?),SUM(first_seen>?),SUM(first_seen>?),SUM(first_seen>?),0,MAX(last_seen) FROM users", a + a).fetchone())
            c.close()
            return dict(zip(("total", "a24", "a7", "a30", "n24", "n7", "n30", "blocked", "last"), [v or 0 for v in r]))
        except Exception: return z
    return cached(("us", bid), 20, f)

def user_counts(bid):
    s = user_stats(bid); return (s["total"], s["a24"])

def get_errors(bid, limit=100):
    if not os.path.exists(db_file(bid)): return []
    try:
        c = sqlite3.connect(db_file(bid), timeout=10); c.row_factory = sqlite3.Row
        rows = c.execute("SELECT * FROM errors ORDER BY id DESC LIMIT ?", (limit,)).fetchall(); c.close()
    except Exception: return []
    out = []
    for r in rows:
        d = dict(r)
        try: d["ctx"] = json.loads(d["ctx"] or "[]")
        except Exception: d["ctx"] = []
        out.append(d)
    return out

def error_count(bid):
    def f():
        if not os.path.exists(db_file(bid)): return 0
        try:
            c = sqlite3.connect(db_file(bid), timeout=10); n = c.execute("SELECT COUNT(*) FROM errors").fetchone()[0]; c.close(); return n
        except Exception: return 0
    return cached(("ec", bid), 15, f)

def bots_overview():
    out = []
    for b in q("SELECT * FROM bots ORDER BY pinned DESC, id DESC"):
        r = RUNNERS.get(b["id"]); s = user_stats(b["id"])
        out.append({"id": b["id"], "tgid": b["tg_id"] or b["id"], "name": b["name"] or "?", "username": b["username"] or "", "enabled": b["enabled"], "pinned": b["pinned"],
                    "state": r.state if r else "stopped", "err": r.err if r else "", "users": s["total"], "active": s["a24"],
                    "cmds": len(r.cmds) if (r and r.alive and r.cmds is not None) else len(load_cmds_file(b["id"]))})
    return out

# ------------------------------------------------------------------ hourly sampler (dashboard chart)
_last = {}
def sampler():
    while True:
        time.sleep(30)
        try:
            h = int(time.time() // 3600)
            for bid, r in list(RUNNERS.items()):
                if r.mod:
                    cur = r.mod.STATS["commands"]; key = (bid, id(r.mod)); d = cur - _last.get(key, cur); _last[key] = cur
                    if d > 0: x("INSERT INTO hourly(hour,bot_id,n) VALUES(?,?,?) ON CONFLICT(hour,bot_id) DO UPDATE SET n=n+excluded.n", (h, bid, d))
            x("DELETE FROM hourly WHERE hour<?", (h - 24 * 8,))
        except Exception: traceback.print_exc()

def dash_data():
    now_h = int(time.time() // 3600); start = now_h - 23
    m = {r["hour"]: r["n"] for r in q("SELECT hour, SUM(n) n FROM hourly WHERE hour>=? GROUP BY hour", (start,))}
    series = [m.get(h, 0) for h in range(start, now_h + 1)]
    ov = bots_overview(); by = {b["id"]: b for b in ov}
    top = []
    for r in q("SELECT bot_id, SUM(n) n FROM hourly WHERE hour>=? GROUP BY bot_id ORDER BY n DESC LIMIT 5", (start,)):
        if r["bot_id"] in by: top.append(by[r["bot_id"]])
    for b in sorted(ov, key=lambda b: -b["users"]):
        if len(top) >= 5: break
        if b not in top: top.append(b)
    tot = sum(series)
    return dict(series=series, hours=[h * 3600 for h in range(start, now_h + 1)], cmds=tot, peak=max(series) if series else 0,
                avg=round(tot / 24), active_hrs=sum(1 for v in series if v > 0), total=len(ov),
                working=sum(1 for b in ov if b["state"] == "running"), users=sum(b["users"] for b in ov),
                active=sum(b["active"] for b in ov), top=top)

# ------------------------------------------------------------------ import / export formats
CODE_KEYS = ("code", "script", "content", "body", "tpy", "source", "python", "command_code", "text")
NAME_KEYS = ("name", "command", "cmd", "pattern", "trigger", "title", "id")
def _pick(d, keys):
    for k in keys:
        if k in d and isinstance(d[k], str): return d[k]
    return None

def extract_commands(obj, depth=0):
    """tolerant: finds commands in many JSON layouts (dict name->code, list of {name,code}, nested 'commands' ...)"""
    if depth > 4: return {}
    if isinstance(obj, dict):
        for key in ("commands", "Commands", "cmds", "bot_commands", "command_list"):
            if key in obj:
                r = extract_commands(obj[key], depth + 1)
                if r: return r
        if obj and all(isinstance(v, str) for v in obj.values()) and any(k.startswith("/") or "\n" in v for k, v in obj.items()):
            return dict(obj)
        out = {}
        for k, v in obj.items():
            if isinstance(v, dict):
                c = _pick(v, CODE_KEYS)
                if c is not None: out[k] = c
        if out: return out
        for v in obj.values():
            if isinstance(v, (dict, list)):
                r = extract_commands(v, depth + 1)
                if r: return r
    elif isinstance(obj, list):
        out = {}
        for it in obj:
            if isinstance(it, dict):
                n, c = _pick(it, NAME_KEYS), _pick(it, CODE_KEYS)
                if n is not None and c is not None: out[n] = c
        return out
    return {}

def extract_data(obj):
    if isinstance(obj, dict):
        for key in ("bot_data", "botData", "bot_variables", "storage"):
            if isinstance(obj.get(key), dict): return obj[key]
    return {}

def parse_any(txt):
    txt = txt.lstrip("\ufeff"); s = txt.lstrip()
    if s[:1] in "{[":
        try: obj = json.loads(s)
        except Exception: obj = None
        if obj is not None: return extract_commands(obj), extract_data(obj)
    return parse_commands_text(txt), {}

def bot_export_obj(bid, with_data=False, with_users=False):
    b = q1("SELECT * FROM bots WHERE id=?", (bid,))
    o = {"format": "tbc-lite/1", "exported": int(time.time()), "bot": {"id": bid, "name": b["name"], "username": b["username"]},
         "commands": get_cmds(bid)}
    if with_data and os.path.exists(db_file(bid)):
        c = dbc(bid); o["bot_data"] = {k: _dec(v) for k, v in c.execute("SELECT name,value FROM bot_data").fetchall()}
        if with_users: o["users"] = [r[0] for r in c.execute("SELECT user FROM users").fetchall()]
        c.close()
    return o
def _dec(s):
    try: return json.loads(s)
    except Exception: return s

def bulk_update(bid, changes):
    """changes: name -> code (or None to delete); one disk write"""
    with _lock_for(bid):
        r = RUNNERS.get(int(bid)); live = r.cmds if (r and r.alive and r.cmds is not None) else None
        cmds = live if live is not None else load_cmds_file(bid)
        for n, c in changes.items():
            if c is None: cmds.pop(n, None)
            else: cmds[n] = c
            if r and r.mod: r.mod._compiled.pop(n, None)
        save_cmds_file(bid, cmds)

def import_into(bid, cmds, data, merge, with_data=True):
    n = replace_cmds(bid, cmds, merge) if cmds else len(get_cmds(bid))
    nd = 0
    if data and with_data:
        c = dbc(bid)
        for k, v in data.items(): c.execute("INSERT OR REPLACE INTO bot_data VALUES(?,?)", (str(k), json.dumps(v, ensure_ascii=False))); nd += 1
        c.commit(); c.close()
    return n, nd

# ------------------------------------------------------------------ web app
from flask import jsonify, send_file
import hashlib
app = Flask(__name__, template_folder=os.path.join(HERE, "templates"), static_folder=os.path.join(HERE, "static"))
keyfile = os.path.join(DATA_DIR, "secret.key")
if not os.path.exists(keyfile): open(keyfile, "w").write(secrets.token_hex(32))
app.secret_key = open(keyfile).read().strip()
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", MAX_CONTENT_LENGTH=60 * 1024 * 1024,
                  MAX_FORM_MEMORY_SIZE=60 * 1024 * 1024, PERMANENT_SESSION_LIFETIME=60 * 60 * 24 * 7, TEMPLATES_AUTO_RELOAD=True)
_fails = {}
def _ip(): return request.headers.get("X-Forwarded-For", request.remote_addr or "?").split(",")[0].strip()

@app.before_request
def guard():
    if request.path.startswith(("/wh/", "/app/", "/static/")) or request.path in ("/health", "/login"): return
    if not session.get("ok"): return redirect("/login")
    if request.method == "POST":
        tok = request.form.get("csrf") or request.headers.get("X-CSRF")
        if not tok or not hmac.compare_digest(tok, session.get("csrf", "")): abort(400, "bad csrf token (refresh the page)")

@app.after_request
def nocache(resp):
    if not request.path.startswith("/static/"): resp.headers["Cache-Control"] = "no-store"
    return resp

@app.context_processor
def inject():
    if "csrf" not in session: session["csrf"] = secrets.token_hex(16)
    def recent_errors():
        def f():
            n = 0
            for b in q("SELECT id FROM bots"):
                try: n += sum(1 for e in get_errors(b["id"], 5) if time.time() - e["ts"] < 3600)
                except Exception: pass
            return n
        return cached("recent_errors", 30, f)
    return {"csrf": session["csrf"], "APP_TITLE": setting("title") or APP_TITLE, "recent_errors": recent_errors if session.get("ok") else (lambda: 0)}

@app.template_filter("compact")
def compact(n):
    n = int(n or 0)
    return "%.1fk" % (n / 1000.0) if n >= 100000 and False else ("%dk" % round(n / 1000.0) if n >= 10000 else "{:,}".format(n))
@app.template_filter("date")
def f_date(ts): return time.strftime("%-d %b %Y", time.localtime(ts)) if ts else "—"
@app.template_filter("dt")
def f_dt(ts): return time.strftime("%-d %b, %H:%M", time.localtime(ts)) if ts else "—"
@app.template_filter("uq")
def f_uq(s): return requests.utils.quote(str(s), safe="")

@app.route("/health")
def health(): return "ok"

@app.route("/login", methods=["GET", "POST"])
def login():
    err = ""
    if request.method == "POST":
        ip = _ip(); f = _fails.get(ip, (0, 0))
        if f[0] >= 5 and time.time() - f[1] < 300: err = "Too many attempts. Wait 5 minutes."
        elif check_pw(request.form.get("password", "")):
            session.clear(); session["ok"] = True; session["csrf"] = secrets.token_hex(16); session.permanent = True
            _fails.pop(ip, None); return redirect("/")
        else: _fails[ip] = (f[0] + 1 if time.time() - f[1] < 300 else 1, time.time()); err = "Wrong password"
    return render_template("login.html", err=err)

@app.route("/logout", methods=["POST"])
def logout(): session.clear(); return redirect("/login")

@app.route("/")
def dashboard(): return render_template("dashboard.html", d=dash_data(), nav="home")

@app.route("/bots")
def bots():
    ov = bots_overview(); f = request.args.get("f", "all"); qs = request.args.get("q", "").strip().lower()
    shown = ov
    if f == "pinned": shown = [b for b in ov if b["pinned"]]
    elif f in ("running", "stopped", "error"): shown = [b for b in ov if b["state"] == f]
    if qs: shown = [b for b in shown if qs in b["name"].lower() or qs in b["username"].lower() or qs == str(b["id"])]
    return render_template("bots.html", bots=shown, f=f, qs=qs, total=len(ov), pinned=sum(1 for b in ov if b["pinned"]),
                           allusers=sum(b["users"] for b in ov), nav="bots")

@app.route("/bots/new")
def bots_new(): return render_template("bots_new.html", all_bots=bots_overview(), nav="bots")

@app.route("/bots/add", methods=["POST"])
def bots_add():
    lines = [l.strip() for l in request.form.get("tokens", "").splitlines() if l.strip()]
    tokens = [m.group(0) for l in lines for m in [re.search(r"\d{6,}:[A-Za-z0-9_-]{30,}", l)] if m]
    src = request.form.get("copy_from", ""); start = request.form.get("start") == "1"
    tcmds, tdata = {}, {}
    f = request.files.get("file")
    if f and f.filename: tcmds, tdata = parse_any(f.read().decode("utf-8", "replace"))
    elif src.isdigit(): tcmds = dict(get_cmds(int(src)))
    ok = bad = 0
    for t in tokens:
        if q1("SELECT id FROM bots WHERE token=?", (t,)): flash("Already added: %s…" % t[:10]); continue
        good, info = fetch_me(t)
        if not good: bad += 1; flash("Token %s…: %s" % (t[:10], info)); continue
        cur = x("INSERT INTO bots(token,name,username,enabled,created,tg_id) VALUES(?,?,?,?,?,?)", (t, info.get("first_name"), info.get("username"), 1 if start else 0, time.time(), info.get("id")))
        bid = cur.lastrowid; save_cmds_file(bid, dict(tcmds)); ok += 1
        if tdata: import_into(bid, {}, tdata, True)
        if start: runner(bid).start()
    flash("Added %d bot(s)%s." % (ok, ", %d failed" % bad if bad else ""))
    return redirect("/bots")

@app.route("/bots/bulk", methods=["POST"])
def bots_bulk():
    act = request.form.get("action"); n = 0
    for b in q("SELECT id FROM bots"):
        r = runner(b["id"])
        if act == "start_all" and not r.alive: x("UPDATE bots SET enabled=1 WHERE id=?", (b["id"],)); r.start(); n += 1; time.sleep(0.05)
        elif act == "stop_all" and r.alive: x("UPDATE bots SET enabled=0 WHERE id=?", (b["id"],)); r.stop(); n += 1
    flash("%s %d bot(s)" % ("Started" if act == "start_all" else "Stopped", n)); return redirect("/bots")

@app.route("/bots/export-all")
def export_all():
    import zipfile
    buf = io.BytesIO(); z = zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED)
    for b in q("SELECT id,username FROM bots"):
        z.writestr("%s_%d.json" % (b["username"] or "bot", b["id"]), json.dumps(bot_export_obj(b["id"], request.args.get("data") == "1"), ensure_ascii=False))
    z.close(); buf.seek(0)
    return Response(buf.read(), mimetype="application/zip", headers={"Content-Disposition": "attachment; filename=all_bots.zip"})

@app.route("/bots/import-zip", methods=["POST"])
def import_zip():
    import zipfile
    f = request.files.get("file")
    if not f or not f.filename: flash("Choose a .zip file"); return redirect("/bots/new")
    merge = request.form.get("mode") == "merge"
    try: z = zipfile.ZipFile(io.BytesIO(f.read()))
    except Exception: flash("Not a valid zip file"); return redirect("/bots/new")
    rows = [(b["id"], (b["username"] or "").lower()) for b in q("SELECT id,username FROM bots") if b["username"]]
    done, skipped = 0, []
    for info in z.infolist():
        if info.is_dir() or not info.filename.lower().endswith((".txt", ".py", ".json", ".tpy")): continue
        base = os.path.basename(info.filename).rsplit(".", 1)[0].lower()
        hits = sorted([(len(u), bid) for bid, u in rows if u and u in base], reverse=True)
        if not hits: skipped.append(os.path.basename(info.filename)); continue
        cmds, data = parse_any(z.read(info).decode("utf-8", "replace"))
        if not cmds and not data: skipped.append(os.path.basename(info.filename) + " (nothing found)"); continue
        import_into(hits[0][1], cmds, data, merge); done += 1
    flash("Imported into %d bot(s)." % done + (" Skipped: " + ", ".join(skipped[:8]) + ("…" if len(skipped) > 8 else "") if skipped else ""))
    return redirect("/bots")

def _bot_or_404(bid):
    b = q1("SELECT * FROM bots WHERE id=?", (bid,))
    if not b: abort(404)
    return b

@app.route("/bots/<int:bid>/action", methods=["POST"])
def bot_action(bid):
    _bot_or_404(bid); act = request.form.get("action"); r = runner(bid)
    if act == "start": x("UPDATE bots SET enabled=1 WHERE id=?", (bid,)); r.start()
    elif act == "stop": x("UPDATE bots SET enabled=0 WHERE id=?", (bid,)); r.stop()
    elif act == "restart": x("UPDATE bots SET enabled=1 WHERE id=?", (bid,)); r.restart()
    elif act == "pin": x("UPDATE bots SET pinned=1-COALESCE(pinned,0) WHERE id=?", (bid,))
    elif act == "delete":
        r.stop(wait=True); RUNNERS.pop(bid, None); x("DELETE FROM bots WHERE id=?", (bid,))
        if request.form.get("purge") == "1": shutil.rmtree(bot_dir(bid), ignore_errors=True)
        flash("Bot deleted"); return redirect("/bots")
    return redirect(request.form.get("next") or "/bots/%d/intro" % bid)

TABS = [("intro", "Intro", "layout"), ("commands", "Commands", "code"), ("search", "Search", "search"), ("miniapp", "Mini App", "code"),
        ("manage", "Manage", "gear"), ("admin", "Admin", "users"), ("settings", "Settings", "sliders")]

def bot_ctx(bid, tab):
    b = _bot_or_404(bid); r = RUNNERS.get(bid)
    return dict(b=b, bid=bid, tab=tab, tabs=TABS, nav="bots", state=r.state if r else "stopped", err=r.err if r else "",
                nerr=error_count(bid), started=(r.mod.STATS["started"] if (r and r.alive and r.mod) else 0))

@app.route("/bots/<int:bid>")
def bot_home(bid): _bot_or_404(bid); return redirect("/bots/%d/intro" % bid)

@app.route("/bots/<int:bid>/<tab>", methods=["GET", "POST"])
def bot_tab(bid, tab):
    if tab not in [t[0] for t in TABS]: abort(404)
    c = bot_ctx(bid, tab); b = c["b"]; cmds = get_cmds(bid)
    if request.method == "POST":
        if tab == "miniapp":
            open(os.path.join(bot_dir(bid), "miniapp.html"), "w", encoding="utf-8").write(request.form.get("html", ""))
            if not b["miniapp_secret"]: x("UPDATE bots SET miniapp_secret=? WHERE id=?", (secrets.token_urlsafe(9), bid))
            flash("Mini app saved"); return redirect("/bots/%d/miniapp" % bid)
        if tab == "settings":
            if request.form.get("do") == "token":
                t = request.form.get("token", "").strip(); good, info = fetch_me(t)
                if not good: flash("Token rejected: %s" % info)
                elif q1("SELECT id FROM bots WHERE token=? AND id<>?", (t, bid)): flash("That token is already used by another bot")
                else:
                    x("UPDATE bots SET token=?, name=?, username=?, tg_id=? WHERE id=?", (t, info.get("first_name"), info.get("username"), info.get("id"), bid))
                    r = runner(bid); was = r.alive; r.stop(wait=True); RUNNERS.pop(bid, None)
                    if was: runner(bid).start()
                    flash("Token updated")
            else:
                ec = request.form.get("error_chat", "").strip()
                x("UPDATE bots SET name=?, error_chat=?, note=? WHERE id=?", (request.form.get("name", "").strip() or b["name"], ec, request.form.get("note", ""), bid))
                r = RUNNERS.get(bid)
                if r and r.mod: r.mod.CFG["error_chat"] = ec or setting("error_chat")
                flash("Settings saved")
            return redirect("/bots/%d/settings" % bid)
        abort(405)
    if tab == "intro":
        s = user_stats(bid); c.update(users=s["total"], last=s["last"], ncmds=len(cmds), url="https://t.me/%s" % b["username"])
    elif tab == "commands":
        recent = {e["command"] for e in get_errors(bid, 60)}
        c.update(names=sorted(cmds, key=lambda n: n.lower()), errcmds=recent, ncmds=len(cmds))
    elif tab == "search": c.update(ncmds=len(cmds))
    elif tab == "miniapp":
        p = os.path.join(bot_dir(bid), "miniapp.html"); html = open(p, encoding="utf-8").read() if os.path.exists(p) else DEFAULT_MINIAPP
        base = PUBLIC_URL or request.host_url.rstrip("/")
        c.update(html=html, url=("%s/app/%s" % (base, b["miniapp_secret"])) if b["miniapp_secret"] else "")
    elif tab == "manage": c.update(others=[o for o in bots_overview() if o["id"] != bid], ncmds=len(cmds))
    elif tab == "admin": return redirect("/bots/%d/admin/analytics" % bid)
    elif tab == "settings": c.update(global_chat=setting("error_chat"))
    return render_template("bot_%s.html" % tab, **c)

DEFAULT_MINIAPP = """<!doctype html><html><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<script src="https://telegram.org/js/telegram-web-app.js"></script><title>Mini App</title></head>
<body style="font-family:sans-serif;text-align:center;padding:30px"><h2>Hello 👋</h2><p id="u"></p>
<script>const t=window.Telegram&&Telegram.WebApp;if(t){t.ready();document.getElementById('u').textContent=(t.initDataUnsafe.user||{}).first_name||''}</script></body></html>"""

@app.route("/app/<secret>")
def miniapp_serve(secret):
    b = q1("SELECT id FROM bots WHERE miniapp_secret=? AND miniapp_secret<>''", (secret,))
    if not b: abort(404)
    p = os.path.join(bot_dir(b["id"]), "miniapp.html")
    if not os.path.exists(p): abort(404)
    return Response(open(p, encoding="utf-8").read(), mimetype="text/html")

# ---- commands: edit / bulk delete / syntax check / search / replace
@app.route("/bots/<int:bid>/cmd", methods=["GET", "POST"])
def cmd_edit(bid):
    c = bot_ctx(bid, "commands"); name = request.values.get("name", ""); cmds = get_cmds(bid); msg = ""
    if request.method == "POST":
        newname = request.form.get("newname", "").strip(); code = request.form.get("code", "").replace("\r\n", "\n")
        if request.form.get("do") == "delete":
            apply_cmd_change(bid, name, None); flash("Deleted %s" % name); return redirect("/bots/%d/commands" % bid)
        if not newname: msg = "Name is required"
        else:
            try: compile(code, "<tpy>", "exec")
            except SyntaxError as e: msg = "Syntax error on line %s: %s" % (e.lineno, e.msg); c["synline"] = e.lineno
            if not msg:
                if name and newname != name: apply_cmd_change(bid, name, None)
                apply_cmd_change(bid, newname, code)
                flash("Saved %s%s" % (newname, " — live on the running bot" if runner(bid).alive else ""))
                return redirect("/bots/%d/cmd?name=%s" % (bid, f_uq(newname)))
        c.update(name=name, newname=newname, code=code, msg=msg, isnew=not name)
    else: c.update(name=name, newname=name, code=cmds.get(name, ""), msg="", isnew=not name)
    errs = [e for e in get_errors(bid, 60) if e["command"] == (c["name"] or c.get("newname"))][:1]
    c["lasterr"] = errs[0] if errs else None
    return render_template("cmd.html", **c)

@app.route("/bots/<int:bid>/cmds/delete", methods=["POST"])
def cmds_delete(bid):
    _bot_or_404(bid); names = request.form.getlist("names")
    bulk_update(bid, {n: None for n in names}); flash("Deleted %d command(s)" % len(names)); return redirect("/bots/%d/commands" % bid)

@app.route("/bots/<int:bid>/check.json")
def cmds_check(bid):
    _bot_or_404(bid); bad = []
    for n, code in get_cmds(bid).items():
        try: compile(code, "<tpy %s>" % n, "exec")
        except SyntaxError as e: bad.append({"name": n, "line": e.lineno, "msg": e.msg})
    return jsonify(total=len(get_cmds(bid)), bad=bad)

def _pattern(qs, case, word, regex):
    pat = qs if regex else re.escape(qs)
    if word: pat = r"\b(?:%s)\b" % pat
    return re.compile(pat, 0 if case else re.I)

@app.route("/bots/<int:bid>/search.json")
def cmds_search(bid):
    _bot_or_404(bid); qs = request.args.get("q", "")
    if not qs: return jsonify(results=[], total=0)
    try: pat = _pattern(qs, request.args.get("case") == "1", request.args.get("word") == "1", request.args.get("regex") == "1")
    except re.error as e: return jsonify(error="Invalid regex: %s" % e)
    out = []; total = 0
    for n, code in sorted(get_cmds(bid).items()):
        cnt = len(pat.findall(code))
        if not cnt: continue
        total += cnt; lines = []
        for i, l in enumerate(code.split("\n"), 1):
            if pat.search(l):
                lines.append({"n": i, "t": l.strip()[:160]})
                if len(lines) >= 4: break
        out.append({"name": n, "count": cnt, "lines": lines})
        if len(out) >= 200: break
    return jsonify(results=out, total=total)

@app.route("/bots/<int:bid>/replace", methods=["POST"])
def cmds_replace(bid):
    _bot_or_404(bid); qs = request.form.get("q", ""); repl = request.form.get("repl", ""); regex = request.form.get("regex") == "1"
    if not qs: return jsonify(error="Type something to search first")
    try: pat = _pattern(qs, request.form.get("case") == "1", request.form.get("word") == "1", regex)
    except re.error as e: return jsonify(error="Invalid regex: %s" % e)
    changes = {}; broken = []; n = 0
    for name, code in get_cmds(bid).items():
        cnt = len(pat.findall(code))
        if not cnt: continue
        try: new = pat.sub(repl if regex else (lambda m: repl), code)
        except re.error as e: return jsonify(error="Bad replacement: %s" % e)
        try: compile(new, "<tpy>", "exec")
        except SyntaxError:
            try: compile(code, "<tpy>", "exec"); broken.append(name); continue     # replacement would break a working command: skip it
            except SyntaxError: pass
        changes[name] = new; n += cnt
    if changes: bulk_update(bid, changes)
    return jsonify(replaced=n, commands=len(changes), skipped=broken)

# ---- import / export
@app.route("/bots/<int:bid>/import", methods=["POST"])
def cmd_import(bid):
    _bot_or_404(bid); f = request.files.get("file"); txt = request.form.get("text", "")
    if f and f.filename: txt = f.read().decode("utf-8", "replace")
    cmds, data = parse_any(txt)
    if not cmds and not data: flash("Nothing found in that file. Send me a sample and I will add support for its format."); return redirect("/bots/%d/manage" % bid)
    n, nd = import_into(bid, cmds, data, request.form.get("mode") == "merge", request.form.get("with_data") == "1")
    flash("Imported %d commands%s (bot now has %d)." % (len(cmds), (" and %d data keys" % nd) if nd else "", n)); return redirect("/bots/%d/commands" % bid)

@app.route("/bots/<int:bid>/export.json")
def export_json(bid):
    _bot_or_404(bid); b = q1("SELECT username FROM bots WHERE id=?", (bid,))
    o = bot_export_obj(bid, request.args.get("data") == "1", request.args.get("users") == "1")
    return Response(json.dumps(o, ensure_ascii=False, indent=1), mimetype="application/json", headers={"Content-Disposition": "attachment; filename=%s_%d.json" % (b["username"] or "bot", bid)})

@app.route("/bots/<int:bid>/export.txt")
def export_txt(bid):
    _bot_or_404(bid)
    body = "\n".join("=== %s ===\n%s\n" % (k, v) for k, v in sorted(get_cmds(bid).items()))
    return Response(body, mimetype="text/plain", headers={"Content-Disposition": "attachment; filename=bot_%d_commands.txt" % bid})

# ---- errors
@app.route("/bots/<int:bid>/errors", methods=["GET", "POST"])
def bot_errors(bid):
    c = bot_ctx(bid, "intro")
    if request.method == "POST":
        if os.path.exists(db_file(bid)): d = dbc(bid); d.execute("DELETE FROM errors"); d.commit(); d.close()
        _cache.pop(("ec", bid), None); flash("Errors cleared"); return redirect("/bots/%d/errors" % bid)
    return render_template("bot_errors.html", errors=get_errors(bid, 100), **c)

@app.route("/errors")
def all_errors():
    rows = []
    for b in q("SELECT id,name,username FROM bots"):
        for e in get_errors(b["id"], 15): e["bot"] = b; rows.append(e)
    rows.sort(key=lambda e: -e["ts"]); return render_template("errors.html", errors=rows[:100], nav="errors")

# ---- admin tab
ADMIN_SUBS = [("analytics", "Analytics"), ("users", "Users"), ("broadcasts", "Broadcasts"), ("data", "Bot Data")]
@app.route("/bots/<int:bid>/admin/<sub>")
def bot_admin(bid, sub):
    if sub not in [s[0] for s in ADMIN_SUBS]: abort(404)
    c = bot_ctx(bid, "admin"); c.update(sub=sub, subs=ADMIN_SUBS); cmds = get_cmds(bid)
    if sub == "analytics":
        rows = sorted(((n, code.count("\n") + 1) for n, code in cmds.items()), key=lambda r: -r[1])
        c.update(s=user_stats(bid), rows=rows[:60], mx=(rows[0][1] if rows else 1), ncmds=len(cmds))
    elif sub == "users":
        page = max(1, int(request.args.get("page", 1))); qs = request.args.get("q", "").strip(); rows = []; tot = 0
        if os.path.exists(db_file(bid)):
            d = dbc(bid); tot = d.execute("SELECT COUNT(*) FROM users WHERE user LIKE ?", ("%" + qs + "%",)).fetchone()[0]
            rows = d.execute("SELECT user,first_seen,last_seen,COALESCE(blocked,0) FROM users WHERE user LIKE ? ORDER BY last_seen DESC LIMIT 40 OFFSET ?", ("%" + qs + "%", (page - 1) * 40)).fetchall(); d.close()
        c.update(rows=rows, tot=tot, page=page, qs=qs, pages=max(1, (tot + 39) // 40))
    elif sub == "broadcasts":
        r = RUNNERS.get(bid); rows = []
        if os.path.exists(db_file(bid)):
            d = dbc(bid); rows = d.execute("SELECT id,ts,text,total,ok,err,status FROM broadcasts ORDER BY ts DESC LIMIT 15").fetchall(); d.close()
        c.update(rows=rows, running=bool(r and r.alive and r.mod and r.mod.BOT_INFO.get("bot_id")), s=user_stats(bid))
    elif sub == "data":
        qs = request.args.get("q", "").strip(); rows = []; counts = (0, 0, 0)
        if os.path.exists(db_file(bid)):
            d = dbc(bid)
            rows = d.execute("SELECT name, substr(value,1,90), length(value) FROM bot_data WHERE name LIKE ? ORDER BY name LIMIT 300", ("%" + qs + "%",)).fetchall()
            counts = d.execute("SELECT (SELECT COUNT(*) FROM bot_data),(SELECT COUNT(*) FROM user_data),(SELECT COUNT(*) FROM users)").fetchone(); d.close()
        c.update(rows=rows, qs=qs, counts=counts)
    return render_template("admin_%s.html" % sub, **c)

@app.route("/bots/<int:bid>/user/<uid>", methods=["GET", "POST"])
def bot_user(bid, uid):
    c = bot_ctx(bid, "admin"); c.update(sub="users", subs=ADMIN_SUBS); d = dbc(bid)
    if request.method == "POST":
        if request.form.get("do") == "res":
            d.execute("INSERT OR REPLACE INTO res VALUES('user',?,?,?)", (uid, request.form.get("name", ""), float(request.form.get("value") or 0)))
        elif request.form.get("do") == "block":
            d.execute("UPDATE users SET blocked=1-COALESCE(blocked,0) WHERE user=?", (uid,))
        d.commit(); d.close(); _cache.pop(("us", bid), None); return redirect("/bots/%d/user/%s" % (bid, uid))
    u = d.execute("SELECT user,first_seen,last_seen,COALESCE(blocked,0) FROM users WHERE user=?", (uid,)).fetchone()
    kv = d.execute("SELECT name, substr(value,1,160) FROM user_data WHERE user=? ORDER BY name", (uid,)).fetchall()
    res = d.execute("SELECT name,value FROM res WHERE scope='user' AND user=? ORDER BY name", (uid,)).fetchall(); d.close()
    if not u: abort(404)
    c.update(u=u, kv=kv, res=res); return render_template("admin_user.html", **c)

@app.route("/bots/<int:bid>/broadcast", methods=["POST"])
def bot_broadcast(bid):
    _bot_or_404(bid); r = RUNNERS.get(bid); text = request.form.get("text", "").strip()
    if not (r and r.alive and r.mod and r.mod.BOT_INFO.get("bot_id")): flash("Start the bot first."); return redirect("/bots/%d/admin/broadcasts" % bid)
    if not text: flash("Write a message first."); return redirect("/bots/%d/admin/broadcasts" % bid)
    markup = None
    if request.form.get("btn_text") and request.form.get("btn_url"):
        markup = {"inline_keyboard": [[{"text": request.form["btn_text"], "url": request.form["btn_url"]}]]}
    days = request.form.get("days"); bcid = r.mod.start_broadcast(text, request.form.get("parse_mode") or "HTML", int(days) if days and days.isdigit() else None, markup)
    flash("Broadcast started (%s)." % bcid); return redirect("/bots/%d/admin/broadcasts" % bid)

@app.route("/bots/<int:bid>/broadcast/<bcid>.json")
def bot_broadcast_status(bid, bcid):
    r = RUNNERS.get(bid)
    if r and r.mod and bcid in r.mod.BROADCASTS: return jsonify({k: v for k, v in r.mod.BROADCASTS[bcid].items()})
    return jsonify(status="unknown")

@app.route("/bots/<int:bid>/data/edit", methods=["GET", "POST"])
def data_edit(bid):
    c = bot_ctx(bid, "admin"); c.update(sub="data", subs=ADMIN_SUBS); key = request.values.get("key", ""); msg = ""; d = dbc(bid)
    if request.method == "POST":
        if request.form.get("do") == "delete":
            d.execute("DELETE FROM bot_data WHERE name=?", (key,)); d.commit(); d.close(); flash("Deleted"); return redirect("/bots/%d/admin/data" % bid)
        newkey = request.form.get("newkey", "").strip(); val = request.form.get("value", "")
        try: json.loads(val)
        except Exception: msg = "Value must be valid JSON (strings need quotes, e.g. \"abc\")"
        if not msg and newkey:
            d.execute("INSERT OR REPLACE INTO bot_data VALUES(?,?)", (newkey, val)); d.commit(); d.close()
            flash("Saved %s" % newkey); return redirect("/bots/%d/data/edit?key=%s" % (bid, f_uq(newkey)))
        d.close(); c.update(key=key, newkey=newkey, value=val, msg=msg); return render_template("admin_dataedit.html", **c)
    r = d.execute("SELECT value FROM bot_data WHERE name=?", (key,)).fetchone(); d.close(); val = r[0] if r else ""
    try: val = json.dumps(json.loads(val), indent=2, ensure_ascii=False)
    except Exception: pass
    c.update(key=key, newkey=key, value=val, msg=""); return render_template("admin_dataedit.html", **c)

@app.route("/bots/<int:bid>/data/import", methods=["POST"])
def data_import(bid):
    _bot_or_404(bid); f = request.files.get("file"); txt = request.form.get("text", "")
    if f and f.filename: txt = f.read().decode("utf-8", "replace")
    try:
        o = json.loads(txt); assert isinstance(o, dict); o = extract_data(o) or o
    except Exception: flash("Need a JSON object like {\"key\": value, ...}"); return redirect("/bots/%d/admin/data" % bid)
    _, nd = import_into(bid, {}, o, True); flash("Imported %d keys. Restart the bot to be safe." % nd); return redirect("/bots/%d/admin/data" % bid)

@app.route("/bots/<int:bid>/data/export.json")
def data_export(bid):
    _bot_or_404(bid); d = dbc(bid); o = {k: _dec(v) for k, v in d.execute("SELECT name,value FROM bot_data").fetchall()}; d.close()
    return Response(json.dumps(o, ensure_ascii=False, indent=1), mimetype="application/json", headers={"Content-Disposition": "attachment; filename=bot_%d_data.json" % bid})

# ---- more / settings (panel level)
@app.route("/more")
def more(): return render_template("more.html", nav="more")

@app.route("/settings", methods=["GET", "POST"])
def panel_settings():
    if request.method == "POST":
        do = request.form.get("do")
        if do == "password":
            if not check_pw(request.form.get("old", "")): flash("Current password is wrong")
            elif len(request.form.get("new", "")) < 8: flash("New password must be at least 8 characters")
            else: set_setting("pw_hash", _hash_pw(request.form["new"])); flash("Password changed")
        elif do == "general":
            set_setting("error_chat", request.form.get("error_chat", "").strip()); set_setting("title", request.form.get("title", "").strip()); flash("Saved")
        return redirect("/settings")
    return render_template("settings.html", nav="settings", error_chat=setting("error_chat"), title=setting("title"), port=PORT, public=PUBLIC_URL,
                           pwgen=PW_GENERATED and not setting("pw_hash"))

@app.route("/backup.zip")
def backup():
    import zipfile
    buf = io.BytesIO(); z = zipfile.ZipFile(buf, "w", zipfile.ZIP_DEFLATED)
    for root, _, files in os.walk(DATA_DIR):
        for fn in files:
            if fn.endswith(("-wal", "-shm", ".tmp", ".key")) or fn == "panel_password.txt": continue
            p = os.path.join(root, fn); z.write(p, os.path.relpath(p, DATA_DIR))
    z.close(); buf.seek(0)
    return Response(buf.read(), mimetype="application/zip", headers={"Content-Disposition": "attachment; filename=panel_backup.zip"})

@app.route("/wh/<secret>/<path:command>/<uid>", methods=["GET", "POST"], strict_slashes=False)
def webhook(secret, command, uid):
    r = WEBHOOKS.get(secret)
    if not r or not r.alive or not r.mod: abort(404)
    body = r.mod.handle_webhook(command, uid, request.get_data(as_text=True), request.query_string.decode())
    return Response(body, mimetype="application/json")

def autostart():
    rows = q("SELECT id,token FROM bots WHERE enabled=1 ORDER BY id")
    print("auto-starting %d bots..." % len(rows), flush=True)
    for r in rows:
        try: runner(r["id"]).start()
        except Exception: traceback.print_exc()
        time.sleep(0.15)

def main():
    threading.Thread(target=autostart, daemon=True).start()
    threading.Thread(target=sampler, daemon=True).start()
    print("=" * 60, flush=True)
    print("Panel starting on %s:%d" % (HOST, PORT), flush=True)
    if PW_GENERATED and not setting("pw_hash"):
        print("PANEL_PASSWORD was not set -> generated password:  %s" % PASSWORD, flush=True)
        print("(saved in %s ; set PANEL_PASSWORD or change it in Settings)" % _PWFILE, flush=True)
    print("Open:  http://<your-server-ip>:%d   (health check: /health)" % PORT, flush=True)
    print("=" * 60, flush=True)
    try:
        from waitress import serve
        serve(app, host=HOST, port=PORT, threads=16)
    except ImportError:
        app.run(host=HOST, port=PORT, threaded=True)

if __name__ == "__main__":
    main()
