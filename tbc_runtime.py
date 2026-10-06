#!/usr/bin/env python3
"""
Standalone runner for Telebot Creator (TPY) bots.
Emulates the TBC globals (Bot, bot, User, libs, HTTP, u, message, params, options ...)
and runs the commands from commands.json using Telegram long-polling.
"""
import os, sys, json, re, time, math, random, sqlite3, threading, traceback, hashlib, base64
import datetime, urllib.parse, queue, string
from concurrent.futures import ThreadPoolExecutor
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
import requests

HERE = os.path.dirname(os.path.abspath(__file__))

def load_env():
    p = os.path.join(HERE, ".env")
    if os.path.exists(p):
        for line in open(p, encoding="utf-8"):
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))
load_env()

BOT_TOKEN = os.environ.get("BOT_TOKEN", "").strip()
PUBLIC_URL = os.environ.get("PUBLIC_URL", "").rstrip("/")   # e.g. https://yourdomain.com
WEBHOOK_PORT = int(os.environ.get("WEBHOOK_PORT", "8080"))
DB_PATH = os.environ.get("DB_PATH", os.path.join(HERE, "bot_data.sqlite3"))
WORKERS = int(os.environ.get("WORKERS", "16"))
# Outbound calls containing any of these strings are blocked (see README: author's hard-coded reporting)
BLOCKED_OUTBOUND = [s for s in os.environ.get(
    "BLOCKED_OUTBOUND", "8327459100:,chat_id=6925391837").split(",") if s]
API = "https://api.telegram.org/bot%s/" % BOT_TOKEN

def log(*a):
    print(time.strftime("%Y-%m-%d %H:%M:%S"), *a, flush=True)

# ---------------------------------------------------------------- helpers
class Bunch(dict):
    """dict with attribute access; missing keys -> None"""
    def __getattr__(self, k):
        if k in self:
            return self[k]
        if k == "from_user" and "from" in self:
            return self["from"]
        return None
    def __setattr__(self, k, v):
        self[k] = v
    def __delattr__(self, k):
        self.pop(k, None)

def bunchify(x):
    if isinstance(x, Bunch):
        return x
    if isinstance(x, dict):
        return Bunch({k: bunchify(v) for k, v in x.items()})
    if isinstance(x, list):
        return [bunchify(i) for i in x]
    return x

class Options(str):
    """options passed to a command: behaves as str, .json parses JSON"""
    @property
    def json(self):
        try:
            v = json.loads(str(self))
            return bunchify(v) if isinstance(v, (dict, list)) else v
        except Exception:
            return None

def make_options(o):
    if o is None:
        return None
    if isinstance(o, Options):
        return o
    if isinstance(o, (dict, list)):
        return Options(json.dumps(o, ensure_ascii=False))
    return Options(str(o))

class ReturnCommand(Exception):
    pass

def jsondumps(o, **k):
    k.setdefault("ensure_ascii", False)
    return json.dumps(o, default=str, **k)

# ---------------------------------------------------------------- storage
_db = sqlite3.connect(DB_PATH, check_same_thread=False, isolation_level=None)
_db.execute("PRAGMA journal_mode=WAL")
_dblock = threading.RLock()
for stmt in [
    "CREATE TABLE IF NOT EXISTS bot_data(name TEXT PRIMARY KEY, value TEXT)",
    "CREATE TABLE IF NOT EXISTS user_data(user TEXT, name TEXT, value TEXT, PRIMARY KEY(user,name))",
    "CREATE TABLE IF NOT EXISTS res(scope TEXT, user TEXT, name TEXT, value REAL, PRIMARY KEY(scope,user,name))",
    "CREATE TABLE IF NOT EXISTS waits(user TEXT PRIMARY KEY, command TEXT, options TEXT)",
    "CREATE TABLE IF NOT EXISTS users(user TEXT PRIMARY KEY, first_seen REAL, last_seen REAL)",
    "CREATE TABLE IF NOT EXISTS jobs(id TEXT PRIMARY KEY, run_at REAL, command TEXT, options TEXT, user TEXT, ctx TEXT)",
    "CREATE TABLE IF NOT EXISTS meta(k TEXT PRIMARY KEY, v TEXT)",
]:
    _db.execute(stmt)

def _enc(v): return json.dumps(v, ensure_ascii=False, default=str)
def _dec(s):
    try: return json.loads(s)
    except Exception: return s

