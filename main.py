from datetime import datetime
import telebot
from telebot import types
from Token import token
import requests


bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("$ USD")
    btn2 = types.KeyboardButton("TON")
    btn3 = types.KeyboardButton("₿ BTN")
    btn4 = types.KeyboardButton("¥ CNY")
    markup.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id,
                     text="Привет, {0.first_name}! Выбери валюту курс которой хочешь узнать".format(message.from_user),
                     reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    if (message.text == "$ USD"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("$ USD")
        btn2 = types.KeyboardButton("TON")
        btn3 = types.KeyboardButton("₿ BTN")
        btn4 = types.KeyboardButton("¥ CNY")
        btn5 = types.KeyboardButton("Вернуться к выбору валют")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        get_price("usd_rur", "USD", message)
    elif (message.text == "TON"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("$ USD")
        btn2 = types.KeyboardButton("TON")
        btn3 = types.KeyboardButton("₿ BTN")
        btn4 = types.KeyboardButton("¥ CNY")
        btn5 = types.KeyboardButton("Вернуться к выбору валют")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        get_price("toncoin_rur", "TON", message)

    elif (message.text == "₿ BTN"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("$ USD")
        btn2 = types.KeyboardButton("TON")
        btn3 = types.KeyboardButton("₿ BTN")
        btn4 = types.KeyboardButton("¥ CNY")
        btn5 = types.KeyboardButton("Вернуться к выбору валют")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        get_price("btn_rur", "BTN", message)

    elif message.text == "¥ CNY":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("$ USD")
        btn2 = types.KeyboardButton("TON")
        btn3 = types.KeyboardButton("₿ BTN")
        btn4 = types.KeyboardButton("¥ CNY")
        btn5 = types.KeyboardButton("Вернуться к выбору валют")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        get_price("cny_rur", "CNY", message)

    elif (message.text == "Вернуться к выбору валют"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("$ USD")
        btn2 = types.KeyboardButton("TON")
        btn3 = types.KeyboardButton("₿ BTN")
        btn4 = types.KeyboardButton("¥ CNY")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         text="Выбери валюту курс которой хочешь узнать".format(
                             message.from_user),
                         reply_markup=markup)
    else:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot.send_message(message.chat.id,
                         text="На такую комманду я не запрограммировал..",
                         reply_markup=markup)


def get_price(currency, currency_name, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    req = requests.get(f"https://yobit.net/api/3/ticker/{currency}")
    response = req.json()
    sell_price = response[currency]["sell"]
    bot.send_message(
        message.chat.id,
        f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell {currency_name} price: {sell_price}",
        reply_markup=markup
    )

if __name__ == '__main__':
    bot.polling(none_stop=True)


