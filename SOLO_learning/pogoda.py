from pyowm import OWM
from pyowm.utils import config
from pyowm.utils.config import get_default_config
config_dict = get_default_config()
from pyowm.utils import timestamps
config_dict['language'] = 'ru'
owm = OWM('12ed415dc4d92d83e8a35d37881676f8')
owm.supported_languages
mgr = owm.weather_manager()

town = input ("Введи название города:\n")
# Search for current weather in London (Great Britain) and get details
observation = mgr.weather_at_place(town)
w = observation.weather

temp = w.temperature('celsius')["temp"]
 
print("В городе " + town + " сейчас " +  w.detailed_status)
print( "Температура сейчас примерно " + str(temp) + " °С")

if temp < 0:
	print ( "Там дубарь, не ходи туда. Грей лапки дома <3")
elif temp < 20:
	print ("Вроде терпимо, но тебе там делать нечего -_-")
else :
    print ("Там жарень, не одевайся сильно =D")
a = input ()