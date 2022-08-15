from json import dumps, loads

from .variables import ENCODING, MAX_PACKAGE_LENGTH


def send_msg(data, socket):
    encoded_data = dumps(data).encode(ENCODING)  # data -> JSON -> utf-8
    socket.send(encoded_data)  # send


def get_msg(socket):
    encoded_data = socket.recv(MAX_PACKAGE_LENGTH)
    if isinstance(encoded_data, bytes):  # if data type == bytes
        json_data = (encoded_data.decode(ENCODING))  # bytes -> encoded data.json
        data = loads(json_data)  # encoded data.json -> data
        if isinstance(data, dict):  # if data type == dict
            return data
        raise ValueError
    raise ValueError
