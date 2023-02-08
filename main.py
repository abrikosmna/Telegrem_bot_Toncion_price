import requests
from datetime import datetime
import telebot
from Token import token
from Token import ID
import schedule


def get_data():
    req = requests.get("https://yobit.net/api/3/ticker/toncoin_rur")
    response = req.json()
    sell_price = response["ton_rur"]["sell"]
    print(f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell Ton price: {sell_price}")


bot = telebot.TeleBot(token)
id = ID

def send_text():
    id = ID
    try:
        req = requests.get("https://yobit.net/api/3/ticker/toncoin_rur")
        response = req.json()
        sell_price = response["toncoin_rur"]["sell"]
        bot.send_message(
            id,
            f"{datetime.now().strftime('%Y-%m-%d %H:%M')}\nSell Ton price: {sell_price}"
                )
        

    except Exception as ex:
        print(ex)
        bot.send_message(
            id,
            "Damn...Something was wrong..."
                )



def main():
    schedule.every().day.at('09:00').do(send_text)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    # get_data()
    main()

