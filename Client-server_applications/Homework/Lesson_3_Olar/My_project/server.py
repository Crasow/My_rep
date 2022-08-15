import json
import sys
from socket import AF_INET, SOCK_STREAM, socket
from common.variables import DEFAULT_PORT, DEFAULT_IP, MAX_CONNECTIONS, \
    USER_NAME, ACTION, PRESENCE, TIME, ABOUT_USER, RESPONSE, ERROR, TEST_NAME, USER_AGE
from common.utils import get_msg, send_msg


def process_client_msg(msg):
    if ACTION in msg and msg[ACTION] == PRESENCE and TIME in msg \
            and ABOUT_USER in msg and msg[ABOUT_USER][USER_NAME] == TEST_NAME and msg[ABOUT_USER][USER_AGE] > 18:
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def main():
    try:
        if '-v' in sys.argv:
            listen_address = sys.argv[sys.argv.index('-v') + 1]
        else:
            listen_address = DEFAULT_IP
    except IndexError:
        print('In parameter \'-v\' you need to enter address for server')
        sys.exit(1)

    try:
        if '-p' in sys.argv:
            listen_port = int(sys.argv[sys.argv.index('-p') + 1])
        else:
            listen_port = DEFAULT_PORT
        if listen_port < 1024 or listen_port > 65535:
            raise ValueError
    except IndexError:
        print('In parameter \'-p\' you need to enter port')
        sys.exit(1)
    except ValueError:
        print('You can enter as port only numbers from 1024 to 65535')
        sys.exit(1)

    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind((listen_address, listen_port))
    print(f'Server started on IP: {listen_address} and PORT: {listen_port}')
    sock.listen(MAX_CONNECTIONS)

    while True:
        client, client_address = sock.accept()
        try:
            msg_from_client = get_msg(client)
            print(msg_from_client, f'\nAll is OK    , {msg_from_client[ABOUT_USER][USER_NAME]} is {msg_from_client[ABOUT_USER][USER_AGE]} years old. He is mature')
            response = process_client_msg(msg_from_client)
            send_msg(response, client)
            client.close()
        except (ValueError, json.JSONDecodeError):
            print('Something wrong in client message')
            client.close()


if __name__ == '__main__':
    main()
