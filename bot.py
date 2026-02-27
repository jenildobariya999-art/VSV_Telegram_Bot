import telebot
from telebot import types
import sqlite3
import random
import string

# ========== BOT TOKENS (HARD-CODED) ==========
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"  # Telegram Bot Token
VSV_TOKEN = "TVJZCUHK"  # Your VSV Wallet Token
ADMIN_IDS = [6925391837]  # Admin Telegram IDs
BOT_USERNAME = "Testing0011_ibot"

bot = telebot.TeleBot(API_TOKEN)

# ========== DATABASE SETUP ==========
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()

# Users table
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    wallet TEXT,
    upi TEXT,
    email TEXT,
    balance REAL DEFAULT 0,
    daily_claimed INTEGER DEFAULT 0,
    referred_by TEXT
)
""")

# Withdraw table
c.execute("""
CREATE TABLE IF NOT EXISTS withdraws (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    status TEXT,
    method TEXT
)
""")

# Gift codes table
c.execute("""
CREATE TABLE IF NOT EXISTS giftcodes (
    code TEXT PRIMARY KEY,
    user_id INTEGER,
    amount REAL,
    claimed INTEGER DEFAULT 0
)
""")

conn.commit()

# ========== HELPERS ==========
def add_user(user_id, username, referred_by=None):
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if not c.fetchone():
        c.execute(
            "INSERT INTO users (user_id, username, referred_by) VALUES (?, ?, ?)",
            (user_id, username, referred_by)
        )
        conn.commit()

def set_wallet(user_id, wallet=None, upi=None, email=None):
    if wallet: c.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet, user_id))
    if upi: c.execute("UPDATE users SET upi=? WHERE user_id=?", (upi, user_id))
    if email: c.execute("UPDATE users SET email=? WHERE user_id=?", (email, user_id))
    conn.commit()

def update_balance(user_id, amount):
    c.execute("UPDATE users SET balance=balance+? WHERE user_id=?", (amount, user_id))
    conn.commit()

def get_balance(user_id):
    c.execute("SELECT balance FROM users WHERE user_id=?", (user_id,))
    res = c.fetchone()
    return res[0] if res else 0

def get_referrals(ref_code):
    c.execute("SELECT user_id FROM users WHERE referred_by=?", (ref_code,))
    return c.fetchall()

def generate_gift_code(length=8):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# ========== USER INTERACTIONS ==========
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    try:
        ref_code = message.text.split()[1]
    except IndexError:
        ref_code = None

    add_user(user_id, username, referred_by=ref_code)

    markup = types.ReplyKeyboardMarkup(row_width=2, resize_keyboard=True)
    markup.add(
        types.KeyboardButton("💰 Balance"),
        types.KeyboardButton("🎁 Daily Bonus"),
        types.KeyboardButton("💸 Withdraw"),
        types.KeyboardButton("👥 Refer & Earn"),
        types.KeyboardButton("⚙️ Set Wallet"),
        types.KeyboardButton("🎁 Gift Code")
    )
    bot.send_message(user_id, "👋 Welcome! Use the buttons below.", reply_markup=markup)

# ========== BALANCE ==========
@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):
    user_id = message.from_user.id
    bal = get_balance(user_id)
    c.execute("SELECT wallet, upi, email FROM users WHERE user_id=?", (user_id,))
    wallet, upi, email = c.fetchone()
    msg = f"💰 Balance: ₹{bal:.2f}\n\nYour payout info:\nWallet: {wallet or 'not set'}\nUPI: {upi or 'not set'}\nEmail: {email or 'not set'}"
    bot.send_message(user_id, msg)

# ========== DAILY BONUS ==========
@bot.message_handler(func=lambda message: message.text == "🎁 Daily Bonus")
def daily_bonus(message):
    user_id = message.from_user.id
    c.execute("SELECT daily_claimed FROM users WHERE user_id=?", (user_id,))
    claimed = c.fetchone()[0]
    if claimed == 0:
        update_balance(user_id, 10)  # daily bonus ₹10
        c.execute("UPDATE users SET daily_claimed=1 WHERE user_id=?", (user_id,))
        conn.commit()
        bot.send_message(user_id, "🎉 You claimed your daily bonus of ₹10!")
    else:
        bot.send_message(user_id, "⏳ You already claimed your daily bonus today!")

# ========== SET WALLET ==========
@bot.message_handler(func=lambda message: message.text == "⚙️ Set Wallet")
def wallet_prompt(message):
    bot.send_message(message.from_user.id, "Send wallet/UPI/email like this:\n/setwallet wallet_number upi_number email")

@bot.message_handler(commands=['setwallet'])
def set_wallet_command(message):
    try:
        parts = message.text.split()
        wallet = parts[1] if len(parts) > 1 else None
        upi = parts[2] if len(parts) > 2 else None
        email = parts[3] if len(parts) > 3 else None
        set_wallet(message.from_user.id, wallet, upi, email)
        bot.send_message(message.from_user.id, f"✅ Wallet/UPI/Email set successfully!")
    except:
        bot.send_message(message.from_user.id, "❌ Invalid format! Use /setwallet <wallet> <upi> <email>")

# ========== WITHDRAW ==========
@bot.message_handler(func=lambda message: message.text == "💸 Withdraw")
def withdraw(message):
    user_id = message.from_user.id
    bal = get_balance(user_id)
    markup = types.InlineKeyboardMarkup()
    markup.add(
        types.InlineKeyboardButton("UPI", callback_data="withdraw_upi"),
        types.InlineKeyboardButton("VSV", callback_data="withdraw_vsv")
    )
    bot.send_message(user_id, f"💰 Balance: ₹{bal:.2f}\nChoose withdrawal method:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("withdraw"))
def withdraw_method(call):
    method = call.data.split("_")[1]
    bot.send_message(call.from_user.id, f"Send amount to withdraw via {method.upper()}:\n/withdraw_amount {method} <amount>")

@bot.message_handler(commands=['withdraw_amount'])
def withdraw_amount(message):
    try:
        _, method, amount = message.text.split()
        amount = float(amount)
        user_id = message.from_user.id
        bal = get_balance(user_id)
        if amount > bal:
            bot.send_message(user_id, "❌ Insufficient balance")
            return
        c.execute("INSERT INTO withdraws (user_id, amount, status, method) VALUES (?, ?, ?, ?)",
                  (user_id, amount, "Pending", method))
        update_balance(user_id, -amount)
        conn.commit()
        bot.send_message(user_id, f"✅ Withdraw of ₹{amount} via {method.upper()} submitted!")
    except:
        bot.send_message(message.from_user.id, "❌ Format: /withdraw_amount <method> <amount>")

# ========== REFERRAL ==========
@bot.message_handler(func=lambda message: message.text == "👥 Refer & Earn")
def refer_earn(message):
    user_id = message.from_user.id
    referral_code = f"REF{user_id}"
    referrals = get_referrals(referral_code)
    bot_link = f"https://t.me/{BOT_USERNAME}?start={referral_code}"
    msg = f"👥 Invite friends & earn!\n\nYour referral link:\n{bot_link}\nTotal referrals: {len(referrals)}\n💰 Per Refer: Rs.4 UPI Cash"
    bot.send_message(user_id, msg)

# ========== GIFT CODES ==========
@bot.message_handler(func=lambda message: message.text == "🎁 Gift Code")
def gift_code_claim(message):
    user_id = message.from_user.id
    c.execute("SELECT code, amount FROM giftcodes WHERE user_id=? AND claimed=0", (user_id,))
    codes = c.fetchall()
    if not codes:
        bot.send_message(user_id, "🎁 You have no gift codes available.")
        return
    total = 0
    for code, amount in codes:
        total += amount
        c.execute("UPDATE giftcodes SET claimed=1 WHERE code=?", (code,))
    update_balance(user_id, total)
    conn.commit()
    bot.send_message(user_id, f"🎉 Gift codes redeemed! Total ₹{total} added to balance.")

# ========== ADMIN PANEL ==========
@bot.message_handler(commands=['adminpanel'])
def admin_panel(message):
    if message.from_user.id not in ADMIN_IDS:
        bot.send_message(message.from_user.id, "❌ You are not admin!")
        return
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💰 Edit Balance", callback_data="admin_edit_balance"),
        types.InlineKeyboardButton("⚙️ Edit Wallet", callback_data="admin_edit_wallet"),
        types.InlineKeyboardButton("🎁 Set Bonus", callback_data="admin_set_bonus"),
        types.InlineKeyboardButton("💸 Withdraw Requests", callback_data="admin_withdraws"),
        types.InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast"),
        types.InlineKeyboardButton("🎁 Create Gift Code", callback_data="admin_giftcode"),
    )
    bot.send_message(message.from_user.id, "🛠 Admin Panel", reply_markup=markup)

# ========== RUN BOT ==========
bot.infinity_polling()