def db_get(table_sql, args):
    with _dblock:
        r = _db.execute(table_sql, args).fetchone()
    return None if r is None else _dec(r[0])

class _BotData:
    def getData(self, name=None):
        return db_get("SELECT value FROM bot_data WHERE name=?", (str(name),))
    def saveData(self, name, data):
        with _dblock:
            _db.execute("INSERT OR REPLACE INTO bot_data VALUES(?,?)", (str(name), _enc(data)))
        return data
    setData = saveData
    def deleteData(self, name=None):
        with _dblock:
            _db.execute("DELETE FROM bot_data WHERE name=?", (str(name),))

# ---------------------------------------------------------------- resources
class _Res:
    def __init__(self, scope, name, user=""):
        self.scope, self.name, self.user = scope, str(name), str(user or "")
    def value(self):
        with _dblock:
            r = _db.execute("SELECT value FROM res WHERE scope=? AND user=? AND name=?",
                            (self.scope, self.user, self.name)).fetchone()
        v = r[0] if r else 0
        return int(v) if float(v).is_integer() else v
    def _set(self, v):
        with _dblock:
            _db.execute("INSERT OR REPLACE INTO res VALUES(?,?,?,?)", (self.scope, self.user, self.name, float(v)))
        return self.value()
    def add(self, n):
        with _dblock: return self._set(float(self.value()) + float(n))
    def cut(self, n):
        with _dblock: return self._set(float(self.value()) - float(n))
    def set(self, n): return self._set(n)
    def reset(self): return self._set(0)
    def getAllData(self, *a, **k):
        with _dblock:
            rows = _db.execute("SELECT user,value FROM res WHERE scope=? AND name=?", (self.scope, self.name)).fetchall()
        return {u: v for u, v in rows}
    fetchAllResources = getAllData

class _Resources:
    def __init__(self): self._u = ""
    def userRes(self, name, user=None, **k): return _Res("user", name, user if user is not None else cur_user())
    def anotherRes(self, name, user=None, **k): return _Res("user", name, user)
    def globalRes(self, name, **k): return _Res("global", name)
    def accountRes(self, name, **k): return _Res("account", name)
    def adminRes(self, name, **k): return _Res("admin", name)

CURRENT_USER = threading.local()
def cur_user(): return getattr(CURRENT_USER, "u", "")

# ---------------------------------------------------------------- Telegram API
SESSION = requests.Session()
class TelegramError(Exception):
    pass

def tg(method, **params):
    data = {}
    files = None
    for k, v in params.items():
        if v is None: continue
        if hasattr(v, "to_dict"): v = v.to_dict()
        if isinstance(v, (dict, list)):
            v = json.dumps(v, ensure_ascii=False)
        elif isinstance(v, bool):
            v = "true" if v else "false"
        data[k] = v
    if "parse_mode" in data and isinstance(data["parse_mode"], str):
        pm = data["parse_mode"].lower()
        data["parse_mode"] = {"html": "HTML", "markdown": "Markdown", "markdownv2": "MarkdownV2"}.get(pm, data["parse_mode"])
    for attempt in range(3):
        try:
            r = SESSION.post(API + method, data=data, timeout=70)
            j = r.json()
        except Exception as e:
            if attempt == 2: raise TelegramError(str(e))
            time.sleep(1); continue
        if j.get("ok"):
            return bunchify(j["result"])
        if j.get("error_code") == 429:
            time.sleep(min(j.get("parameters", {}).get("retry_after", 2), 30)); continue
        raise TelegramError("%s: %s" % (method, j.get("description")))
    raise TelegramError("%s failed" % method)

# ---- keyboard helper classes (telebot-style)
class InlineKeyboardButton:
    def __init__(self, text, url=None, callback_data=None, web_app=None, switch_inline_query=None,
                 switch_inline_query_current_chat=None, **kw):
        self.d = {"text": text}
        if url: self.d["url"] = url
        if callback_data is not None: self.d["callback_data"] = str(callback_data)
        if web_app: self.d["web_app"] = web_app if isinstance(web_app, dict) else {"url": web_app}
        if switch_inline_query is not None: self.d["switch_inline_query"] = switch_inline_query
        if switch_inline_query_current_chat is not None: self.d["switch_inline_query_current_chat"] = switch_inline_query_current_chat
        self.d.update({k: v for k, v in kw.items() if v is not None})
    def to_dict(self): return self.d

