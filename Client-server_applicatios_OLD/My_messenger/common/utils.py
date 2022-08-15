from json import dumps, loads

from .vars import ENCODING


def send_msg(data, socket):
    encoded_data = dumps(data).encode(ENCODING)  # data -> JSON -> utf-8
    socket.send(encoded_data)  # send


def get_msg(socket):
    encoded_data = socket.recv(1024)
    if isinstance(encoded_data, bytes):
        json_data = encoded_data.decode(ENCODING)  # data -> encoded data.json
        data = loads(json_data)  # encoded data.json -> data
        if isinstance(data, dict):
            return data
        raise ValueError
    raise ValueError
