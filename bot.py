# bot.py
import telebot
from telebot import types
from datetime import datetime
import sqlite3
from config import API_TOKEN, VSV_TOKEN

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

# -------------------- Listen to button presses --------------------
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.from_user.id
    text = message.text
    user = get_user(user_id)

    if text == "💰 Balance":
        balance = user[2] if user else 0
        bot.send_message(user_id, f"💰 Your balance is: {balance}")

    elif text == "🎁 Daily Bonus":
        today = str(datetime.now().date())
        if user[5] != today:
            new_balance = user[2] + 10  # daily bonus
            update_balance(user_id, new_balance)
            update_daily_bonus_date(user_id, today)
            bot.send_message(user_id, f"🎁 Daily bonus added! Your new balance: {new_balance}")
        else:
            bot.send_message(user_id, "❌ You already claimed your daily bonus today!")

    elif text == "💸 Withdraw":
        if not user[6]:
            bot.send_message(user_id, "❌ Please set your UPI/Wallet first using the 💳 Set Wallet button.")
        else:
            amount = user[2]
            if amount <= 0:
                bot.send_message(user_id, "❌ You have no balance to withdraw!")
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

# -------------------- Command to set wallet --------------------
@bot.message_handler(commands=['setwallet'])
def set_wallet_command(message):
    user_id = message.from_user.id
    try:
        wallet_number = message.text.split()[1]
        set_wallet(user_id, wallet_number)
        bot.send_message(user_id, f"✅ Your wallet/UPI is set: {wallet_number}")
    except:
        bot.send_message(user_id, "❌ Usage: /setwallet <number>")

# -------------------- Run the bot --------------------
bot.polling()
