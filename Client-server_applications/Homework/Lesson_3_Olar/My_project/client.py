import json
import sys
import time
from socket import socket, AF_INET, SOCK_STREAM
from common.utils import send_msg, get_msg
from common.variables import ACTION, TIME, ABOUT_USER, USER_NAME, DEFAULT_IP, DEFAULT_PORT, PRESENCE, TEST_NAME, \
    RESPONSE, \
    ERROR, USER_AGE, TEST_AGE


def create_presence():
    presence_msg = {
        ACTION: PRESENCE,
        TIME: time.time(),
        ABOUT_USER: {
            USER_NAME: TEST_NAME,
            USER_AGE: TEST_AGE,
        }
    }
    return presence_msg


def process_response(msg):
    if RESPONSE in msg:
        if msg[RESPONSE] == 200:
            return 'All is OK'
        elif msg[RESPONSE] == 400:
            return f'You`ve got error: {msg[ERROR]}'


def main():
    try:
        if len(sys.argv) > 1:
            server_address = sys.argv[1]
        else:
            server_address = DEFAULT_IP
        if len(sys.argv) > 2:
            server_port = int(sys.argv[2])
            if server_port < 1024 or server_port > 65535:
                raise ValueError
        else:
            server_port = DEFAULT_PORT
    except ValueError:
        print('The port can only be set with number from 1024 to 65535')
        sys.exit(1)

    sock = socket(AF_INET, SOCK_STREAM)
    sock.connect((server_address, server_port))

    msg_to_server = create_presence()
    send_msg(msg_to_server, sock)
    try:
        response_from_server = process_response(get_msg(sock))
        print(response_from_server)
    except(ValueError, json.JSONDecodeError):
        print('Decoding is failed')


if __name__ == '__main__':
    main()
