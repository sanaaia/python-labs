from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from datetime import datetime
from math import factorial as fac
from urllib.request import urlopen

import random
import locale
import json

locale.setlocale(locale.LC_ALL, 'ru')


def hello(update: Update, context: CallbackContext) -> None:
    username = update.message.chat.username
    update.message.reply_text(f'Привет @{username}')


def time(update: Update, context: CallbackContext) -> None:
    date = datetime.now().strftime('%H:%M, %d %B %Y года')
    update.message.reply_text(f'Сейчас {date}')


def binom(update: Update, context: CallbackContext) -> None:
    message = update.message.text.split(' ')
    n = int(message[1])
    k = int(message[2])
    binom = fac(n) // (fac(k) * fac(n-k))
    update.message.reply_text(f'Binom({n},{k}) = {binom}')


def cat(update: Update, context: CallbackContext) -> None:
    cats = ['100', '101', '102', '206', '207', '307', '308',
            '429', '431', '444', '450', '451', '497', '498', '499',
            '500', '501', '502', '503', '504', '521', '523', '525', '599']
    cats += [str(i) for i in range(200, 205)]
    cats += [str(i) for i in range(300, 306)]
    cats += [str(i) for i in range(400, 419)]
    cats += [str(i) for i in range(420, 427)]
    cats += [str(i) for i in range(506, 512)]
    random_index = random.randint(0, len(cats) - 1)
    update.message.reply_photo(f'https://http.cat/{cats[random_index]}.jpg')


def weather(update: Update, context: CallbackContext) -> None:
    message = update.message.text.split(' ')
    latitude = message[1]
    longitude = message[2]
    url_first = 'https://api.weather.gov/points/' + latitude + ',' + longitude
    data_first = json.loads(urlopen(url_first).read().decode())
    url_second = data_first['properties']['forecast']
    data_second = json.loads(urlopen(url_second).read().decode())
    cond = data_second['properties']['periods'][0]['shortForecast']
    temp = data_second['properties']['periods'][0]['temperature']
    update.message.reply_text(f'Сейчас: {cond} ({temp}\N{DEGREE SIGN}F)')


with open('token') as token:
    updater = Updater(token.read().strip())

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('time', time))
updater.dispatcher.add_handler(CommandHandler('binom', binom))
updater.dispatcher.add_handler(CommandHandler('cat', cat))
updater.dispatcher.add_handler(CommandHandler('weather', weather))

updater.start_polling()
updater.idle()
