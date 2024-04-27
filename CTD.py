import telebot
from telebot import types
from telebot import *

base ={
     "Высокий приоритет":"",
     "Средний приоритет":"",
     "Низкий приоритет":""
}


bot = telebot.TeleBot('TOKEN')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Добавить задачи")
    btn2 = types.KeyboardButton("Удалить задачу")
    btn3 = types.KeyboardButton("Посмотреть задачи")
    markup.add(btn1)
    markup.add(btn2)
    markup.add(btn3)
    bot.send_message(message.from_user.id, "Добро пожаловать в CTD", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def tasks(message):
     if message.text == "Добавить задачи":
          msg = bot.send_message(message.from_user.id, "Задача высокого приоритета")
          bot.register_next_step_handler(msg, high_priority)
     if message.text == "Посмотреть задачи":
          bot.send_message(message.from_user.id, f"Задача высокого приоритета: {base['Высокий приоритет']} \nЗадача среднего приоритета: {base['Средний приоритет']} \nЗадача низкого приоритета: {base['Низкий приоритет']}")

def high_priority (message):
     base["Высокий приоритет"] = message.text
     msg = bot.send_message(message.from_user.id, "Задача среднего приоритета")
     bot.register_next_step_handler(msg, medium_priority)

def medium_priority(message):
     base["Средний приоритет"] = message.text
     msg = bot.send_message(message.from_user.id, "Задача низкого приоритета")
     bot.register_next_step_handler(msg, low_priority)

def low_priority(message):
     base["Низкий приоритет"] = message.text
     bot.send_message(message.from_user.id, f"Задача высокого приоритета: {base['Высокий приоритет']} \nЗадача среднего приоритета: {base['Средний приоритет']} \nЗадача низкого приоритета: {base['Низкий приоритет']}")
     bot.clear_step_handler(message)
   
     
bot.polling(none_stop=True)
