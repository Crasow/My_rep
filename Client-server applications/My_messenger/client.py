import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_msg, send_msg
from common.vars import PORT, IP, GUEST, STATUS_HERE, PRESENCE, \
    RESPONSE, ERROR


def presence(acc_login=GUEST, status_here=STATUS_HERE):
    data = {
        "action": PRESENCE,
        "time": time.time(),
        "user": {
            "account_login": acc_login,
            "status": status_here
        },
    }
    return data


def process_ans(data):
    if RESPONSE in data:
        if data[RESPONSE] == 200:
            return '200 : OK'
        return f'400 : {data[ERROR]}'


def main():
    # Подключение к серверу
    try:
        server_address = IP
        server_port = PORT
        if PORT < 1024 or PORT > 65535:
            raise ValueError
    except ValueError:
        print('Порт может быть только цифрой от 1024 до 65535.')
        sys.exit(1)

    client = socket(AF_INET, SOCK_STREAM)  # Создание сокета TCP
    client.connect((server_address, server_port))

    send_msg(presence(), client)  # Отправка серверу присутствие

    try:
        server_data = process_ans(get_msg(client))  # Получение ответа
        print(server_data)
    except (ValueError, json.JSONDecodeError):
        print('Не удалось декодировать сообщение сервера.')


if __name__ == '__main__':
    main()
