import socket

DEFAULT_PORT = 7777
DEFAULT_IP = (socket.gethostbyname(socket.gethostname()))

MAX_CONNECTIONS = 5
MAX_PACKAGE_LENGTH = 1024
ENCODING = 'utf-8'

# Протокол JIM
ACTION = 'action'
TIME = 'time'
ABOUT_USER = 'about user'
USER_NAME = 'user name'
TEST_NAME = 'user'
USER_AGE = 'user age'
TEST_AGE = 19

# other
PRESENCE = 'presence'
RESPONSE = 'response'
ERROR = 'error'