class InlineKeyboardMarkup:
    def __init__(self, row_width=3, **k):
        self.rows, self.row_width = [], row_width
    def add(self, *btns, row_width=None):
        w = row_width or self.row_width
        for i in range(0, len(btns), w):
            self.rows.append(list(btns[i:i + w]))
        return self
    def row(self, *btns):
        self.rows.append(list(btns)); return self
    def to_dict(self):
        return {"inline_keyboard": [[b.to_dict() if hasattr(b, "to_dict") else b for b in r] for r in self.rows]}

class KeyboardButton:
    def __init__(self, text, request_contact=None, request_location=None, web_app=None, **k):
        self.d = {"text": text}
        if request_contact: self.d["request_contact"] = True
        if request_location: self.d["request_location"] = True
        if web_app: self.d["web_app"] = web_app if isinstance(web_app, dict) else {"url": web_app}
    def to_dict(self): return self.d

class ReplyKeyboardMarkup:
    def __init__(self, resize_keyboard=True, one_time_keyboard=False, row_width=3, selective=None, **k):
        self.rows, self.resize, self.one, self.row_width = [], bool(resize_keyboard), one_time_keyboard, row_width
    def add(self, *btns, row_width=None):
        w = row_width or self.row_width
        for i in range(0, len(btns), w): self.rows.append(list(btns[i:i + w]))
        return self
    def row(self, *btns):
        self.rows.append(list(btns)); return self
    def to_dict(self):
        conv = lambda b: b.to_dict() if hasattr(b, "to_dict") else ({"text": b} if isinstance(b, str) else b)
        return {"keyboard": [[conv(b) for b in r] for r in self.rows],
                "resize_keyboard": self.resize, "one_time_keyboard": bool(self.one)}

class ReplyKeyboardRemove:
    def to_dict(self): return {"remove_keyboard": True}

# ---------------------------------------------------------------- bot (low level)
class _LowBot:
    """bot.<anyTelegramMethod>(...) -> Telegram Bot API call"""
    # positional-arg order for methods used positionally in TPY
    POS = {
        "sendMessage": ["text"], "sendPhoto": ["photo"], "sendVideo": ["video"], "sendDocument": ["document"],
        "sendAudio": ["audio"], "sendAnimation": ["animation"], "sendSticker": ["sticker"], "sendVoice": ["voice"],
        "replyText": ["chat_id", "text"], "replyPhoto": ["chat_id", "photo"],
        "editMessageText": ["text"], "editMessageCaption": ["caption"], "editMessageReplyMarkup": [],
        "answerCallbackQuery": ["callback_query_id", "text", "show_alert"],
        "getChatMember": ["chat_id", "user_id"], "getChat": ["chat_id"], "getChatMemberCount": ["chat_id"],
        "getChatMembersCount": ["chat_id"], "deleteMessage": ["chat_id", "message_id"],
        "copyMessage": ["chat_id", "from_chat_id", "message_id"],
        "forwardMessage": ["chat_id", "from_chat_id", "message_id"],
        "pinChatMessage": ["chat_id", "message_id"], "unpinChatMessage": ["chat_id", "message_id"],
        "banChatMember": ["chat_id", "user_id"], "unbanChatMember": ["chat_id", "user_id"],
        "approveChatJoinRequest": ["chat_id", "user_id"], "declineChatJoinRequest": ["chat_id", "user_id"],
        "createChatInviteLink": ["chat_id"], "exportChatInviteLink": ["chat_id"],
        "sendChatAction": ["action"], "getFile": ["file_id"], "sendContact": ["phone_number", "first_name"],
        "sendLocation": ["latitude", "longitude"], "sendPoll": ["question", "options"],
        "setMessageReaction": ["chat_id", "message_id", "reaction"], "leaveChat": ["chat_id"],
    }
    NEEDS_CHAT = {"sendMessage", "sendPhoto", "sendVideo", "sendDocument", "sendAudio", "sendAnimation",
                  "sendSticker", "sendVoice", "sendChatAction", "sendContact", "sendLocation", "sendPoll",
                  "sendDice", "sendMediaGroup", "sendVideoNote"}
    def __init__(self, info): self._info = info
    def info(self, *a, **k): return self._info
    def replyTo(self, message, text, **kw):
        return tg("sendMessage", chat_id=message.chat.id, text=text, reply_to_message_id=message.message_id, **kw)
    def __getattr__(self, name):
        if name.startswith("_"): raise AttributeError(name)
        method = _camel(name)
        def call(*args, **kw):
            order = self.POS.get(method, [])
            for i, a in enumerate(args):
                if i < len(order): kw[order[i]] = a
                else: raise TypeError("%s: too many positional args" % method)
            if method == "replyText":
                method_ = "sendMessage"
            elif method == "replyPhoto":
                method_ = "sendPhoto"
            else:
                method_ = method
            if method_ in self.NEEDS_CHAT and "chat_id" not in kw:
                kw["chat_id"] = cur_user()
            if method_ == "answerCallbackQuery" and "callback_query_id" not in kw:
                kw["callback_query_id"] = cur_cb()
            if method_ in ("sendMessage",) and "text" in kw and "link_preview_options" not in kw:
                pass
            return tg(method_, **kw)
        return call

