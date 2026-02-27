# bot.py
import telebot
from telebot import types
from datetime import datetime
from config import API_TOKEN
from utils import init_db, add_user, get_user, update_balance, update_daily_bonus_date, vsv_transfer

bot = telebot.TeleBot(API_TOKEN)
init_db()  # initialize DB

# Start command with keyboard
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
    keyboard.add(btn1, btn2, btn3, btn4)

    bot.send_message(
        user_id,
        f"👋 Hello {username}!\nWelcome to the VSV Payment Bot.",
        reply_markup=keyboard
    )

# Listen to keyboard button presses
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
            new_balance = user[2] + 10  # daily bonus amount
            update_balance(user_id, new_balance)
            update_daily_bonus_date(user_id, today)
            bot.send_message(user_id, f"🎁 Daily bonus added! Your new balance: {new_balance}")
        else:
            bot.send_message(user_id, "❌ You already claimed your daily bonus today!")

    elif text == "💸 Withdraw":
        if not user[6]:  # wallet not set
            bot.send_message(user_id, "❌ Please set your UPI/Wallet first using /setwallet <number>")
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

    else:
        bot.send_message(user_id, "Please use the buttons below.")

# Command to set wallet/UPI
@bot.message_handler(commands=['setwallet'])
def set_wallet(message):
    user_id = message.from_user.id
    try:
        wallet_number = message.text.split()[1]
        conn = sqlite3.connect("database.db")
        c = conn.cursor()
        c.execute("UPDATE users SET wallet=? WHERE user_id=?", (wallet_number, user_id))
        conn.commit()
        conn.close()
        bot.send_message(user_id, f"✅ Your wallet/UPI is set: {wallet_number}")
    except:
        bot.send_message(user_id, "❌ Usage: /setwallet <number>")

bot.polling()
