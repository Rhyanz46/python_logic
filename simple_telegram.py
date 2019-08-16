import time
import urllib.request as urllib
import json
import html
import random

from telegram.ext import Updater
from telegram.ext import CommandHandler

updater = Updater(token='token')
dispatcher = updater.dispatcher

def func1():
    my_list = ['\"this is line1\"',
        '\"this is line2\"',
        '\"this is line3\"',
        '\"this is line4\"',
        '\"this is line5\"'
        ]

    return random.choice(my_list)

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text=func1())

my_handler = CommandHandler('start', start)

dispatcher.add_handler(my_handler)

updater.start_polling()