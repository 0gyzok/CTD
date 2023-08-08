import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot('token')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить задачи")
    btn2 = types.KeyboardButton("Удалить задачу")
    markup.add(btn1)
    markup.add(btn2)
    bot.send_message(message.from_user.id, "Добро пожаловать в CTD", reply_markup=markup)

    user = bot.get_me()
    userid = user.id

bot.polling(none_stop=True, interval=0)