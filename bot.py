# bot.py
import telebot
from telebot import types
from datetime import datetime
import sqlite3
import requests

# -------------------- Tokens --------------------
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"
VSV_TOKEN = "TVJZCUHK"
ADMIN_ID = 6925391837  # <-- Replace with your Telegram ID

bot = telebot.TeleBot(API_TOKEN)

# -------------------- Database functions --------------------
def init_db():
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("""CREATE TABLE IF NOT EXISTS users (
                    user_id INTEGER PRIMARY KEY,
                    username TEXT,
                    balance REAL DEFAULT 0,
                    referral_code TEXT,
                    referred_by TEXT,
                    last_daily_bonus TEXT,
                    wallet TEXT
                )""")
    c.execute("""CREATE TABLE IF NOT EXISTS settings (
                    key TEXT PRIMARY KEY,
                    value REAL
                )""")
    # Set default settings
    c.execute("INSERT OR IGNORE INTO settings(key,value) VALUES (?,?)", ("daily_bonus", 10))
    c.execute("INSERT OR IGNORE INTO settings(key,value) VALUES (?,?)", ("min_withdraw", 50))
    conn.commit()
    conn.close()

def add_user(user_id, username):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("INSERT OR IGNORE INTO users(user_id, username) VALUES (?, ?)", (user_id, username))
    conn.commit()
    conn.close()

def get_user(user_id):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    user = c.fetchone()
    conn.close()
    return user

def update_balance(user_id, new_balance):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET balance=? WHERE user_id=?", (new_balance, user_id))
    conn.commit()
    conn.close()

def update_daily_bonus_date(user_id, date_str):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET last_daily_bonus=? WHERE user_id=?", (date_str, user_id))
    conn.commit()
    conn.close()

def set_wallet(user_id, wallet_number):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet_number, user_id))
    conn.commit()
    conn.close()

def get_setting(key):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT value FROM settings WHERE key=?", (key,))
    result = c.fetchone()
    conn.close()
    return result[0] if result else None

def set_setting(key, value):
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("UPDATE settings SET value=? WHERE key=?", (value, key))
    conn.commit()
    conn.close()

# -------------------- VSV Payment function --------------------
def vsv_transfer(paytm_number, amount, comment):
    url = f"https://vsv-gateway-solutions.co.in/Api/api.php?token={VSV_TOKEN}&paytm={paytm_number}&amount={amount}&comment={comment}"
    try:
        response = requests.get(url)
        return response.json()
    except Exception as e:
        return {"status": "error", "message": str(e)}

# -------------------- Initialize DB --------------------
init_db()

# -------------------- Start command --------------------
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    add_user(user_id, username)

    keyboard = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    btn1 = types.KeyboardButton("💰 Balance")
    btn2 = types.KeyboardButton("🎁 Daily Bonus")
    btn3 = types.KeyboardButton("💸 Withdraw")
    btn4 = types.KeyboardButton("👥 Refer & Earn")
    btn5 = types.KeyboardButton("💳 Set Wallet")
    keyboard.add(btn1, btn2, btn3, btn4, btn5)

    bot.send_message(
        user_id,
        f"👋 Hello {username}!\nWelcome to the VSV Payment Bot.",
        reply_markup=keyboard
    )

# -------------------- Handle button presses --------------------
@bot.message_handler(func=lambda message: not message.text.startswith("/"))
def handle_buttons(message):
    user_id = message.from_user.id
    text = message.text
    user = get_user(user_id)

    if text == "💰 Balance":
        balance = user[2] if user else 0
        bot.send_message(user_id, f"💰 Your balance is: {balance}")

    elif text == "🎁 Daily Bonus":
        today = str(datetime.now().date())
        bonus_amount = get_setting("daily_bonus")
        if user[5] != today:
            new_balance = user[2] + bonus_amount
            update_balance(user_id, new_balance)
            update_daily_bonus_date(user_id, today)
            bot.send_message(user_id, f"🎁 Daily bonus added! Your new balance: {new_balance}")
        else:
            bot.send_message(user_id, "❌ You already claimed your daily bonus today!")

    elif text == "💸 Withdraw":
        min_withdraw = get_setting("min_withdraw")
        if not user[6]:
            bot.send_message(user_id, "❌ Please set your UPI/Wallet first using 💳 Set Wallet button.")
        else:
            amount = user[2]
            if amount < min_withdraw:
                bot.send_message(user_id, f"❌ Minimum withdrawal is {min_withdraw}")
            else:
                result = vsv_transfer(user[6], amount, "Withdraw")
                if result.get("status") == "success":
                    update_balance(user_id, 0)
                    bot.send_message(user_id, f"✅ Withdrawal successful! {amount} sent to your wallet.")
                else:
                    bot.send_message(user_id, f"❌ Withdrawal failed: {result.get('message')}")

    elif text == "👥 Refer & Earn":
        referral_code = f"REF{user_id}"
        bot.send_message(user_id, f"👥 Your referral code is: {referral_code}")

    elif text == "💳 Set Wallet":
        bot.send_message(user_id, "Send your wallet/UPI number like this:\n/setwallet 9876543210")

    else:
        bot.send_message(user_id, "Please use the buttons below.")

