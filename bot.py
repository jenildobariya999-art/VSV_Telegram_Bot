import telebot
from telebot import types
import sqlite3
import os

# ========== Environment Variables ==========
API_TOKEN = os.environ.get("8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8")  # Telegram Bot Token
VSV_TOKEN = os.environ.get("TVJZCUHK")  # Your VSV API Token
ADMIN_ID = 6925391837  # Replace with your Telegram ID

if not API_TOKEN or not VSV_TOKEN:
    raise Exception("❌ API_TOKEN or VSV_TOKEN is not set in environment variables!")

bot = telebot.TeleBot(API_TOKEN)

# ========== Database Setup ==========
conn = sqlite3.connect("database.db", check_same_thread=False)
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS users (
    user_id INTEGER PRIMARY KEY,
    username TEXT,
    wallet TEXT,
    balance REAL DEFAULT 0,
    daily_claimed INTEGER DEFAULT 0,
    referred_by TEXT
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS withdraws (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    amount REAL,
    status TEXT
)
""")
conn.commit()

# ========== Helper Functions ==========
def add_user(user_id, username, referred_by=None):
    c.execute("SELECT * FROM users WHERE user_id=?", (user_id,))
    if not c.fetchone():
        c.execute(
            "INSERT INTO users (user_id, username, referred_by) VALUES (?, ?, ?)",
            (user_id, username, referred_by)
        )
        conn.commit()

def set_wallet(user_id, wallet):
    c.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet, user_id))
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

# ========== Start Command ==========
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
        types.KeyboardButton("⚙️ Set Wallet")
    )
    bot.send_message(user_id, "👋 Welcome! Use the buttons below.", reply_markup=markup)

# ========== Balance ==========
@bot.message_handler(func=lambda message: message.text == "💰 Balance")
def balance(message):
    user_id = message.from_user.id
    bal = get_balance(user_id)
    bot.send_message(user_id, f"💰 Your balance: ₹{bal:.2f}")

# ========== Daily Bonus ==========
@bot.message_handler(func=lambda message: message.text == "🎁 Daily Bonus")
def daily_bonus(message):
    user_id = message.from_user.id
    c.execute("SELECT daily_claimed FROM users WHERE user_id=?", (user_id,))
    claimed = c.fetchone()[0]
    if claimed == 0:
        update_balance(user_id, 10)  # daily bonus ₹10
        c.execute("UPDATE users SET daily_claimed=1")
        conn.commit()
        bot.send_message(user_id, "🎉 You claimed your daily bonus of ₹10!")
    else:
        bot.send_message(user_id, "⏳ You already claimed your daily bonus today!")

# ========== Set Wallet ==========
@bot.message_handler(func=lambda message: message.text == "⚙️ Set Wallet")
def wallet_prompt(message):
    bot.send_message(message.from_user.id, "Send your wallet/UPI number like this:\n/setwallet 9876543210")

@bot.message_handler(commands=['setwallet'])
def set_wallet_command(message):
    try:
        wallet = message.text.split()[1]
        set_wallet(message.from_user.id, wallet)
        bot.send_message(message.from_user.id, f"✅ Wallet set to {wallet}")
    except IndexError:
        bot.send_message(message.from_user.id, "❌ Invalid format! Use /setwallet <number>")

# ========== Withdraw ==========
@bot.message_handler(func=lambda message: message.text == "💸 Withdraw")
def withdraw(message):
    user_id = message.from_user.id
    bal = get_balance(user_id)
    bot.send_message(user_id, f"💰 Your balance: ₹{bal}\nSend amount to withdraw like this:\n/withdraw 50")

@bot.message_handler(commands=['withdraw'])
def withdraw_command(message):
    try:
        amount = float(message.text.split()[1])
        bal = get_balance(message.from_user.id)
        if amount > bal:
            bot.send_message(message.from_user.id, "❌ You don't have enough balance.")
            return
        # Insert into withdraw table
        c.execute("INSERT INTO withdraws (user_id, amount, status) VALUES (?, ?, ?)", (message.from_user.id, amount, "Pending"))
        update_balance(message.from_user.id, -amount)
        conn.commit()
        bot.send_message(message.from_user.id, f"✅ Withdraw request for ₹{amount} sent!")
    except Exception as e:
        bot.send_message(message.from_user.id, "❌ Invalid format! Use /withdraw <amount>")

# ========== Referral ==========
@bot.message_handler(func=lambda message: message.text == "👥 Refer & Earn")
def refer_earn(message):
    user_id = message.from_user.id
    referral_code = f"REF{user_id}"
    referrals = get_referrals(referral_code)
    bot_link = f"https://t.me/YOUR_BOT_USERNAME?start={referral_code}"  # replace with your bot username

    msg = f"👥 Invite your friends and earn bonuses!\n\n" \
          f"Your referral link:\n{bot_link}\n\n" \
          f"Total referrals: {len(referrals)}"
    bot.send_message(user_id, msg)

# ========== Admin Panel ==========
@bot.message_handler(commands=['adminpanel'])
def admin_panel(message):
    if message.from_user.id != ADMIN_ID:
        bot.send_message(message.from_user.id, "❌ You are not admin!")
        return
    markup = types.InlineKeyboardMarkup(row_width=2)
    markup.add(
        types.InlineKeyboardButton("💰 Edit User Balance", callback_data="edit_balance"),
        types.InlineKeyboardButton("⚙️ Edit User Wallet", callback_data="edit_wallet"),
        types.InlineKeyboardButton("🎁 Daily Bonus Control", callback_data="daily_bonus_control"),
        types.InlineKeyboardButton("💸 Withdraw Requests", callback_data="withdraw_requests"),
        types.InlineKeyboardButton("👥 Referral Dashboard", callback_data="ref_dashboard")
    )
    bot.send_message(ADMIN_ID, "🛠 Admin Panel", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def callback_admin(call):
    if call.from_user.id != ADMIN_ID:
        return

    if call.data == "ref_dashboard":
        c.execute("SELECT user_id, username FROM users")
        data = c.fetchall()
        msg = "👥 Referral Dashboard:\n"
        for d in data:
            referrals = get_referrals(f"REF{d[0]}")
            msg += f"{d[1]} ({d[0]}): {len(referrals)} referrals\n"
        bot.send_message(ADMIN_ID, msg)

    elif call.data == "withdraw_requests":
        c.execute("SELECT id, user_id, amount, status FROM withdraws WHERE status='Pending'")
        rows = c.fetchall()
        msg = "💸 Pending Withdraw Requests:\n"
        for r in rows:
            msg += f"ID:{r[0]} | User:{r[1]} | Amount:₹{r[2]}\n"
        bot.send_message(ADMIN_ID, msg)

# ========== Run Bot ==========
bot.infinity_polling()
