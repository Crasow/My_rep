import logging
import os
import sys
sys.path.append('../')

# задаем формат выводимого сообщения
formatter = logging.Formatter('%(asctime)s --- %(levelname)s --- %(filename)s --- %(message)s')

# Путь для файла с логами
path = os.path.dirname(os.path.abspath(__file__))

# создаем хендлера записи в файл всех логов
all_log_hand = logging.FileHandler(path + '\\client.log', encoding='utf-8')
all_log_hand.setFormatter(formatter)

server_log = logging.getLogger('client.logger')
server_log.addHandler(all_log_hand)
server_log.setLevel(logging.INFO)
