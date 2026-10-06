import os
import telebot

TOKEN = os.environ["BOT_TOKEN"]

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    bot.reply_to(message, "✅ Bot is working!")

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, message.text)

print("🤖 Bot started...")
bot.infinity_polling()
