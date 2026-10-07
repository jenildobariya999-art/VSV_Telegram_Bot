#!/usr/bin/env python3
"""
TBC-Lite panel: run MANY Telebot-Creator (TPY) bots on your own server with a web dashboard.
  python tbc_panel.py        (needs PANEL_PASSWORD in .env or environment)
"""
import os, sys, json, time, threading, types, secrets, hmac, re, sqlite3, traceback, io, shutil
import requests
from flask import Flask, request, redirect, session, render_template, abort, Response, url_for, flash
from jinja2 import DictLoader

HERE = os.path.dirname(os.path.abspath(__file__))
def _load_env():
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1); os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
_load_env()

PASSWORD = os.environ.get("PANEL_PASSWORD", "")
HOST = os.environ.get("PANEL_HOST", "0.0.0.0")
PORT = int(os.environ.get("PANEL_PORT", "8000"))
PUBLIC_URL = os.environ.get("PUBLIC_URL", "").rstrip("/")
DATA_DIR = os.path.abspath(os.environ.get("DATA_DIR", os.path.join(HERE, "data")))
WORKERS_PER_BOT = int(os.environ.get("WORKERS_PER_BOT", "4"))
BOTS_DIR = os.path.join(DATA_DIR, "bots")
os.makedirs(BOTS_DIR, exist_ok=True)
RUNTIME_PATH = os.path.join(HERE, "tbc_runtime.py")
RUNTIME_CODE = compile(open(RUNTIME_PATH, encoding="utf-8").read(), RUNTIME_PATH, "exec")

# ------------------------------------------------------------------ panel database
_pdb = sqlite3.connect(os.path.join(DATA_DIR, "panel.sqlite3"), check_same_thread=False, isolation_level=None, timeout=30)
_pdb.row_factory = sqlite3.Row
_plock = threading.RLock()
_pdb.execute("""CREATE TABLE IF NOT EXISTS bots(id INTEGER PRIMARY KEY AUTOINCREMENT, token TEXT UNIQUE,
    name TEXT, username TEXT, enabled INTEGER DEFAULT 0, created REAL, note TEXT DEFAULT '')""")
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
               "public_url": PUBLIC_URL or "http://127.0.0.1:%d" % PORT}
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

# ------------------------------------------------------------------ stats helpers (cached)
_cache = {}
def cached(key, ttl, fn):
    v = _cache.get(key)
    if v and time.time() - v[0] < ttl: return v[1]
    val = fn(); _cache[key] = (time.time(), val); return val

def user_counts(bid):
    def f():
        p = db_file(bid)
        if not os.path.exists(p): return (0, 0)
        try:
            c = sqlite3.connect(p, timeout=10)
            tot = c.execute("SELECT COUNT(*) FROM users").fetchone()[0]
            act = c.execute("SELECT COUNT(*) FROM users WHERE last_seen>?", (time.time() - 86400,)).fetchone()[0]
            c.close(); return (tot, act)
        except Exception: return (0, 0)
    return cached(("uc", bid), 30, f)

def bots_overview():
    rows = q("SELECT * FROM bots ORDER BY id DESC")
    out = []
    for b in rows:
        r = RUNNERS.get(b["id"])
        tot, act = user_counts(b["id"])
        out.append({"id": b["id"], "name": b["name"] or "?", "username": b["username"] or "", "enabled": b["enabled"],
                    "state": r.state if r else "stopped", "err": r.err if r else "", "users": tot, "active": act,
                    "cmds": len(get_cmds(b["id"])) if not (r and r.alive) else len(r.cmds or {})})
    return out