CURRENT_CB = threading.local()
def cur_cb(): return getattr(CURRENT_CB, "id", None)

def _camel(n):
    if "_" in n and n.lower() == n:
        parts = n.split("_")
        n = parts[0] + "".join(p.capitalize() for p in parts[1:])
    # ensure official camelCase for common snake variants
    return n

# ---------------------------------------------------------------- HTTP lib
class _Resp:
    def __init__(self, r): self._r = r
    def json(self): return bunchify(self._r.json()) if False else self._r.json()
    @property
    def text(self): return self._r.text
    @property
    def content(self): return self._r.content
    @property
    def status_code(self): return self._r.status_code
    def __getattr__(self, k): return getattr(self._r, k)

class _HTTP:
    def _check(self, url, *rest):
        blob = str(url) + " " + str(rest)
        for b in BLOCKED_OUTBOUND:
            if b in blob:
                log("BLOCKED outbound request (matches %r): %s" % (b, str(url)[:120]))
                raise Exception("outbound request blocked")
    def _do(self, m, url, **k):
        self._check(url, k.get("params"), k.get("data"), k.get("json"))
        k.setdefault("timeout", 30)
        return _Resp(requests.request(m, url, **k))
    def get(self, url, **k): return self._do("GET", url, **k)
    def post(self, url, **k): return self._do("POST", url, **k)
    def put(self, url, **k): return self._do("PUT", url, **k)
    def delete(self, url, **k): return self._do("DELETE", url, **k)

# ---------------------------------------------------------------- libs
class _DateAndTime:
    """TBC returns a dict: {"date": "YYYY-MM-DD", "time": "HH:MM:SS", ...}"""
    def now(self, tz=None):
        try:
            from zoneinfo import ZoneInfo
            d = datetime.datetime.now(ZoneInfo(tz)) if tz else datetime.datetime.now()
        except Exception:
            d = datetime.datetime.now()
        return Bunch({"date": d.strftime("%Y-%m-%d"), "time": d.strftime("%H:%M:%S"),
                      "datetime": d.strftime("%Y-%m-%d %H:%M:%S"), "timestamp": d.timestamp(),
                      "year": d.year, "month": d.month, "day": d.day, "hour": d.hour,
                      "minute": d.minute, "second": d.second, "weekday": d.strftime("%A"), "tz": tz})
    def today(self, tz=None): return self.now(tz)["date"]

class _Random:
    def randomInt(self, a, b): return random.randint(int(a), int(b))
    def randomFloat(self, a, b): return random.uniform(a, b)
    def randomStr(self, n, char_set=None): return "".join(random.choice(char_set or string.ascii_letters + string.digits) for _ in range(int(n)))
    def randomAscii(self, n): return "".join(random.choice(string.ascii_letters) for _ in range(int(n)))
    def randomChoice(self, seq): return random.choice(seq)
    def randomWeightedChoice(self, items, weights): return random.choices(items, weights=weights, k=1)[0]

class _TbcAds:
    """TBC ad network does not exist outside TBC -> always 'no ad available'"""
    def reward_ad(self, *a, **k): return False
    def claim(self, *a, **k): return True
    def __getattr__(self, n): return lambda *a, **k: False

class _Webhook:
    def getUrlFor(self, command, user_id=None, **k):
        base = PUBLIC_URL or ("http://127.0.0.1:%d" % WEBHOOK_PORT)
        q = urllib.parse.quote(str(command), safe="")
        return "%s/wh/%s/%s/%s" % (base, WEBHOOK_SECRET, q, user_id if user_id is not None else "0")

class _Libs:
    Resources = _Resources()
    DateAndTime = _DateAndTime()
    Random = _Random()
    tbcads = _TbcAds()
    Webhook = _Webhook()

WEBHOOK_SECRET = hashlib.sha256(("wh" + BOT_TOKEN).encode()).hexdigest()[:24]

