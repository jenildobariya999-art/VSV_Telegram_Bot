import os
import json
import re
import html
import time
import sqlite3
import traceback
import threading
import urllib.parse
import urllib.request
from datetime import datetime, timedelta
from zoneinfo import ZoneInfo
from types import SimpleNamespace

from telebot import types
from telebot.types import (
    InlineKeyboardMarkup, InlineKeyboardButton,
    ReplyKeyboardMarkup, KeyboardButton,
    LinkPreviewOptions
)

DB_PATH = os.environ.get("TBC_DB_PATH", "tbc_data.sqlite3")


class ReturnCommand(Exception):
    pass


class _DB:
    def __init__(self, path=DB_PATH):
        self.path = path
        self.lock = threading.RLock()
        with self.lock, sqlite3.connect(self.path) as c:
            c.execute("""CREATE TABLE IF NOT EXISTS kv(
                scope TEXT NOT NULL, owner TEXT NOT NULL, key TEXT NOT NULL,
                value TEXT, PRIMARY KEY(scope, owner, key)
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS resources(
                name TEXT NOT NULL, owner TEXT NOT NULL, value REAL NOT NULL,
                PRIMARY KEY(name, owner)
            )""")
            c.execute("""CREATE TABLE IF NOT EXISTS users(
                user_id TEXT PRIMARY KEY
            )""")

    def get(self, scope, owner, key):
        with self.lock, sqlite3.connect(self.path) as c:
            row = c.execute(
                "SELECT value FROM kv WHERE scope=? AND owner=? AND key=?",
                (scope, str(owner), key)
            ).fetchone()
        if not row:
            return None
        try:
            return json.loads(row[0])
        except Exception:
            return row[0]

    def set(self, scope, owner, key, value):
        raw = json.dumps(value, ensure_ascii=False, default=str)
        with self.lock, sqlite3.connect(self.path) as c:
            c.execute("""INSERT INTO kv(scope,owner,key,value)
                         VALUES(?,?,?,?)
                         ON CONFLICT(scope,owner,key)
                         DO UPDATE SET value=excluded.value""",
                      (scope, str(owner), key, raw))

    def delete(self, scope, owner, key):
        with self.lock, sqlite3.connect(self.path) as c:
            c.execute("DELETE FROM kv WHERE scope=? AND owner=? AND key=?",
                      (scope, str(owner), key))

    def resource(self, name, owner):
        with self.lock, sqlite3.connect(self.path) as c:
            row = c.execute(
                "SELECT value FROM resources WHERE name=? AND owner=?",
                (name, str(owner))
            ).fetchone()
        return float(row[0]) if row else 0.0

    def set_resource(self, name, owner, value):
        with self.lock, sqlite3.connect(self.path) as c:
            c.execute("""INSERT INTO resources(name,owner,value)
                         VALUES(?,?,?)
                         ON CONFLICT(name,owner)
                         DO UPDATE SET value=excluded.value""",
                      (name, str(owner), float(value)))

    def add_resource(self, name, owner, amount):
        v = self.resource(name, owner) + float(amount)
        self.set_resource(name, owner, v)
        return v

    def cut_resource(self, name, owner, amount):
        v = self.resource(name, owner) - float(amount)
        self.set_resource(name, owner, v)
        return v


class Resource:
    def __init__(self, db, name, owner):
        self.db, self.name, self.owner = db, name, owner

    def value(self):
        return self.db.resource(self.name, self.owner)

    def add(self, amount):
        return self.db.add_resource(self.name, self.owner, amount)

    def cut(self, amount):
        return self.db.cut_resource(self.name, self.owner, amount)

    def set(self, amount):
        self.db.set_resource(self.name, self.owner, amount)
        return amount


class Resources:
    def __init__(self, db):
        self.db = db

    def anotherRes(self, name, user=None):
        return Resource(self.db, name, user)

    def globalRes(self, name):
        return Resource(self.db, name, "__GLOBAL__")


class UserStore:
    def __init__(self, db, uid):
        self.db, self.uid = db, str(uid)

    def getData(self, key):
        return self.db.get("user", self.uid, key)

    def saveData(self, key, value):
        self.db.set("user", self.uid, key, value)

    def deleteData(self, key):
        self.db.delete("user", self.uid, key)


class BotStore:
    def __init__(self, env):
        self.env = env
        self.db = env.db

    def getData(self, key):
        return self.db.get("bot", "0", key)

    def saveData(self, key, value):
        self.db.set("bot", "0", key, value)

    def deleteData(self, key):
        self.db.delete("bot", "0", key)

    def runCommand(self, command, options=None):
        return self.env.run_command(command, options=options)

    def handleNextCommand(self, command, options=None):
        uid = str(self.env.current_uid)
        self.db.set("pending", uid, "command", command)
        self.db.set("pending", uid, "options", options)
        return True

    def sendMessage(self, text, **kwargs):
        return self.env.send_text(text, **kwargs)

    def broadcast(self, *args, **kwargs):
        return self.env.broadcast(*args, **kwargs)


class DateAndTime:
    @staticmethod
    def now(tz="Asia/Kolkata"):
        d = datetime.now(ZoneInfo(tz))
        return {"date": d.strftime("%Y-%m-%d"), "time": d.strftime("%H:%M:%S")}


class Random:
    @staticmethod
    def randomInt(a, b):
        import random
        return random.randint(int(a), int(b))


class _HTTP:
    def get(self, url, **kwargs):
        with urllib.request.urlopen(url, timeout=20) as r:
            return r.read().decode("utf-8", errors="replace")


