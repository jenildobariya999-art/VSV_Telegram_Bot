import telebot
from telebot import types

# ----------------- CONFIG -----------------
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

# In-memory users database
users = {}

# Admin ID
ADMIN_ID = 6925391837
# ------------------------------------------

# ----------------- /start -----------------
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "wallet": "not set",
            "upi": "not set",
            "referrals": 0,
            "bonus_claimed": False
        }

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("💰 Balance", "👤 Refer & Earn")
    markup.row("🎁 Bonus & Gift Code", "💸 Withdraw")
    markup.row("💳 Payout Method")
    
    bot.send_message(
        user_id,
        "*🏡 Welcome To UPI Giveaway Bot!*",
        reply_markup=markup
    )

# ----------------- BUTTON HANDLER -----------------
@bot.message_handler(func=lambda message: True)
def handle_buttons(message):
    user_id = message.from_user.id
    text = message.text

    if user_id not in users:
        users[user_id] = {"balance":0, "wallet":"not set", "upi":"not set", "referrals":0, "bonus_claimed":False}

    if text == "💰 Balance":
        bot.send_message(
            user_id,
            f"*💰 Balance: ₹{users[user_id]['balance']}*\n\n*Use 'Withdraw' button to withdraw your balance to UPI*"
        )

    elif text == "👤 Refer & Earn":
        bot.send_message(
            user_id,
            "*💰 Per Refer Rs.4 Upi Cash*\n\n"
            f"*👤Your Referral Link: https://t.me/mybotusername?start={user_id}*\n\n"
            "*Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑*"
        )

    elif text == "🎁 Bonus & Gift Code":
        bot.send_message(
            user_id,
            "*Bonus/GiftCode 🎁*\n\nChoose One:\nBonus or Gift Code"
        )

    elif text == "💸 Withdraw":
        bot.send_message(
            user_id,
            "*✨ Choose Withdrawal Method:*\nUPI or VSV"
        )

    elif text == "💳 Payout Method":
        user = users[user_id]
        bot.send_message(
            user_id,
            "*Choose Desired Payment Method From Below 👇*\n\n"
            f"*Your Current Wallet - {user['wallet']}*\n"
            f"*Your Current UPI - {user['upi']}*\n\n"
            "Use 'Set Wallet' or 'Set UPI' to update"
        )

    elif text.lower() == "set wallet":
        bot.send_message(user_id, "*Send your wallet number like this:*\n/setwallet 9876543210")
    elif text.lower() == "set upi":
        bot.send_message(user_id, "*Send your UPI like this:*\n/setupi 9999999999")

# ----------------- RUN BOT -----------------
bot.infinity_polling()
