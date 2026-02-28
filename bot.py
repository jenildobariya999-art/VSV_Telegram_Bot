import telebot
from telebot import types

# ----------------- CONFIG -----------------
API_TOKEN = "8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8"
bot = telebot.TeleBot(API_TOKEN, parse_mode="Markdown")

# ----------------- DATA -----------------
users = {}
ADMIN_ID = 6925391837

# ----------------- /start -----------------
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "wallet": "not set",
            "upi": "not set",
            "bonus_claimed": False,
            "referrals": 0
        }

    # Main keyboard
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
        users[user_id] = {"balance":0, "wallet":"not set", "upi":"not set", "bonus_claimed":False, "referrals":0}

    user = users[user_id]

    # ---------- BALANCE ----------
    if text == "💰 Balance":
        bot.send_message(
            user_id,
            f"*💰 Balance: ₹{user['balance']}*\n\n*Use 'Withdraw' button to withdraw your balance to UPI*"
        )

    # ---------- REFER & EARN ----------
    elif text == "👤 Refer & Earn":
        # Referral keyboard
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("My Invites", "Leaderboard")
        markup.row("💰 Balance", "🎁 Bonus & Gift Code")
        markup.row("💸 Withdraw", "💳 Payout Method")

        bot.send_message(
            user_id,
            "*💰 Per Refer Rs.4 Upi Cash*\n\n"
            f"*👤 Your Referral Link: https://t.me/mybotusername?start={user_id}*\n\n"
            "*Share With Your Friends & Family And Earn Refer Bonus Easily ✨🤑*",
            reply_markup=markup
        )

    # ---------- BONUS & GIFT CODE ----------
    elif text == "🎁 Bonus & Gift Code":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Claim Bonus", "Gift Code")
        markup.row("💰 Balance", "👤 Refer & Earn")
        markup.row("💸 Withdraw", "💳 Payout Method")

        bot.send_message(
            user_id,
            "*Bonus/GiftCode 🎁*\n\nChoose One:",
            reply_markup=markup
        )

    elif text == "Claim Bonus":
        if not user['bonus_claimed']:
            user['balance'] += 10  # Example bonus
            user['bonus_claimed'] = True
            bot.send_message(user_id, "*✅ Bonus claimed!*")
        else:
            bot.send_message(user_id, "*❌ You already claimed your bonus today!*")

    elif text == "Gift Code":
        bot.send_message(user_id, "*Send your gift code to claim it.*")

    # ---------- WITHDRAW ----------
    elif text == "💸 Withdraw":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("UPI", "VSV")
        markup.row("💰 Balance", "👤 Refer & Earn")
        markup.row("🎁 Bonus & Gift Code", "💳 Payout Method")

        bot.send_message(
            user_id,
            "*✨ Choose Withdrawal Method:*",
            reply_markup=markup
        )

    # ---------- PAYOUT METHOD ----------
    elif text == "💳 Payout Method":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row("Set Wallet", "Set UPI")
        markup.row("💰 Balance", "👤 Refer & Earn")
        markup.row("🎁 Bonus & Gift Code", "💸 Withdraw")

        bot.send_message(
            user_id,
            "*Choose Desired Payment Method From Below 👇*\n\n"
            f"*Your Current Wallet - {user['wallet']}*\n"
            f"*Your Current UPI - {user['upi']}*",
            reply_markup=markup
        )

    # ---------- SET WALLET ----------
    elif text == "Set Wallet":
        bot.send_message(user_id, "*Send your wallet number like this:*\n/setwallet 9876543210")

    elif text == "Set UPI":
        bot.send_message(user_id, "*Send your UPI like this:*\n/setupi 9999999999")

# ---------- COMMANDS FOR SETTING WALLET/UPI ----------
@bot.message_handler(commands=['setwallet'])
def set_wallet(message):
    user_id = message.from_user.id
    wallet = message.text.split(" ")[1] if len(message.text.split(" ")) > 1 else None
    if wallet:
        users[user_id]['wallet'] = wallet
        bot.send_message(user_id, f"*✅ Wallet set to {wallet}*")
    else:
        bot.send_message(user_id, "*❌ Please send wallet like /setwallet 9876543210*")

@bot.message_handler(commands=['setupi'])
def set_upi(message):
    user_id = message.from_user.id
    upi = message.text.split(" ")[1] if len(message.text.split(" ")) > 1 else None
    if upi:
        users[user_id]['upi'] = upi
        bot.send_message(user_id, f"*✅ UPI set to {upi}*")
    else:
        bot.send_message(user_id, "*❌ Please send UPI like /setupi 9999999999*")

# ----------------- RUN BOT -----------------
bot.infinity_polling()