# ---------------------------------------------------------------- command engine
COMMANDS = json.load(open(os.path.join(HERE, "commands.json"), encoding="utf-8"))
_compiled = {}
BOT_INFO = Bunch()
_pool = ThreadPoolExecutor(max_workers=WORKERS)
_user_locks = {}
_user_locks_guard = threading.Lock()
def user_lock(uid):
    with _user_locks_guard:
        return _user_locks.setdefault(str(uid), threading.RLock())

def get_code(name):
    if name not in COMMANDS: return None
    if name not in _compiled:
        _compiled[name] = compile(COMMANDS[name], "<tpy %s>" % name, "exec")
    return _compiled[name]

class Ctx:
    def __init__(self, u, message, update_type="message", msg=None, params=None, options=None, cb_id=None):
        self.u, self.message, self.update_type = u, message, update_type
        self.msg, self.params, self.options, self.cb_id = msg, params, options, cb_id

_SAFE_MODULES = {}
def run_command(name, ctx, depth=0):
    code = get_code(name)
    if code is None:
        log("command not found:", name); return False
    if depth > 25:
        log("runCommand depth exceeded at", name); return False
    CURRENT_USER.u = ctx.u
    CURRENT_CB.id = ctx.cb_id
    g = build_globals(ctx, depth)
    try:
        exec(code, g)
    except ReturnCommand:
        pass
    except Exception:
        log("ERROR in command %s (user %s):\n%s" % (name, ctx.u, traceback.format_exc(limit=6)))
    return True

class _BotHigh(_BotData):
    def __init__(self, ctx, depth): self.ctx, self.depth = ctx, depth
    def info(self, *a, **k): return BOT_INFO
    def log(self, *a, **k): log("Bot.log:", *a)
    def genId(self): return int(time.time() * 1000) * 1000 + random.randint(0, 999)
    def genRandomId(self): return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
    def runCommand(self, command, options=None, **k):
        c = Ctx(self.ctx.u, self.ctx.message, self.ctx.update_type, self.ctx.msg, None, make_options(options), self.ctx.cb_id)
        run_command(command, c, self.depth + 1)
        CURRENT_USER.u = self.ctx.u
    def handleNextCommand(self, command, options=None, cancel_at_command=None):
        with _dblock:
            _db.execute("INSERT OR REPLACE INTO waits VALUES(?,?,?)",
                        (str(self.ctx.u), command, None if options is None else _enc(options if not isinstance(options, Options) else str(options))))
    def runCommandAfter(self, timeout, command, options=None, id=None):
        if isinstance(timeout, datetime.datetime):
            secs = max(1, (timeout - datetime.datetime.now(timeout.tzinfo)).total_seconds())
        else:
            secs = max(1, float(timeout))
        jid = id or self.genRandomId()
        m = self.ctx.message
        ctxd = {"message": m, "update_type": self.ctx.update_type, "msg": self.ctx.msg}
        with _dblock:
            _db.execute("INSERT OR REPLACE INTO jobs VALUES(?,?,?,?,?,?)",
                        (str(jid), time.time() + secs, command,
                         None if options is None else _enc(str(options) if isinstance(options, Options) else options),
                         str(self.ctx.u), json.dumps(ctxd, default=str)))
        return {"id": str(jid), "command": command, "timeout": secs}
    def cancelScheduledTask(self, jid):
        with _dblock: _db.execute("DELETE FROM jobs WHERE id=?", (str(jid),))
    def replyText(self, text, **kw): return tg("sendMessage", chat_id=self.ctx.u, text=text, **kw)
    def sendMessage(self, text, **kw): return tg("sendMessage", chat_id=self.ctx.u, text=text, **kw)
    def broadcast(self, function=None, callback_url=None, command=None, code=None, **kwargs):
        func = _camel(function or "send_message")
        with _dblock:
            users = [r[0] for r in _db.execute("SELECT user FROM users").fetchall()]
        bid = self.genRandomId()
        threading.Thread(target=_do_broadcast, args=(bid, func, users, kwargs, callback_url), daemon=True).start()
        return {"status": "success", "broadcast_id": bid, "total": len(users)}
    def getBroadcastStatus(self, bid): return {"status": "unknown"}
    def stopBroadcast(self, bid): return {"status": "unsupported"}
    def clearBroadcast(self, *a, **k): return {"status": "success"}