class _TBCAds:
    def reward_ad(self, *args, **kwargs):
        # TBC's ad provider has no portable equivalent here.
        # Return False so the old command can continue instead of crashing.
        return False


class _Webhook:
    def __getattr__(self, name):
        def unsupported(*args, **kwargs):
            return None
        return unsupported


class _Libs:
    def __init__(self, env):
        self.Resources = Resources(env.db)
        self.DateAndTime = DateAndTime
        self.Random = Random
        self.HTTP = _HTTP()
        self.tbcads = _TBCAds()
        self.Webhook = _Webhook()

    def __getattr__(self, name):
        # Provide a harmless namespace for less-common TBC libraries.
        return SimpleNamespace()


class TBCEnvironment:
    def __init__(self, bot, export):
        self.bot = bot
        self.export = export
        self.db = _DB()
        self.commands = {}
        for item in export.get("commands", []):
            cmd = item.get("command", "")
            if cmd:
                self.commands[cmd.lstrip("/")] = item.get("code", "")
        self.current_uid = None
        self.current_message = None
        self.current_call = None
        self.current_options = None
        self._local = threading.local()

    def _ctx(self, message=None, call=None, options=None):
        if message is not None:
            self.current_message = message
            self.current_uid = getattr(getattr(message, "chat", None), "id", None)
        elif call is not None:
            self.current_call = call
            self.current_uid = getattr(getattr(call, "message", None), "chat", None)
            if hasattr(self.current_uid, "id"):
                self.current_uid = self.current_uid.id
            if self.current_uid is None:
                self.current_uid = getattr(call, "from_user", None).id
        self.current_options = options

    def _globals(self):
        m = self.current_message
        call = self.current_call
        uid = self.current_uid
        user = getattr(m, "from_user", None) if m else getattr(call, "from_user", None)

        bot_store = BotStore(self)
        user_store = UserStore(self.db, uid)
        libs = _Libs(self)

        # Common TBC globals. These intentionally mirror names used by the export.
        g = {
            "bot": self.bot,
            "Bot": bot_store,
            "User": user_store,
            "libs": libs,
            "ReturnCommand": ReturnCommand,
            "InlineKeyboardMarkup": InlineKeyboardMarkup,
            "InlineKeyboardButton": InlineKeyboardButton,
            "ReplyKeyboardMarkup": ReplyKeyboardMarkup,
            "KeyboardButton": KeyboardButton,
            "LinkPreviewOptions": LinkPreviewOptions,
            "types": types,
            "message": m,
            "call": call,
            "u": uid,
            "params": self._callback_params(call) if call else None,
            "options": self.current_options,
            "os": os,
            "json": json,
            "re": re,
            "html": html,
            "urllib": urllib,
            "urllib_parse": urllib.parse,
            "encodeURIComponent": urllib.parse.quote,
            "HTTP": libs.HTTP,
        }
        return g

    def _callback_params(self, call):
        if not call:
            return "None"
        data = call.data or ""
        parts = data.split(maxsplit=1)
        return parts[1] if len(parts) > 1 else "None"

    def execute(self, cmd, message=None, call=None, options=None):
        code = self.commands.get(cmd.lstrip("/"))
        if code is None:
            return False
        self._ctx(message, call, options)
        g = self._globals()
        # Functions defined in one command are available for that command only,
        # matching the usual TBC command scope.
        try:
            exec(compile(code, f"<TBC:{cmd}>", "exec"), g, g)
        except ReturnCommand:
            return True
        except Exception:
            print(f"\n[TBC COMMAND ERROR] /{cmd}")
            traceback.print_exc()
            try:
                if message:
                    self.bot.send_message(message.chat.id, "⚠️ Command error. Check server logs.")
            except Exception:
                pass
        return True

    def dispatch(self, cmd, message):
        self.db.set("users", str(message.chat.id), "seen", True)
        self.db.set("pending", str(message.chat.id), "last_command", cmd)
        return self.execute(cmd, message=message)

    def dispatch_pending_or_message(self, message):
        uid = str(message.chat.id)
        pending = self.db.get("pending", uid, "command")
        if pending:
            options = self.db.get("pending", uid, "options")
            # Clear before executing; the command can set another pending command.
            self.db.delete("pending", uid, "command")
            self.db.delete("pending", uid, "options")
            return self.execute(str(pending).lstrip("/"), message=message, options=options)

        # Commands not registered because they contain unusual names can still
        # be routed here.
        text = getattr(message, "text", "") or ""
        if text.startswith("/"):
            name = text.split()[0].split("@")[0].lstrip("/")
            if name in self.commands:
                return self.execute(name, message=message)
        return False

    def dispatch_callback(self, call):
        data = call.data or ""
        if data.startswith("/"):
            parts = data[1:].split(maxsplit=1)
            cmd = parts[0]
            options = parts[1] if len(parts) > 1 else None
            return self.execute(cmd, call=call, options=options)
        try:
            self.bot.answer_callback_query(call.id)
        except Exception:
            pass

    def run_command(self, command, options=None):
        cmd = str(command).lstrip("/").split()[0]
        return self.execute(cmd, message=self.current_message, call=self.current_call,
                            options=options)

    def send_text(self, text, **kwargs):
        if self.current_uid is None:
            return None
        return self.bot.send_message(self.current_uid, text, **kwargs)

    def broadcast(self, *args, **kwargs):
        # Safe baseline. The export has several custom broadcast systems.
        # A production migration should implement each required broadcast flow
        # against the stored FulBotUsrs/AllMainChTGID lists.
        return None
