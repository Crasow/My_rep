"""Константы"""

# Порт по умолчанию для сетевого ваимодействия
defoult_port = 7777
# IP адрес по умолчанию для подключения клиента
default_ip_address = '127.0.0.1'
# Максимальная очередь подключений
max_connnections = 5
# Максимальная длинна сообщения в байтах
max_package_length = 1024
# Кодировка проекта
encoding = 'utf-8'

# Прококол JIM основные ключи:
action = 'action'
time = 'time'
user = 'user'
account_name = 'account_name'

# Прочие ключи, используемые в протоколе
presence = 'presence'
response = 'response'
error = 'error'
