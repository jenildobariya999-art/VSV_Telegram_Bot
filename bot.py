import telebot
from telebot import types

# ----------------- CONFIG -----------------
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

# Example in-memory users database
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

    # ✅ Only welcome message
    bot.send_message(user_id, "*🏡 Welcome To UPI Giveaway Bot!*")


# ----------------- MAIN BUTTONS -----------------
def main_buttons():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("💰 Balance", callback_data="balance"),
        types.InlineKeyboardButton("👤 Refer & Earn", callback_data="refer")
    )
    markup.row(
        types.InlineKeyboardButton("🎁 Bonus & Gift Code", callback_data="bonus"),
        types.InlineKeyboardButton("💸 Withdraw", callback_data="withdraw")
    )
    markup.row(
        types.InlineKeyboardButton("💳 Payout Method", callback_data="payout")
    )
    return markup


# ----------------- CALLBACK HANDLER -----------------
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    if user_id not in users:
        users[user_id] = {"balance":0, "wallet":"not set", "upi":"not set", "referrals":0, "bonus_claimed":False}

    if call.data == "balance":
        text = f"*💰 Balance: ₹{users[user_id]['balance']}*\n\n*Use 'Withdraw' button to withdraw your balance to UPI*"
        bot.edit_message_text(text, user_id, call.message.message_id, reply_markup=balance_markup())

    elif call.data == "refer":
        text = (
            "*💰 Per Refer Rs.4 Upi Cash*\n\n"
            f"*👤Your Referral Link: https://t.me/mybotusername?start={user_id}*\n\n"
            "*Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑*"
        )
        bot.edit_message_text(text, user_id, call.message.message_id, reply_markup=refer_markup())

    elif call.data == "bonus":
        text = "*Bonus/GiftCode 🎁*"
        bot.edit_message_text(text, user_id, call.message.message_id, reply_markup=bonus_markup())

    elif call.data == "withdraw":
        text = "*✨ Choose Withdrawal Method:*"
        bot.edit_message_text(text, user_id, call.message.message_id, reply_markup=withdraw_markup())

    elif call.data == "payout":
        user = users[user_id]
        text = (
            "*Choose Desired Payment Method From Below 👇*\n\n"
            f"*Your Current Wallet - {user['wallet']}*\n"
            f"*Your Current UPI - {user['upi']}*"
        )
        bot.edit_message_text(text, user_id, call.message.message_id, reply_markup=payout_markup())


# ----------------- BUTTON MARKUPS -----------------
def balance_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row(types.InlineKeyboardButton("💸 Withdraw", callback_data="withdraw"))
    markup.row(types.InlineKeyboardButton("⬅ Back", callback_data="start"))
    return markup

def refer_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("📋 My Invites", callback_data="my_invites"),
        types.InlineKeyboardButton("🏆 Leaderboard", callback_data="leaderboard")
    )
    markup.row(types.InlineKeyboardButton("⬅ Back", callback_data="start"))
    return markup

def bonus_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("🎁 Bonus", callback_data="claim_bonus"),
        types.InlineKeyboardButton("🎁 Gift Code", callback_data="claim_gift")
    )
    markup.row(types.InlineKeyboardButton("⬅ Back", callback_data="start"))
    return markup

def withdraw_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("UPI", callback_data="withdraw_upi"),
        types.InlineKeyboardButton("VSV", callback_data="withdraw_vsv")
    )
    markup.row(types.InlineKeyboardButton("⬅ Back", callback_data="start"))
    return markup

def payout_markup():
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("Set Wallet", callback_data="set_wallet"),
        types.InlineKeyboardButton("Set UPI", callback_data="set_upi")
    )
    markup.row(types.InlineKeyboardButton("⬅ Back", callback_data="start"))
    return markup


# ----------------- RUN BOT -----------------
bot.infinity_polling()
