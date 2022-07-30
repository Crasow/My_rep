import json
import logging
import log.server_log_config
from socket import socket, AF_INET, SOCK_STREAM

from common.utils import get_msg, send_msg
from common.vars import PORT, IP, ACTION, TIME, \
    USER, ACC_LOGIN, GUEST, RESPONSE, ERROR, STATUS, STATUS_HERE

# Создание объект логгера на сервере
logger = logging.getLogger('server.logger')

# Тестим всякую дрянь
def data_check(data):
    logger.info(f'Started to check message from client')
    if ACTION in data and TIME in data and USER in data \
            and data[USER][ACC_LOGIN] == GUEST \
            and data[USER][STATUS] == STATUS_HERE:
        logger.info(f'Data check succeeded')
        return {RESPONSE: 200}
    else:
        logger.error(f'One of the required values {data.keys()} is wrong')
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }


def main():
    server = socket(AF_INET, SOCK_STREAM)  # Создание сокета TCP

    server.bind((IP, PORT))  # Закрепление серва на айпи и порте

    qty_to_listen = 10
    server.listen(qty_to_listen)  # Открытие сервера на 10 одновременных подключений
    logger.info(f'\n\n'+'-'*110+'\n')
    logger.info(f'The server started it`s work at {IP} : {PORT} \n'
                f'and ready to listen at once {qty_to_listen} clients')
    while True:
        client, client_address = server.accept()
        logger.info(f'New client connected from the address {client_address} ')
        try:
            data_from_client = get_msg(client)
            answer_to_client = data_check(data_from_client)
            send_msg(answer_to_client, client)
            logger.info(f'Messaging ended')
        except (ValueError, json.JSONDecodeError):
            logger.error('Incorrect message received from client')
            client.close()


if __name__ == '__main__':
    main()
