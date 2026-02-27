import telebot
from telebot import types
import sqlite3
import random
import string

# ======== BOT TOKENS ========
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"
VSV_TOKEN = "TVJZCUHK"
ADMIN_IDS = [6925391837]
BOT_USERNAME = "Testing0011_ibot"

bot = telebot.TeleBot(API_TOKEN)

# ======== DATABASE ========
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

# ======== HELPERS ========
def add_user(user_id, username, referred_by=None):
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if not c.fetchone():
        c.execute("INSERT INTO users (user_id, username, referred_by) VALUES (?, ?, ?)", (user_id, username, referred_by))
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

# ======== START / USER INTERFACE ========
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    try:
        ref_code = message.text.split()[1]
    except IndexError:
        ref_code = None

    add_user(user_id, username, referred_by=ref_code)
    send_main_menu(user_id)

def send_main_menu(user_id):
    c.execute("SELECT balance, wallet, upi, email FROM users WHERE user_id=?", (user_id,))
    data = c.fetchone()
    bal = data[0]
    wallet = data[1] or "not set"
    upi = data[2] or "not set"
    email = data[3] or "not set"

    msg = f"""💰 Balance: ₹{bal:.2f}

Use 'Withdraw' button to withdraw your balance to upi

Refer and earn
💰 Per Refer Rs.4 Upi Cash

👤Your Refferal Link: https://t.me/{BOT_USERNAME}?start={user_id}

Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑

Bonus & Gift Code
✨ Choose One:
"""
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("🎁 Bonus", callback_data="daily_bonus"),
        types.InlineKeyboardButton("🎁 Gift Code", callback_data="gift_code")
    )
    msg += "\n✨ Choose Withdrawal Method:"
    markup2 = types.InlineKeyboardMarkup(row_width=2)
    markup2.add(
        types.InlineKeyboardButton("UPI", callback_data="withdraw_upi"),
        types.InlineKeyboardButton("VSV", callback_data="withdraw_vsv")
    )
    payout_msg = f"""

Choose Desired Payment Method From Below 👇

Payout method
Your Current Wallet - {wallet}
Your Current UPI - {upi}
Your Current Email - {email}
"""
    bot.send_message(user_id, msg, reply_markup=markup)
    bot.send_message(user_id, "Choose Withdrawal Method:", reply_markup=markup2)
    bot.send_message(user_id, payout_msg)

# ======== CALLBACK HANDLERS ========
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id

    # ===== DAILY BONUS =====
    if call.data == "daily_bonus":
        c.execute("SELECT daily_claimed FROM users WHERE user_id=?", (user_id,))
        claimed = c.fetchone()[0]
        if claimed == 0:
            update_balance(user_id, 10)
            c.execute("UPDATE users SET daily_claimed=1 WHERE user_id=?", (user_id,))
            conn.commit()
            bot.answer_callback_query(call.id, "🎉 You claimed your daily bonus of ₹10!")
        else:
            bot.answer_callback_query(call.id, "⏳ You already claimed your daily bonus today!")

    # ===== GIFT CODE =====
    elif call.data == "gift_code":
        c.execute("SELECT code, amount FROM giftcodes WHERE user_id=? AND claimed=0", (user_id,))
        codes = c.fetchall()
        if not codes:
            bot.answer_callback_query(call.id, "🎁 You have no gift codes available.")
            return
        total = 0
        for code, amount in codes:
            total += amount
            c.execute("UPDATE giftcodes SET claimed=1 WHERE code=?", (code,))
        update_balance(user_id, total)
        conn.commit()
        bot.answer_callback_query(call.id, f"🎉 Gift codes redeemed! Total ₹{total} added to balance.")

    # ===== WITHDRAW =====
    elif call.data.startswith("withdraw"):
        method = call.data.split("_")[1]
        bot.send_message(user_id, f"Send amount to withdraw via {method.upper()}:\n/withdraw_amount {method} <amount>")

    # ===== ADMIN PANEL =====
    elif call.data.startswith("admin"):
        if user_id not in ADMIN_IDS:
            bot.answer_callback_query(call.id, "❌ You are not admin!")
            return
        bot.answer_callback_query(call.id, "Admin panel clicked! (Inline buttons coming soon)")

# ======== WITHDRAW COMMAND ========
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

# ======== SET WALLET COMMAND ========
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

# ======== ADMIN PANEL COMMAND ========
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

# ======== RUN BOT ========
bot.infinity_polling()
