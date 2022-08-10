import logging.handlers
import os
import sys
sys.path.append('../')

# задаем формат выводимого сообщения
formatter = logging.Formatter('%(asctime)s --- %(levelname)s --- %(filename)s --- %(message)s')

# Путь для файла с логами
path = os.path.dirname(os.path.abspath(__file__))


# создаем хендлера записи в файл всех логов
all_log_hand = logging.handlers.TimedRotatingFileHandler(path+'\\server.log',
                                                         encoding='utf-8',
                                                         when='D',
                                                         interval=1,
                                                         backupCount=10)
all_log_hand.setFormatter(formatter)
# all_log_hand.setLevel(logging.INFO)

server_log = logging.getLogger('server.logger')
server_log.addHandler(all_log_hand)
server_log.setLevel(logging.INFO)