def _do_broadcast(bid, func, users, kwargs, callback_url):
    ok = err = 0
    for uid in users:
        try:
            kw = dict(kwargs); kw["chat_id"] = uid
            tg(func, **kw); ok += 1
        except Exception:
            err += 1
        time.sleep(0.05)   # ~20 msgs/sec, under Telegram's 30/sec limit
    log("broadcast %s done ok=%d err=%d" % (bid, ok, err))
    if callback_url:
        try:
            requests.post(callback_url, json={"broadcast_id": bid, "total": len(users),
                          "total_success": ok, "total_errors": err}, timeout=20)
        except Exception as e:
            log("broadcast callback failed:", e)

class _User:
    def __init__(self, ctx): self.ctx = ctx
    def _uid(self, user): return str(user if user is not None else self.ctx.u)
    def getData(self, name, user=None):
        return db_get("SELECT value FROM user_data WHERE user=? AND name=?", (self._uid(user), str(name)))
    def saveData(self, name, data, user=None):
        with _dblock:
            _db.execute("INSERT OR REPLACE INTO user_data VALUES(?,?,?)", (self._uid(user), str(name), _enc(data)))
        return data
    def deleteData(self, name, user=None):
        with _dblock:
            _db.execute("DELETE FROM user_data WHERE user=? AND name=?", (self._uid(user), str(name)))

class _Time:
    def __getattr__(self, n): return getattr(time, n)

def isNumeric(x):
    try: float(str(x)); return True
    except Exception: return False

def MembershipCheck(chat_id, user_id=None):
    try:
        st = tg("getChatMember", chat_id=chat_id, user_id=user_id or cur_user()).status
        return st in ("member", "administrator", "creator", "restricted")
    except Exception: return False

def build_globals(ctx, depth):
    import builtins
    g = {"__builtins__": builtins, "__name__": "tpy"}
    bot = _LowBot(BOT_INFO)
    Bot = _BotHigh(ctx, depth)
    g.update(
        u=ctx.u, message=ctx.message, msg=ctx.msg, params=ctx.params, options=ctx.options,
        update_type=ctx.update_type, bot=bot, Bot=Bot, User=_User(ctx), libs=_Libs, HTTP=_HTTP(),
        bot_token=BOT_TOKEN, bot_id=BOT_INFO.get("bot_id"), left_points=10**9,
        ReturnCommand=ReturnCommand, returnCommand=ReturnCommand, returncommand=ReturnCommand,
        handleNextCommand=Bot.handleNextCommand, runCommand=Bot.runCommand, runCommandAfter=Bot.runCommandAfter,
        InlineKeyboardButton=InlineKeyboardButton, InlineKeyboardMarkup=InlineKeyboardMarkup,
        ReplyKeyboardMarkup=ReplyKeyboardMarkup, KeyboardButton=KeyboardButton, ReplyKeyboardRemove=ReplyKeyboardRemove,
        bunchify=bunchify, jsondumps=jsondumps, encodejson=jsondumps, bf_json=lambda x: json.loads(x) if isinstance(x, (str, bytes)) else json.dumps(x),
        isNumeric=isNumeric, MembershipCheck=MembershipCheck,
        rawurlencode=lambda s: urllib.parse.quote(str(s), safe=""),
        encodeURIComponent=lambda s: urllib.parse.quote(str(s), safe="~()*!.'"),
        decodeURIComponent=lambda s: urllib.parse.unquote(str(s)),
        parse_qs=urllib.parse.parse_qs, md5=lambda s: hashlib.md5(str(s).encode()).hexdigest(),
        hashlib=hashlib, base64=base64, re=re, regex=re, time=time, json=json, math=math, random=random,
        datetime=datetime, binascii=__import__("binascii"),
    )
    g["call"] = ctx.message if ctx.update_type == "callback_query" else None
    return g

def _norm_cmd_token(tok):
    # "/start@MyBot" -> "/start"
    if tok.startswith("/") and "@" in tok:
        tok = tok.split("@", 1)[0]
    return tok

def _touch_user(uid):
    now = time.time()
    with _dblock:
        r = _db.execute("SELECT 1 FROM users WHERE user=?", (str(uid),)).fetchone()
        if r: _db.execute("UPDATE users SET last_seen=? WHERE user=?", (now, str(uid)))
        else: _db.execute("INSERT INTO users VALUES(?,?,?)", (str(uid), now, now))

