import os
import json
import time
import traceback
import threading
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
from pathlib import Path

import telebot
from telebot import types
from telebot import util

from tbc_runtime import TBCEnvironment

BASE = Path(__file__).resolve().parent
with open(BASE / "tbc_export.json", "r", encoding="utf-8") as f:
    EXPORT = json.load(f)

TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    raise RuntimeError("BOT_TOKEN environment variable is required")

bot = telebot.TeleBot(TOKEN, parse_mode=None)
env = TBCEnvironment(bot, EXPORT)

# Normal slash commands
for item in EXPORT.get("commands", []):
    command = item.get("command", "")
    if not command:
        continue
    # TBC has internal/non-user commands too. We still register every valid
    # command name; aliases are normalized by the runtime.
    name = command.lstrip("/").strip()
    if not name or " " in name:
        continue
    if name.startswith("/"):
        continue

    def make_handler(cmd):
        def handler(message):
            env.dispatch(cmd, message)
        return handler

    try:
        bot.register_message_handler(
            make_handler(name),
            commands=[name],
            pass_bot=True,
            func=lambda m: True
        )
    except Exception:
        # Duplicate/invalid registrations should not prevent the rest loading.
        pass

@bot.message_handler(content_types=[
    "text", "photo", "video", "document", "audio", "voice",
    "animation", "sticker", "contact", "location", "venue"
])
def fallback(message):
    env.dispatch_pending_or_message(message)

@bot.callback_query_handler(func=lambda call: True)
def callbacks(call):
    try:
        env.dispatch_callback(call)
    except Exception:
        traceback.print_exc()
        try:
            bot.answer_callback_query(call.id, "Error")
        except Exception:
            pass

print(f"Loaded {len(EXPORT.get('commands', []))} exported TBC command blocks.")
print("TeleBot compatibility runtime started.")
bot.infinity_polling(
    timeout=30,
    long_polling_timeout=30,
    allowed_updates=["message", "callback_query", "chat_member"]
)