# -------------------- Set Wallet Command --------------------
@bot.message_handler(commands=['setwallet'])
def set_wallet_command(message):
    user_id = message.from_user.id
    try:
        wallet_number = message.text.split()[1]
        set_wallet(user_id, wallet_number)
        bot.send_message(user_id, f"✅ Your wallet/UPI is set: {wallet_number}")
    except:
        bot.send_message(user_id, "❌ Usage: /setwallet <number>")

# -------------------- Admin Panel --------------------
@bot.message_handler(commands=['adminpanel'])
def admin_panel(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.from_user.id, "❌ You are not authorized!")
        return

    keyboard = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton("💰 Change User Balance", callback_data="change_balance")
    btn2 = types.InlineKeyboardButton("🎁 Change Daily Bonus", callback_data="change_bonus")
    btn3 = types.InlineKeyboardButton("💸 Change Min Withdraw", callback_data="change_min_withdraw")
    btn4 = types.InlineKeyboardButton("📢 Broadcast Message", callback_data="broadcast")
    keyboard.add(btn1, btn2, btn3, btn4)
    bot.send_message(ADMIN_ID, "⚙️ Admin Panel", reply_markup=keyboard)

@bot.callback_query_handler(func=lambda call: True)
def handle_admin_buttons(call):
    if call.from_user.id != ADMIN_ID:
        bot.answer_callback_query(call.id, "❌ Unauthorized")
        return

    if call.data == "change_balance":
        bot.send_message(ADMIN_ID, "Send message in this format:\n/setbalance <user_id> <amount>")

    elif call.data == "change_bonus":
        bot.send_message(ADMIN_ID, "Send message in this format:\n/setbonus <amount>")

    elif call.data == "change_min_withdraw":
        bot.send_message(ADMIN_ID, "Send message in this format:\n/setminwithdraw <amount>")

    elif call.data == "broadcast":
        bot.send_message(ADMIN_ID, "Send message in this format:\n/broadcast <your message>")

# -------------------- Admin Commands --------------------
@bot.message_handler(commands=['setbalance'])
def admin_set_balance(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        parts = message.text.split()
        user_id = int(parts[1])
        amount = float(parts[2])
        update_balance(user_id, amount)
        bot.send_message(ADMIN_ID, f"✅ Balance for {user_id} set to {amount}")
    except:
        bot.send_message(ADMIN_ID, "❌ Usage: /setbalance <user_id> <amount>")

@bot.message_handler(commands=['setbonus'])
def admin_set_bonus(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        amount = float(message.text.split()[1])
        set_setting("daily_bonus", amount)
        bot.send_message(ADMIN_ID, f"✅ Daily bonus set to {amount}")
    except:
        bot.send_message(ADMIN_ID, "❌ Usage: /setbonus <amount>")

@bot.message_handler(commands=['setminwithdraw'])
def admin_set_min_withdraw(message):
    if message.from_user.id != ADMIN_ID:
        return
    try:
        amount = float(message.text.split()[1])
        set_setting("min_withdraw", amount)
        bot.send_message(ADMIN_ID, f"✅ Minimum withdrawal set to {amount}")
    except:
        bot.send_message(ADMIN_ID, "❌ Usage: /setminwithdraw <amount>")

@bot.message_handler(commands=['broadcast'])
def admin_broadcast(message):
    if message.from_user.id != ADMIN_ID:
        return
    broadcast_msg = message.text.replace("/broadcast", "").strip()
    conn = sqlite3.connect("database.db")
    c = conn.cursor()
    c.execute("SELECT user_id FROM users")
    users = c.fetchall()
    for u in users:
        bot.send_message(u[0], broadcast_msg)
    conn.close()
    bot.send_message(ADMIN_ID, "✅ Broadcast sent to all users")

# -------------------- Run Bot --------------------
bot.polling()
