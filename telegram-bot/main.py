from telegram.ext import Updater
import os

BOT_USERNAME = "bazar22Bot"

def get_env_var(ENV):
    return os.environ[ENV]

"""
export TELEGRAM_ACCESS_TOKEN="1924609853:AAFAbWVcSNs-0PlQi1YQr-Wz5EGrr9LHve0"
"""

updater = Updater(token=get_env_var("TELEGRAM_ACCESS_TOKEN"), use_context=True)
dispatcher = updater.dispatcher

import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

from telegram.ext import CommandHandler
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()
