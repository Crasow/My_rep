import json
from socket import socket, AF_INET, SOCK_STREAM

from utils import get_msg, send_msg
from vars import PORT, IP, ACTION, TIME, \
    USER, ACC_LOGIN, GUEST, RESPONSE, ERROR, STATUS, STATUS_HERE


def data_check(data):
    if ACTION in data and TIME in data and USER in data \
            and data[USER][ACC_LOGIN] == GUEST \
            and data[USER][STATUS] == STATUS_HERE:
        return {RESPONSE: 200}
    else:
        return {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        }


def main():
    server = socket(AF_INET, SOCK_STREAM)  # Создание сокета TCP

    server.bind((IP, PORT))  # Закрепление серва на айпи и порте

    server.listen(10)  # Открытие сервера на 10 одновременных подключений

    while True:
        client, client_address = server.accept()
        try:
            data_from_client = get_msg(client)
            print(data_from_client)
            answer_to_client = data_check(data_from_client)
            send_msg(answer_to_client, client)
        except (ValueError, json.JSONDecodeError):
            print('Принято некорретное сообщение от клиента.')
            client.close()


if __name__ == '__main__':
    main()
