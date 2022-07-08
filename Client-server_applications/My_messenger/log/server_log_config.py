import logging

# задаем формат выводимого сообщения
formatter = logging.Formatter('%(asctime)s --- %(levelname)s --- %(module) --- %(message)s')

# создаем хендлера записи в файл всех логов
all_log_hand = logging.FileHandler('server.log', encoding='utf-8')
all_log_hand.setFormatter(formatter)

server_log = logging.getLogger('server_logger')
server_log.addHandler(all_log_hand)
server_log.setLevel(logging.INFO)