def _pop_wait(uid):
    with _dblock:
        r = _db.execute("SELECT command, options FROM waits WHERE user=?", (str(uid),)).fetchone()
        if r: _db.execute("DELETE FROM waits WHERE user=?", (str(uid),))
    if not r: return None
    return r[0], (None if r[1] is None else _dec(r[1]))

def _run_at_handler(ctx):
    """'@' runs before every command. Returns False if it stopped (raised ReturnCommand) the flow."""
    if "@" not in COMMANDS: return True
    code = get_code("@")
    CURRENT_USER.u = ctx.u; CURRENT_CB.id = ctx.cb_id
    g = build_globals(ctx, 0)
    try:
        exec(code, g)
    except ReturnCommand:
        return False
    except Exception:
        log("ERROR in '@' (user %s):\n%s" % (ctx.u, traceback.format_exc(limit=6)))
    return True

def handle_update(upd):
    try:
        _handle_update(upd)
    except Exception:
        log("update handler crashed:\n" + traceback.format_exc())

def _handle_update(upd):
    if "message" in upd:
        m = bunchify(upd["message"]); utype = "message"
    elif "callback_query" in upd:
        cq = bunchify(upd["callback_query"]); utype = "callback_query"
        orig = cq.message or Bunch()
        m = Bunch(orig)
        m["id"] = cq["id"]; m["data"] = cq.data; m["from"] = cq["from"]
        m["message"] = orig; m["callback_query_id"] = cq["id"]
        if "chat" not in m: m["chat"] = Bunch({"id": cq["from"]["id"], "type": "private"})
    else:
        utype = next((k for k in upd if k != "update_id"), None)
        if utype is None: return
        m = bunchify(upd[utype])
    m["update_type"] = utype
    frm = m.get("from") or (m.chat.get("id") if m.chat else None)
    uid = (m["from"]["id"] if m.get("from") else (m.chat.id if m.chat else None))
    if uid is None: return
    if m.get("chat") is None or not m.get("chat"):
        m["chat"] = Bunch({"id": uid, "type": "private"})
    with user_lock(uid):
        CURRENT_USER.u = uid
        if utype in ("message", "callback_query") and (m.chat.type == "private"):
            _touch_user(uid)
        cb_id = m["id"] if utype == "callback_query" else None
        text = m.text if utype == "message" else m.data
        text = text if isinstance(text, str) else None
        ctx = Ctx(uid, m, utype, msg=text, cb_id=cb_id)

        # special updates
        if utype not in ("message", "callback_query"):
            _run_at_handler(ctx)
            for name in ("/handler_" + utype, "/handler_special_updates"):
                if name in COMMANDS:
                    run_command(name, ctx); break
            return

        if not _run_at_handler(ctx):
            return

        command, params, options = None, None, None
        if utype == "message":
            wait = None
            is_known_cmd = bool(text) and text.startswith("/") and _norm_cmd_token(text.split()[0]) in COMMANDS
            if not is_known_cmd:
                wait = _pop_wait(uid)
            else:
                with _dblock: _db.execute("DELETE FROM waits WHERE user=?", (str(uid),))
            if wait:
                command, options = wait[0], make_options(wait[1])
                params = None
            elif text:
                tok = _norm_cmd_token(text.split()[0])
                if tok.startswith("/") and tok in COMMANDS:
                    command = tok
                    rest = text.split(None, 1)
                    params = rest[1] if len(rest) > 1 else None
                elif text in COMMANDS:
                    command = text
                elif "*" in COMMANDS:
                    command = "*"
            else:
                # non-text (photo, contact, new members...): joined event or wildcard
                if m.get("new_chat_members") and "/joined" in COMMANDS: command = "/joined"
                elif "*" in COMMANDS: command = "*"
        else:  # callback_query
            parts = (text or "").split(None, 1)
            tok = parts[0] if parts else ""
            if tok in COMMANDS:
                command = tok; params = parts[1] if len(parts) > 1 else None
            elif text in COMMANDS:
                command = text
            elif "*" in COMMANDS:
                command = "*"
        if command:
            ctx.params, ctx.options = params, options
            run_command(command, ctx)

# ---------------------------------------------------------------- scheduler
def scheduler_loop():
    while True:
        try:
            with _dblock:
                rows = _db.execute("SELECT id,command,options,user,ctx FROM jobs WHERE run_at<=?", (time.time(),)).fetchall()
                for r in rows: _db.execute("DELETE FROM jobs WHERE id=?", (r[0],))
            for jid, cmd, opts, uid, ctxj in rows:
                _pool.submit(_run_job, cmd, opts, uid, ctxj)
        except Exception:
            log("scheduler error:\n" + traceback.format_exc())
        time.sleep(1)

