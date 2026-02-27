import telebot
from telebot import types

# ----- API KEYS -----
API_TOKEN = '8534393299:AAFLYuQiqImk6wWI6TLTYrR_7xKbgwZvK_8'  # your bot token
VSV_TOKEN = 'TVJZCUHK'  # your VSV gateway token

bot = telebot.TeleBot(API_TOKEN)

# ----- DATABASE SIMULATION -----
users = {}  # user_id: {balance, wallet, upi, email, referrals, bonus_claimed}
gift_codes = {}  # code: {amount, user_id (optional)}

# ----- MAIN MENU -----
def main_menu_markup(user_id):
    markup = types.InlineKeyboardMarkup()
    
    # Bonus & Gift Code
    markup.row(
        types.InlineKeyboardButton("🎁 Bonus", callback_data="bonus"),
        types.InlineKeyboardButton("🎉 Gift Code", callback_data="giftcode")
    )
    # Withdraw
    markup.row(
        types.InlineKeyboardButton("💸 Withdraw", callback_data="withdraw")
    )
    # Set payout method
    markup.row(
        types.InlineKeyboardButton("💳 Set Wallet/UPI/Email", callback_data="setpayout")
    )
    # Admin Panel (only for admin users)
    if user_id == 6925391837:  # Replace with your Telegram ID
        markup.row(
            types.InlineKeyboardButton("🛠 Admin Panel", callback_data="adminpanel")
        )
    return markup

# ----- START COMMAND -----
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    if user_id not in users:
        users[user_id] = {
            "balance": 0,
            "wallet": "not set",
            "upi": "not set",
            "email": "not set",
            "referrals": 0,
            "bonus_claimed": False
        }

    # Welcome message first
    bot.send_message(user_id, "🏡 Welcome To UPI Giveaway Bot!")

    # Then show main menu
    show_user_dashboard(user_id)

def show_user_dashboard(user_id):
    user = users[user_id]
    text = f"""💰 Balance: ₹{user['balance']}

Use 'Withdraw' button to withdraw your balance to upi

Refer and earn 
💰 Per Refer Rs.4 Upi Cash

👤Your Referral Link: https://t.me/ThunderCashBot?start={user_id}

Share With Your Friend's & Family And Earn Refer Bonus Easily ✨🤑

Bonus & Gift Code:
✨ Choose One:

✨ Choose Withdrawal Method:
Withdraw 2 inline button UPI Or VSV

Choose Desired Payment Method From Below 👇

Payout method
Your Current Wallet - {user['wallet']}
Your Current UPI - {user['upi']}
Your Current Email - {user['email']}
"""
    bot.send_message(user_id, text, reply_markup=main_menu_markup(user_id))

# ----- CALLBACK HANDLER -----
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    if call.data == "bonus":
        claim_bonus(user_id, call.message)
    elif call.data == "giftcode":
        bot.send_message(user_id, "Please enter your gift code using /gift <code>")
    elif call.data == "withdraw":
        show_withdraw_options(user_id)
    elif call.data == "setpayout":
        bot.send_message(user_id, "Set your Wallet/UPI/Email using commands:\n/setwallet <number>\n/setupi <upi>\n/setemail <email>")
    elif call.data == "adminpanel" and user_id == 6925391837:
        show_admin_panel(user_id)
    else:
        bot.answer_callback_query(call.id, "❌ Unauthorized or unknown action.")

# ----- BONUS -----
def claim_bonus(user_id, message):
    user = users[user_id]
    if user["bonus_claimed"]:
        bot.send_message(user_id, "⚠️ You have already claimed your daily bonus!")
    else:
        user["balance"] += 10  # daily bonus amount
        user["bonus_claimed"] = True
        bot.send_message(user_id, "🎉 You claimed your bonus!")
        show_user_dashboard(user_id)

# ----- WITHDRAW -----
def show_withdraw_options(user_id):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("💸 UPI Withdraw", callback_data="withdraw_upi"),
        types.InlineKeyboardButton("💸 VSV Withdraw", callback_data="withdraw_vsv")
    )
    bot.send_message(user_id, "Choose withdrawal method:", reply_markup=markup)

@bot.callback_query_handler(func=lambda call: call.data.startswith("withdraw_"))
def withdraw_handler(call):
    user_id = call.from_user.id
    method = call.data.split("_")[1]
    bot.send_message(user_id, f"Withdrawal via {method.upper()} selected.\nUse /withdraw_amount <amount> to withdraw.")

# ----- ADMIN PANEL -----
def show_admin_panel(admin_id):
    markup = types.InlineKeyboardMarkup()
    markup.row(
        types.InlineKeyboardButton("💰 Edit User Balance", callback_data="admin_edit_balance"),
        types.InlineKeyboardButton("💳 Edit User Wallet", callback_data="admin_edit_wallet")
    )
    markup.row(
        types.InlineKeyboardButton("🎁 Create Gift Code", callback_data="admin_create_giftcode"),
        types.InlineKeyboardButton("📢 Broadcast", callback_data="admin_broadcast")
    )
    markup.row(
        types.InlineKeyboardButton("⚡ Set Bonus Amount", callback_data="admin_set_bonus"),
        types.InlineKeyboardButton("💸 Withdraw Requests", callback_data="admin_withdraw_requests")
    )
    bot.send_message(admin_id, "🛠 Admin Panel:", reply_markup=markup)

# ----- ADMIN BUTTON HANDLERS -----
@bot.callback_query_handler(func=lambda call: call.data.startswith("admin_"))
def admin_handler(call):
    admin_id = call.from_user.id
    action = call.data.split("_")[1]
    if admin_id != 6925391837:
        bot.answer_callback_query(call.id, "❌ You are not admin.")
        return

    if action == "edit":
        bot.send_message(admin_id, "Use /edit_balance <user_id> <amount>")
    elif action == "wallet":
        bot.send_message(admin_id, "Use /edit_wallet <user_id> <wallet_number>")
    elif action == "create":
        bot.send_message(admin_id, "Use /create_gift <user_id> <amount> to create gift code")
    elif action == "broadcast":
        bot.send_message(admin_id, "Use /broadcast <message> to send message to all users")
    elif action == "set":
        bot.send_message(admin_id, "Use /set_bonus <amount> to change daily bonus")
    elif action == "withdraw":
        bot.send_message(admin_id, "List of withdraw requests (simulate in db)")

# ----- COMMANDS -----
@bot.message_handler(commands=['setwallet'])
def set_wallet(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Usage: /setwallet <number>")
        return
    users[message.from_user.id]["wallet"] = args[1]
    bot.reply_to(message, f"✅ Wallet set to {args[1]}")

@bot.message_handler(commands=['setupi'])
def set_upi(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Usage: /setupi <upi>")
        return
    users[message.from_user.id]["upi"] = args[1]
    bot.reply_to(message, f"✅ UPI set to {args[1]}")

@bot.message_handler(commands=['setemail'])
def set_email(message):
    args = message.text.split()
    if len(args) < 2:
        bot.reply_to(message, "Usage: /setemail <email>")
        return
    users[message.from_user.id]["email"] = args[1]
    bot.reply_to(message, f"✅ Email set to {args[1]}")

# ----- RUN BOT -----
bot.infinity_polling()
