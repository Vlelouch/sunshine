import logging
from telegram.ext import *
import responses
from flask import Flask, request
import os

API_KEY = '1940733414:AAEffQ_4SFUVttv47qnwzkzLlQpFEGMDsVA'
server = Flask(__name__)

# Set up the logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logging.info('Starting Bot...')


def start_command(update, context):
    update.message.reply_text('Hello there! I\'m a bot. What\'s up?')


def help_command(update, context):
    update.message.reply_text('Try typing anything and I will do my best to respond!')


def custom_command(update, context):
    update.message.reply_text('This is a custom command, you can add whatever text you want here.')


def handle_message(update, context):
    text = str(update.message.text).lower()
    logging.info(f'User ({update.message.chat.id}) says: {text}')

    # Bot response
    response = responses.get_response(text)
    update.message.reply_text(response)


def error(update, context):
    # Logs errors
    logging.error(f'Update {update} caused error {context.error}')


# Run the programme
@server.route('/' + API_KEY, methods=['POST'])
def getMessage():
    json_string = request.get_data().decode('utf-8')
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://mysterious-oasis-84536.herokuapp.com/' + API_KEY)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))