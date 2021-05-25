import telebot
from decouple import config
import requests
from bs4 import BeautifulSoup

TOKEN = '1826011151:AAELB4qxSxg-GxMVoUnwJnWaaKY_V7eqO1o'
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'привет, я бот')


@bot.message_handler(content_types=['text'])
def text(message):
    if message.text.lower() == "хэй":
        bot.send_message(message.chat.id, 'Хэй')


bot.polling()