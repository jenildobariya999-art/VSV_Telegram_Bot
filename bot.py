import telebot
from config import API_TOKEN, ADMIN_IDS

bot = telebot.TeleBot(API_TOKEN)

# Start command
@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    username = message.from_user.username or "User"
    bot.send_message(user_id, f"👋 Hello {username}!\nWelcome to the VSV Payment Bot.\n\nUse /dailybonus to claim your daily bonus.\nUse /balance to check your balance.\nUse /withdraw to withdraw money.")

bot.polling()
