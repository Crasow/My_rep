from typing import Any, Union

import telebot
from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
from pyowm.utils import timestamps
config_dict['language'] = 'ru'
owm = OWM('12ed415dc4d92d83e8a35d37881676f8')
owm.supported_languages
mgr = owm.weather_manager()

bot = telebot.TeleBot("1498401360:AAE9BfQqx2cOwR5fB3Cu_5GcXk9tn5m69Gk", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Напиши название своего города и узнай погоду на улице")


@bot.message_handler(content_types=['Погода'])
def send_echo(message): 

        observation = mgr.weather_at_place(message.text)
        w = observation.weather
        temp = w.temperature('celsius')["temp"]

        answer: Union[str, Any] = "В городе " + message.text + " сейчас " +  w.detailed_status + "\n"
        answer += "Температура сейчас примерно " + str(temp) + " °С" + "\n\n"
        if temp < 0:
            answer +=  "Там дубарь, не ходи туда. Грей лапки дома <3"
        elif temp < 20:
            answer += "Вроде терпимо, но тебе там делать нечего -_-"
        else :
            answer += "Там жарень, не одевайся сильно =D"

        bot.send_message(message.chat.id, answer )



bot.polling (none_stop = True)