def _run_job(cmd, opts, uid, ctxj):
    try:
        c = json.loads(ctxj)
        m = bunchify(c["message"])
        ctx = Ctx(int(uid) if str(uid).lstrip("-").isdigit() else uid, m, c.get("update_type", "message"),
                  c.get("msg"), None, make_options(_dec(opts) if opts is not None else None))
        with user_lock(uid):
            run_command(cmd, ctx)
    except Exception:
        log("job failed:\n" + traceback.format_exc())

# ---------------------------------------------------------------- webhook server
class WebhookHandler(BaseHTTPRequestHandler):
    def log_message(self, *a): pass
    def _go(self):
        try:
            u = urllib.parse.urlparse(self.path)
            parts = [urllib.parse.unquote(p) for p in u.path.strip("/").split("/")]
            if len(parts) < 4 or parts[0] != "wh" or parts[1] != WEBHOOK_SECRET:
                self.send_response(404); self.end_headers(); return
            command, uid = parts[2], parts[3]
            n = int(self.headers.get("Content-Length") or 0)
            raw = self.rfile.read(n).decode("utf-8", "replace") if n else ""
            payload = None
            if raw:
                try: payload = json.loads(raw)
                except Exception:
                    payload = {k: v[0] if len(v) == 1 else v for k, v in urllib.parse.parse_qs(raw).items()}
            if payload is None:
                q = {k: v[0] if len(v) == 1 else v for k, v in urllib.parse.parse_qs(u.query).items()}
                payload = q or None
            uid_i = int(uid) if uid.lstrip("-").isdigit() else uid
            m = Bunch({"chat": Bunch({"id": uid_i, "type": "private"}), "from": Bunch({"id": uid_i, "first_name": "User"}),
                       "update_type": "webhook"})
            ctx = Ctx(uid_i, m, "webhook", None, None, make_options(payload))
            _pool.submit(lambda: (user_lock(uid_i).acquire(), run_command(command, ctx), user_lock(uid_i).release()))
            body = b'{"ok":true}'
            self.send_response(200); self.send_header("Content-Type", "application/json")
            self.send_header("Content-Length", str(len(body))); self.end_headers(); self.wfile.write(body)
        except Exception:
            log("webhook error:\n" + traceback.format_exc())
            self.send_response(500); self.end_headers()
    do_GET = do_POST = _go

# ---------------------------------------------------------------- main loop
def main():
    if not BOT_TOKEN:
        sys.exit("Set BOT_TOKEN in .env (see README.md)")
    me = tg("getMe")
    BOT_INFO.update({"token": BOT_TOKEN, "bot_id": me.id, "bot_username": me.username, "bot_name": me.first_name,
                     "username": me.username, "id": me.id, "first_name": me.first_name, "status": "working"})
    log("Started as @%s (id %s), %d commands loaded" % (me.username, me.id, len(COMMANDS)))
    try: tg("deleteWebhook", drop_pending_updates=False)
    except Exception: pass
    threading.Thread(target=scheduler_loop, daemon=True).start()
    srv = ThreadingHTTPServer(("0.0.0.0", WEBHOOK_PORT), WebhookHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    log("webhook server on port %d (PUBLIC_URL=%s)" % (WEBHOOK_PORT, PUBLIC_URL or "not set"))
    with _dblock:
        r = _db.execute("SELECT v FROM meta WHERE k='offset'").fetchone()
    offset = int(r[0]) if r else 0
    allowed = ["message", "callback_query", "my_chat_member", "chat_member", "chat_join_request",
               "edited_message", "channel_post", "inline_query", "pre_checkout_query", "message_reaction"]
    while True:
        try:
            r = SESSION.post(API + "getUpdates", data={"offset": offset, "timeout": 50,
                             "allowed_updates": json.dumps(allowed)}, timeout=65).json()
            if not r.get("ok"):
                log("getUpdates error:", r); time.sleep(3); continue
            for upd in r["result"]:
                offset = upd["update_id"] + 1
                _pool.submit(handle_update, upd)
            if r["result"]:
                with _dblock: _db.execute("INSERT OR REPLACE INTO meta VALUES('offset',?)", (str(offset),))
        except KeyboardInterrupt:
            break
        except Exception as e:
            log("poll error:", e); time.sleep(3)

if __name__ == "__main__":
    main()