def hourly_series():
    now_h = int(time.time() // 3600); agg = {}
    for r in list(RUNNERS.values()):
        if r.mod:
            for h, n in list(r.mod.STATS["hours"].items()): agg[h] = agg.get(h, 0) + n
    return [agg.get(h, 0) for h in range(now_h - 23, now_h + 1)]

# ------------------------------------------------------------------ web app
app = Flask(__name__)
keyfile = os.path.join(DATA_DIR, "secret.key")
if not os.path.exists(keyfile): open(keyfile, "w").write(secrets.token_hex(32))
app.secret_key = open(keyfile).read().strip()
app.config.update(SESSION_COOKIE_HTTPONLY=True, SESSION_COOKIE_SAMESITE="Lax", MAX_CONTENT_LENGTH=40 * 1024 * 1024, MAX_FORM_MEMORY_SIZE=40 * 1024 * 1024,
                  PERMANENT_SESSION_LIFETIME=60 * 60 * 24 * 7)

_fails = {}
def _ip(): return request.headers.get("X-Forwarded-For", request.remote_addr or "?").split(",")[0].strip()

@app.before_request
def guard():
    if request.path.startswith("/wh/") or request.path == "/health": return
    if request.path == "/login": return
    if not session.get("ok"): return redirect("/login")
    if request.method == "POST":
        tok = request.form.get("csrf") or request.headers.get("X-CSRF")
        if not tok or not hmac.compare_digest(tok, session.get("csrf", "")): abort(400, "bad csrf token (refresh the page)")

@app.context_processor
def inject():
    if "csrf" not in session: session["csrf"] = secrets.token_hex(16)
    return {"csrf": session["csrf"]}

@app.route("/health")
def health(): return "ok"

@app.route("/login", methods=["GET", "POST"])
def login():
    err = ""
    if request.method == "POST":
        ip = _ip(); f = _fails.get(ip, (0, 0))
        if f[0] >= 5 and time.time() - f[1] < 300:
            err = "Too many attempts. Wait 5 minutes."
        elif hmac.compare_digest(request.form.get("password", ""), PASSWORD):
            session.clear(); session["ok"] = True; session["csrf"] = secrets.token_hex(16); session.permanent = True
            _fails.pop(ip, None); return redirect("/")
        else:
            _fails[ip] = (f[0] + 1 if time.time() - f[1] < 300 else 1, time.time()); err = "Wrong password"
    return render_template("login.html", err=err)

@app.route("/logout", methods=["POST"])
def logout():
    session.clear(); return redirect("/login")

@app.route("/")
def dashboard():
    ov = bots_overview()
    running = [b for b in ov if b["state"] == "running"]
    series = hourly_series(); mx = max(series) or 1
    cmds_run = sum(r.mod.STATS["commands"] for r in RUNNERS.values() if r.mod)
    errs = sum(r.mod.STATS["errors"] for r in RUNNERS.values() if r.mod)
    top = sorted(ov, key=lambda b: -b["users"])[:8]
    return render_template("dashboard.html", total=len(ov), running=len(running), users=sum(b["users"] for b in ov),
        active=sum(b["active"] for b in ov), cmds_run=cmds_run, errs=errs, series=series, mx=mx, top=top,
        errbots=[b for b in ov if b["state"] == "error"])

@app.route("/bots")
def bots():
    qs = request.args.get("q", "").strip().lower(); flt = request.args.get("f", "")
    ov = bots_overview()
    if qs: ov = [b for b in ov if qs in b["name"].lower() or qs in b["username"].lower() or qs == str(b["id"])]
    if flt: ov = [b for b in ov if b["state"] == flt]
    return render_template("bots.html", bots=ov, qs=qs, flt=flt, all_bots=bots_overview())

@app.route("/bots/add", methods=["POST"])
def bots_add():
    lines = [l.strip() for l in request.form.get("tokens", "").splitlines() if l.strip()]
    tokens = [m.group(0) for l in lines for m in [re.search(r"\d{6,}:[A-Za-z0-9_-]{30,}", l)] if m]
    src = request.form.get("copy_from", ""); start = request.form.get("start") == "1"
    src_cmds = get_cmds(int(src)) if src.isdigit() else {}
    ok = bad = 0
    for t in tokens:
        if q1("SELECT id FROM bots WHERE token=?", (t,)): flash("Already added: %s…" % t[:10]); continue
        good, info = fetch_me(t)
        if not good: bad += 1; flash("Token %s…: %s" % (t[:10], info)); continue
        cur = x("INSERT INTO bots(token,name,username,enabled,created) VALUES(?,?,?,?,?)",
                (t, info.get("first_name"), info.get("username"), 1 if start else 0, time.time()))
        bid = cur.lastrowid; save_cmds_file(bid, dict(src_cmds)); ok += 1
        if start: runner(bid).start()
    flash("Added %d bot(s)%s." % (ok, ", %d failed" % bad if bad else ""))
    return redirect("/bots")

@app.route("/bots/import-zip", methods=["POST"])
def import_zip():
    import zipfile
    f = request.files.get("file")
    if not f or not f.filename: flash("Choose a .zip file"); return redirect("/bots")
    merge = request.form.get("mode") == "merge"
    try: z = zipfile.ZipFile(io.BytesIO(f.read()))
    except Exception: flash("Not a valid zip file"); return redirect("/bots")
    bots_rows = [(b["id"], (b["username"] or "").lower()) for b in q("SELECT id,username FROM bots") if b["username"]]
    done, skipped = [], []
    for info in z.infolist():
        if info.is_dir() or not info.filename.lower().endswith((".txt", ".py", ".json", ".tpy")): continue
        base = os.path.basename(info.filename).rsplit(".", 1)[0].lower()
        hits = sorted([(len(u), bid) for bid, u in bots_rows if u and u in base], reverse=True)
        if not hits: skipped.append(os.path.basename(info.filename)); continue
        new = parse_commands_text(z.read(info).decode("utf-8", "replace"))
        if not new: skipped.append(os.path.basename(info.filename) + " (no commands found)"); continue
        replace_cmds(hits[0][1], new, merge); done.append("#%d" % hits[0][1])
    flash("Imported commands into %d bot(s)." % len(done) + (" Skipped: " + ", ".join(skipped[:8]) + ("…" if len(skipped) > 8 else "") if skipped else ""))
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
    elif act == "delete":
        r.stop(wait=True); RUNNERS.pop(bid, None); x("DELETE FROM bots WHERE id=?", (bid,))
        if request.form.get("purge") == "1": shutil.rmtree(bot_dir(bid), ignore_errors=True)
        flash("Bot deleted"); return redirect("/bots")
    return redirect(request.form.get("next") or "/bots/%d" % bid)

@app.route("/bots/<int:bid>")
def bot_page(bid):
    b = _bot_or_404(bid); r = RUNNERS.get(bid); qs = request.args.get("q", "").strip().lower()
    cmds = get_cmds(bid); names = sorted(n for n in cmds if qs in n.lower())
    tot, act = user_counts(bid)
    st = r.mod.STATS if (r and r.mod) else {"commands": 0, "errors": 0, "updates": 0}
    return render_template("bot.html", b=b, state=r.state if r else "stopped", err=r.err if r else "", names=names,
        ncmds=len(cmds), qs=qs, users=tot, active=act, st=st, size=lambda n: len(cmds[n]),
        hook=bool(PUBLIC_URL))

@app.route("/bots/<int:bid>/cmd", methods=["GET", "POST"])
def cmd_edit(bid):
    b = _bot_or_404(bid); name = request.values.get("name", ""); cmds = get_cmds(bid); msg = ""
    if request.method == "POST":
        newname = request.form.get("newname", "").strip(); code = request.form.get("code", "").replace("\r\n", "\n")
        if request.form.get("do") == "delete":
            apply_cmd_change(bid, name, None); flash("Deleted %s" % name); return redirect("/bots/%d" % bid)
        if not newname: msg = "Name is required"
        else:
            try: compile(code, "<tpy>", "exec")
            except SyntaxError as e: msg = "Syntax error line %s: %s" % (e.lineno, e.msg)
            if not msg:
                if name and newname != name: apply_cmd_change(bid, name, None)
                apply_cmd_change(bid, newname, code)
                flash("Saved %s%s" % (newname, " (live)" if runner(bid).alive else ""))
                return redirect("/bots/%d/cmd?name=%s" % (bid, requests.utils.quote(newname, safe="")))
        return render_template("cmd.html", b=b, name=name, newname=newname, code=code, msg=msg, isnew=not name)
    return render_template("cmd.html", b=b, name=name, newname=name, code=cmds.get(name, ""), msg="", isnew=not name)

@app.route("/bots/<int:bid>/import", methods=["POST"])
def cmd_import(bid):
    _bot_or_404(bid); f = request.files.get("file"); txt = request.form.get("text", "")
    if f and f.filename: txt = f.read().decode("utf-8", "replace")
    new = parse_commands_text(txt)
    if not new: flash("No commands found. Use blocks like:  === /start ===  then the code."); return redirect("/bots/%d" % bid)
    n = replace_cmds(bid, new, request.form.get("mode") == "merge")
    flash("Imported %d commands (bot now has %d)." % (len(new), n)); return redirect("/bots/%d" % bid)

@app.route("/bots/<int:bid>/export")
def cmd_export(bid):
    _bot_or_404(bid); cmds = get_cmds(bid)
    body = "\n".join("=== %s ===\n%s\n" % (k, v) for k, v in sorted(cmds.items()))
    return Response(body, mimetype="text/plain", headers={"Content-Disposition": "attachment; filename=bot_%d_commands.txt" % bid})

@app.route("/bots/<int:bid>/logs")
def logs(bid):
    b = _bot_or_404(bid); r = RUNNERS.get(bid)
    lines = list(r.mod.LOGBUF)[-300:] if (r and r.mod) else []
    return render_template("logs.html", b=b, lines=reversed(lines), err=r.err if r else "")

def dbc(bid):
    c = sqlite3.connect(db_file(bid), timeout=30); c.execute("PRAGMA journal_mode=WAL"); return c

@app.route("/bots/<int:bid>/data")
def data_list(bid):
    b = _bot_or_404(bid); qs = request.args.get("q", "").strip()
    rows = []
    if os.path.exists(db_file(bid)):
        c = dbc(bid)
        try:
            rows = c.execute("SELECT name, substr(value,1,90), length(value) FROM bot_data WHERE name LIKE ? ORDER BY name LIMIT 300", ("%" + qs + "%",)).fetchall()
            counts = c.execute("SELECT (SELECT COUNT(*) FROM bot_data),(SELECT COUNT(*) FROM user_data),(SELECT COUNT(*) FROM users)").fetchone()
        except Exception: counts = (0, 0, 0)
        c.close()
    else: counts = (0, 0, 0)
    return render_template("data.html", b=b, rows=rows, qs=qs, counts=counts)

@app.route("/bots/<int:bid>/data/edit", methods=["GET", "POST"])
def data_edit(bid):
    b = _bot_or_404(bid); key = request.values.get("key", ""); msg = ""
    if not os.path.exists(db_file(bid)): flash("Start the bot once to create its database."); return redirect("/bots/%d/data" % bid)
    c = dbc(bid)
    if request.method == "POST":
        if request.form.get("do") == "delete":
            c.execute("DELETE FROM bot_data WHERE name=?", (key,)); c.commit(); c.close(); flash("Deleted"); return redirect("/bots/%d/data" % bid)
        newkey = request.form.get("newkey", "").strip(); val = request.form.get("value", "")
        try: json.loads(val)
        except Exception: msg = "Value must be valid JSON (strings need quotes, e.g. \"abc\")"
        if not msg and newkey:
            c.execute("INSERT OR REPLACE INTO bot_data VALUES(?,?)", (newkey, val)); c.commit(); c.close()
            flash("Saved %s" % newkey); return redirect("/bots/%d/data/edit?key=%s" % (bid, requests.utils.quote(newkey, safe="")))
        c.close(); return render_template("dataedit.html", b=b, key=key, newkey=newkey, value=val, msg=msg)
    r = c.execute("SELECT value FROM bot_data WHERE name=?", (key,)).fetchone(); c.close()
    val = r[0] if r else ""
    try: val = json.dumps(json.loads(val), indent=2, ensure_ascii=False)
    except Exception: pass
    return render_template("dataedit.html", b=b, key=key, newkey=key, value=val, msg="")

@app.route("/bots/<int:bid>/data/import", methods=["POST"])
def data_import(bid):
    _bot_or_404(bid); f = request.files.get("file"); txt = request.form.get("text", "")
    if f and f.filename: txt = f.read().decode("utf-8", "replace")
    try: d = json.loads(txt); assert isinstance(d, dict)
    except Exception: flash("Need a JSON object like {\"key\": value, ...}"); return redirect("/bots/%d/data" % bid)
    if not os.path.exists(db_file(bid)): flash("Start the bot once first (creates its database)."); return redirect("/bots/%d/data" % bid)
    c = dbc(bid)
    for k, v in d.items(): c.execute("INSERT OR REPLACE INTO bot_data VALUES(?,?)", (str(k), json.dumps(v, ensure_ascii=False)))
    c.commit(); c.close(); flash("Imported %d keys. Restart the bot to be safe." % len(d)); return redirect("/bots/%d/data" % bid)

@app.route("/wh/<secret>/<path:command>/<uid>", methods=["GET", "POST"], strict_slashes=False)
def webhook(secret, command, uid):
    r = WEBHOOKS.get(secret)
    if not r or not r.alive or not r.mod: abort(404)
    body = r.mod.handle_webhook(command, uid, request.get_data(as_text=True), request.query_string.decode())
    return Response(body, mimetype="application/json")

# ------------------------------------------------------------------ templates
CSS = """
:root{--bg:#0b0b0f;--card:#14141b;--bd:#262633;--tx:#ececf3;--mu:#8b8ba0;--ac:#7c5cff;--gr:#34d27b;--rd:#ff5b6e;--yl:#f5b942}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--tx);font:15px/1.45 system-ui,Segoe UI,Roboto,sans-serif}
a{color:#a99bff;text-decoration:none}.wrap{max-width:980px;margin:0 auto;padding:14px 14px 90px}
nav{position:sticky;top:0;background:#0b0b0fee;backdrop-filter:blur(8px);border-bottom:1px solid var(--bd);z-index:5}
nav .in{max-width:980px;margin:0 auto;padding:10px 14px;display:flex;gap:16px;align-items:center}
nav b{font-size:17px}nav a{color:var(--mu)}nav a.on{color:var(--tx)}nav form{margin-left:auto}
.card{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:14px;margin:12px 0}
.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:10px}
.stat{background:var(--card);border:1px solid var(--bd);border-radius:14px;padding:12px 14px}
.stat small{color:var(--mu);display:block}.stat b{font-size:24px}
h1,h2{margin:.5em 0}h1{font-size:24px}h2{font-size:13px;letter-spacing:.08em;color:var(--mu);text-transform:uppercase}
input,select,textarea,button{font:inherit;color:var(--tx);background:#0f0f15;border:1px solid var(--bd);border-radius:10px;padding:9px 11px}
input,select,textarea{width:100%}textarea{font-family:ui-monospace,Menlo,Consolas,monospace;font-size:13px;line-height:1.4}
button,.btn{background:var(--ac);border:0;color:#fff;cursor:pointer;padding:9px 14px;border-radius:10px;display:inline-block}
button.g,.btn.g{background:#22222e;color:var(--tx)}button.r{background:#4a1f27;color:#ff9aa8}button.s{padding:5px 10px;font-size:13px}
.row{display:flex;gap:8px;align-items:center;flex-wrap:wrap}.row>*{flex:0 0 auto}.grow{flex:1!important}
.bot{display:flex;gap:10px;align-items:center;padding:12px 0;border-top:1px solid var(--bd)}.bot:first-child{border:0}
.dot{width:10px;height:10px;border-radius:50%;background:#555;flex:none}.running .dot{background:var(--gr)}.error .dot{background:var(--rd)}.starting .dot,.stopping .dot{background:var(--yl)}
.mu{color:var(--mu)}.pill{background:#1e1e2a;border-radius:99px;padding:2px 10px;font-size:12px;color:var(--mu)}
.flash{background:#1d2a22;border:1px solid #2c5a3f;color:#9be5b8;padding:10px 12px;border-radius:10px;margin:10px 0}
.err{background:#2a1a1e;border:1px solid #5a2c35;color:#ff9aa8;padding:10px 12px;border-radius:10px;margin:10px 0;white-space:pre-wrap}
pre{white-space:pre-wrap;word-break:break-word;font-size:12px;background:#0f0f15;border:1px solid var(--bd);border-radius:10px;padding:10px;margin:6px 0}
.cmd{display:flex;justify-content:space-between;padding:9px 0;border-top:1px solid var(--bd);gap:8px}.cmd:first-child{border:0}
code{background:#1e1e2a;padding:1px 6px;border-radius:6px}svg text{fill:#8b8ba0;font-size:10px}
@media(max-width:560px){nav .in{gap:10px}}
"""
BASE = """<!doctype html><html><head><meta charset=utf-8><meta name=viewport content="width=device-width,initial-scale=1">
<title>{% block title %}TBC-Lite{% endblock %}</title><style>""" + CSS + """</style></head><body>
{% if session.ok %}<nav><div class=in><b>⚡ TBC-Lite</b><a href="/" class="{{ 'on' if request.path=='/' }}">Home</a>
<a href="/bots" class="{{ 'on' if request.path.startswith('/bots') }}">Bots</a>
<form method=post action=/logout><input type=hidden name=csrf value="{{csrf}}"><button class="g s">Logout</button></form></div></nav>{% endif %}
<div class=wrap>{% for m in get_flashed_messages() %}<div class=flash>{{m}}</div>{% endfor %}{% block body %}{% endblock %}</div></body></html>"""

TEMPLATES = {
"base.html": BASE,
"login.html": """{% extends 'base.html' %}{% block body %}<div class=card style="max-width:360px;margin:12vh auto"><h1>⚡ TBC-Lite</h1>
{% if err %}<div class=err>{{err}}</div>{% endif %}<form method=post><p><input type=password name=password placeholder="Panel password" autofocus></p>
<button style="width:100%">Login</button></form></div>{% endblock %}""",
"dashboard.html": """{% extends 'base.html' %}{% block body %}<h1>Dashboard</h1>
<div class=grid><div class=stat><small>Total bots</small><b>{{total}}</b></div><div class=stat><small>Running</small><b style="color:var(--gr)">{{running}}</b></div>
<div class=stat><small>Total users</small><b>{{users}}</b></div><div class=stat><small>Active 24h</small><b>{{active}}</b></div>
<div class=stat><small>Commands run (since start)</small><b>{{cmds_run}}</b></div><div class=stat><small>Command errors</small><b style="color:{{ 'var(--rd)' if errs else 'inherit' }}">{{errs}}</b></div></div>
{% if errbots %}<div class=err>Bots with startup errors: {% for b in errbots %}<a href="/bots/{{b.id}}">#{{b.id}} {{b.name}}</a> ({{b.err}}) {% endfor %}</div>{% endif %}
<h2>Activity (updates / hour, last 24h)</h2><div class=card><svg viewBox="0 0 480 110" width=100%>
{% for v in series %}{% set h = (v / mx * 80) %}<rect x="{{ loop.index0 * 20 + 2 }}" y="{{ 90 - h }}" width=16 height="{{ h if h > 0.5 else 0.5 }}" rx=3 fill="#7c5cff"/>{% endfor %}
<text x=2 y=105>24h ago</text><text x=430 y=105>now</text><text x=2 y=10>peak {{mx if mx>1 else 0}}</text></svg></div>
<h2>Most users</h2><div class=card>{% for b in top %}<div class=bot><a class=grow href="/bots/{{b.id}}"><b>{{b.name}}</b> <span class=mu>@{{b.username}}</span></a><span class=pill>{{b.users}} users</span></div>{% else %}<span class=mu>No bots yet — add one in Bots.</span>{% endfor %}</div>{% endblock %}""",
"bots.html": """{% extends 'base.html' %}{% block body %}<h1>My Bots <span class=pill>{{all_bots|length}}</span></h1>
<form class=row method=get><input class=grow name=q value="{{qs}}" placeholder="Search name / @username / id"><select name=f style="width:auto"><option value="">All</option>
{% for s in ['running','stopped','error'] %}<option {{'selected' if flt==s}}>{{s}}</option>{% endfor %}</select><button class=g>Filter</button></form>
<div class=card>{% for b in bots %}<div class="bot {{b.state}}"><span class=dot></span><a class=grow href="/bots/{{b.id}}"><b>{{b.name}}</b><br><span class=mu>@{{b.username}} · #{{b.id}} · {{b.cmds}} cmds</span>
{% if b.err %}<br><span style="color:var(--rd);font-size:12px">{{b.err}}</span>{% endif %}</a><span class=pill>{{b.users}} users</span>
<form method=post action="/bots/{{b.id}}/action"><input type=hidden name=csrf value="{{csrf}}"><input type=hidden name=next value="/bots">
{% if b.state in ['running','starting'] %}<button class="g s" name=action value=stop>Stop</button>{% else %}<button class="s" name=action value=start>Start</button>{% endif %}</form></div>
{% else %}<span class=mu>No bots.</span>{% endfor %}</div>
<h2>Add bots</h2><form method=post action=/bots/add class=card><p class=mu style="margin-top:0">Paste one or many BotFather tokens (one per line).</p>
<textarea name=tokens rows=4 placeholder="123456:ABC-DEF...&#10;987654:XYZ..."></textarea>
<p><select name=copy_from><option value="">Start with no commands</option>{% for b in all_bots %}<option value="{{b.id}}">Copy commands from #{{b.id}} {{b.name}} ({{b.cmds}})</option>{% endfor %}</select></p>
<p><label><input type=checkbox name=start value=1 style="width:auto"> Start right after adding</label></p>
<input type=hidden name=csrf value="{{csrf}}"><button>Add</button></form>
<h2>Bulk import commands (ZIP)</h2><form method=post action=/bots/import-zip enctype=multipart/form-data class=card>
<p class=mu style="margin-top:0">A .zip with one file per bot. Each file name must contain the bot's <code>@username</code> (e.g. <code>My_bot.txt</code>). Matches bots already added above.</p>
<p><input type=file name=file accept=".zip"></p><p class=row><select name=mode style="width:auto"><option value=replace>Replace commands</option><option value=merge>Merge</option></select>
<input type=hidden name=csrf value="{{csrf}}"><button>Import ZIP</button></p></form>{% endblock %}""",
"bot.html": """{% extends 'base.html' %}{% block body %}<p><a href="/bots">← Bots</a></p>
<div class="row {{state}}"><span class=dot style="width:12px;height:12px"></span><h1 class=grow style="margin:0">{{b.name}}</h1><span class=pill>{{state}}</span></div>
<p class=mu><a href="https://t.me/{{b.username}}" target=_blank>@{{b.username}}</a> · id #{{b.id}} · {{users}} users ({{active}} active 24h) · {{st.commands}} cmds run · {{st.errors}} errors</p>
{% if err %}<div class=err>{{err}}</div>{% endif %}
<form method=post action="/bots/{{b.id}}/action" class=row><input type=hidden name=csrf value="{{csrf}}">
<button name=action value=start>Start</button><button class=g name=action value=restart>Restart</button><button class=g name=action value=stop>Stop</button>
<a class="btn g" href="/bots/{{b.id}}/logs">Logs</a><a class="btn g" href="/bots/{{b.id}}/data">Data</a><a class="btn g" href="/bots/{{b.id}}/export">Export</a></form>
<h2>Commands ({{ncmds}})</h2><div class=card><form class=row method=get><input class=grow name=q value="{{qs}}" placeholder="Search commands"><button class=g>Search</button>
<a class=btn href="/bots/{{b.id}}/cmd">+ New</a></form>
{% for n in names %}<div class=cmd><a href="/bots/{{b.id}}/cmd?name={{n|urlencode}}"><code>{{n}}</code></a><span class=mu>{{size(n)}} chars</span></div>{% endfor %}</div>
<h2>Import commands</h2><form method=post action="/bots/{{b.id}}/import" enctype=multipart/form-data class=card>
<p class=mu style="margin-top:0">Upload the commands .txt exported from TBC (blocks like <code>=== /start ===</code>) — or paste it.</p>
<p><input type=file name=file></p><p><textarea name=text rows=3 placeholder="…or paste here"></textarea></p>
<p class=row><select name=mode style="width:auto"><option value=replace>Replace all commands</option><option value=merge>Merge (overwrite same names)</option></select>
<input type=hidden name=csrf value="{{csrf}}"><button>Import</button></p></form>
<h2>Danger</h2><form method=post action="/bots/{{b.id}}/action" class="card row" onsubmit="return confirm('Delete this bot from the panel?')"><input type=hidden name=csrf value="{{csrf}}">
<label class=mu><input type=checkbox name=purge value=1 style="width:auto"> also delete its commands &amp; data</label><button class=r name=action value=delete>Delete bot</button></form>{% endblock %}""",
"cmd.html": """{% extends 'base.html' %}{% block body %}<p><a href="/bots/{{b.id}}">← {{b.name}}</a></p><h1>{{ 'New command' if isnew else name }}</h1>
{% if msg %}<div class=err>{{msg}}</div>{% endif %}<form method=post class=card><input type=hidden name=csrf value="{{csrf}}"><input type=hidden name=name value="{{name}}">
<p><input name=newname value="{{newname}}" placeholder="/command name (or button text)"></p><p><textarea name=code rows=26 spellcheck=false>{{code}}</textarea></p>
<p class=row><button>Save{% if not isnew %} (applies live){% endif %}</button>{% if not isnew %}<button class=r name=do value=delete onclick="return confirm('Delete command?')">Delete</button>{% endif %}</p></form>{% endblock %}""",
"logs.html": """{% extends 'base.html' %}{% block body %}<p><a href="/bots/{{b.id}}">← {{b.name}}</a></p><h1>Logs</h1>
{% if err %}<div class=err>{{err}}</div>{% endif %}<p class=mu>Newest first · <a href="">refresh</a></p>
{% for l in lines %}<pre>{{l}}</pre>{% else %}<span class=mu>No log lines yet.</span>{% endfor %}{% endblock %}""",
"data.html": """{% extends 'base.html' %}{% block body %}<p><a href="/bots/{{b.id}}">← {{b.name}}</a></p><h1>Data</h1>
<p class=mu>{{counts[0]}} bot keys · {{counts[1]}} user keys · {{counts[2]}} users</p>
<form class=row method=get><input class=grow name=q value="{{qs}}" placeholder="Search bot data keys"><button class=g>Search</button><a class=btn href="/bots/{{b.id}}/data/edit">+ New key</a></form>
<div class=card>{% for r in rows %}<div class=cmd><a href="/bots/{{b.id}}/data/edit?key={{r[0]|urlencode}}"><code>{{r[0]}}</code></a><span class=mu style="overflow:hidden;text-overflow:ellipsis;white-space:nowrap;max-width:50%">{{r[1]}}</span></div>{% else %}<span class=mu>No keys.</span>{% endfor %}</div>
<h2>Import data (JSON)</h2><form method=post action="/bots/{{b.id}}/data/import" enctype=multipart/form-data class=card>
<p class=mu style="margin-top:0">A JSON object <code>{"key": value}</code> — each key goes into Bot data (e.g. admins, settings).</p>
<p><input type=file name=file></p><p><textarea name=text rows=3></textarea></p><input type=hidden name=csrf value="{{csrf}}"><button>Import</button></form>{% endblock %}""",
"dataedit.html": """{% extends 'base.html' %}{% block body %}<p><a href="/bots/{{b.id}}/data">← Data</a></p><h1>{{ key or 'New key' }}</h1>
{% if msg %}<div class=err>{{msg}}</div>{% endif %}<form method=post class=card><input type=hidden name=csrf value="{{csrf}}"><input type=hidden name=key value="{{key}}">
<p><input name=newkey value="{{newkey}}" placeholder="key name"></p><p><textarea name=value rows=14 spellcheck=false>{{value}}</textarea></p>
<p class=row><button>Save</button>{% if key %}<button class=r name=do value=delete onclick="return confirm('Delete key?')">Delete</button>{% endif %}</p></form>{% endblock %}""",
}
app.jinja_loader = DictLoader(TEMPLATES)
app.jinja_env.filters["urlencode"] = lambda s: requests.utils.quote(str(s), safe="")

def autostart():
    rows = q("SELECT id,token FROM bots WHERE enabled=1 ORDER BY id")
    print("auto-starting %d bots..." % len(rows), flush=True)
    for r in rows:
        try: runner(r["id"]).start()
        except Exception: traceback.print_exc()
        time.sleep(0.15)

def main():
    if len(PASSWORD) < 8:
        sys.exit("Set PANEL_PASSWORD (min 8 characters) in .env first.")
    threading.Thread(target=autostart, daemon=True).start()
    print("Panel on http://%s:%d" % (HOST, PORT), flush=True)
    try:
        from waitress import serve
        serve(app, host=HOST, port=PORT, threads=16)
    except ImportError:
        app.run(host=HOST, port=PORT, threaded=True)

if __name__ == "__main__":
    main()
