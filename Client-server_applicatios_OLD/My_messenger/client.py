import json
import logging
import sys
import time
import log.client_log_config
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_msg, send_msg
from common.vars import PORT, IP, GUEST, STATUS_HERE, PRESENCE, \
    RESPONSE, ERROR

# Создание объект логгера у клиента
logger = logging.getLogger('client.logger')


def presence(acc_login, status):
    data = {
        "action": PRESENCE,
        "time": time.time(),
        "user": {
            "account_login": acc_login,
            "status": status
        },
    }
    return data


def process_ans(data):
    logger.info('Processing answer from the server...')
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
        logger.error('Port can be a number only in range from 1024 to 65535')
        sys.exit(1)

    client = socket(AF_INET, SOCK_STREAM)  # Создание сокета TCP
    client.connect((server_address, server_port))
    logger.info('Connecting succeeded')

    send_msg(presence(GUEST, STATUS_HERE), client)  # Отправка серверу присутствие
    logger.info('Message to server sended')

    try:
        response = process_ans(get_msg(client))  # Получение ответа
        logger.info(f'Received a response from the server: TI PIDOR')
    except (ValueError, json.JSONDecodeError):
        logger.error('Failed to decode data from the server')


if __name__ == '__main__':
    main()
