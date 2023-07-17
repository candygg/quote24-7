import telebot
import requests
import random
import os

bot = telebot.TeleBot(os.environ['TELEGRAM_API_TOKEN'])
CHANNEL_ID = "@botcraftpython"


def check_membership(user_id):
    try:
        chat_member = bot.get_chat_member(CHANNEL_ID, user_id)
        return chat_member.status in ["member", "creator", "administrator"]
    except telebot.apihelper.ApiException:
        return False


@bot.message_handler(commands=['start'])
def start(message):
    try:
        if check_membership(message.from_user.id):
            bot.send_photo(
                message.chat.id,
                "https://img.freepik.com/premium-vector/bot-sign-welcome-chatbot-online-consultation-support-service-vector-illustration_476325-701.jpg?w=2000",
                caption=
                "Hello, Welcome to the bot! Click on /help command to show all available commands. 😊",
                parse_mode="Markdown")
        else:
            bot.send_photo(
                message.chat.id,
                "https://latium.org/storage/prod/kQ3d42JD/full/1000x",
                caption=
                "*⛔️ Access Denied ⛔️*\n\nYou are not joined our channel ❗️\n\nIf you want to use me,\n\nJoin our channel [@BotCraftPython](https://t.me/BotCraftPython) 👥",
                parse_mode="Markdown")
    except Exception as e:
        print("An error occurred in the start command:", e)


@bot.message_handler(commands=['help'])
def help(message):
    try:
        if check_membership(message.from_user.id):
            help_message = "Available Commands in the bot:\n\n" \
                           "/start - Restart the bot.\n" \
                           "/help - Show Available Commands.\n" \
                           "/quote - Get a random quote.\n" \
                           "/contact - Contact the bot owner."
            bot.send_message(message.chat.id, help_message, parse_mode="Markdown")
        else:
            bot.send_photo(
                message.chat.id,
                "https://latium.org/storage/prod/kQ3d42JD/full/1000x",
                caption=
                "*⛔️ Access Denied ⛔️*\n\nYou are not joined our channel ❗️\n\nIf you want to use me,\n\nJoin our channel [@BotCraftPython](https://t.me/BotCraftPython) 👥",
                parse_mode="Markdown")
    except Exception as e:
        print("An error occurred in the help command:", e)


@bot.message_handler(commands=['quote'])
def get_quote(message):
    try:
        if check_membership(message.from_user.id):
            try:
                api = requests.get("https://api.quotable.io/quotes/random")
                quote = api.json()

                quotes = quote['content']
                author = quote['author']

                quote_message = f'*"{quotes}"*\n\n- {author} 💬'
                bot.send_message(message.chat.id, quote_message, parse_mode="Markdown")
            except requests.exceptions.RequestException:
                bot.send_message(
                    message.chat.id,
                    "Apologies, there was an error fetching the quote. Please try again later. 😕",
                    parse_mode="Markdown")
        else:
            bot.send_photo(
                message.chat.id,
                "https://latium.org/storage/prod/kQ3d42JD/full/1000x",
                caption=
                "*⛔️ Access Denied ⛔️*\n\nYou are not joined our channel ❗️\n\nIf you want to use me,\n\nJoin our channel [@BotCraftPython](https://t.me/BotCraftPython) 👥",
                parse_mode="Markdown")
    except Exception as e:
        print("An error occurred in the quote command:", e)


@bot.message_handler(commands=['contact'])
def contact_owner(message):
    try:
        if check_membership(message.from_user.id):
            contact_message = "If you have any bug reports or queries, please contact the bot owner:\n\n" \
                              "Email: botcraftpython@gmail.com ✉️\n" \
                              "Telegram: @D2NVER0 📞"
            bot.send_message(message.chat.id, contact_message, parse_mode="Markdown")
        else:
            bot.send_photo(
                message.chat.id,
                "https://latium.org/storage/prod/kQ3d42JD/full/1000x",
                caption=
                "*⛔️ Access Denied ⛔️*\n\nYou are not joined our channel ❗️\n\nIf you want to use me,\n\nJoin our channel [@BotCraftPython](https://t.me/BotCraftPython) 👥",
                parse_mode="Markdown")
    except Exception as e:
        print("An error occurred in the contact command:", e)


@bot.message_handler(func=lambda message: True)
def invalid_message(message):
    try:
        if check_membership(message.from_user.id):
            responses = [
                "Sorry, I can't understand. Please use the available commands or ask for help. 🤔",
                "I'm sorry, I didn't get that. You can use the available commands or ask for assistance. 😅",
                "Apologies, I didn't catch that. Please use one of the provided commands or request help. 🙏"
            ]
            response = random.choice(responses)
            bot.reply_to(message, response, parse_mode="Markdown")
        else:
            bot.send_photo(
                message.chat.id,
                "https://latium.org/storage/prod/kQ3d42JD/full/1000x",
                caption=
                "*⛔️ Access Denied ⛔️*\n\nYou are not joined our channel ❗️\n\nIf you want to use me,\n\nJoin our channel [@BotCraftPython](https://t.me/BotCraftPython) 👥",
                parse_mode="Markdown")
    except Exception as e:
        print("An error occurred in the invalid_message function:", e)


if __name__ == '__main__':
    bot.polling()
