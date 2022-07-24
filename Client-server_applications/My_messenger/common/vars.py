import socket
import sys
import os
sys.path.append(os.path.join(os.getcwd(), '..'))
PORT = 7777

IP = (socket.gethostbyname(socket.gethostname()))
print (socket.gethostbyname(socket.gethostname()))

ENCODING = 'utf-8'

# Протокол JIM
ACTION = 'action'
TIME = 'time'
USER = 'user'
ACC_LOGIN = 'account_login'
ACC_PASS = 'account_password'

# other
PRESENCE = 'presence'
AUTHENTICATE = 'authenticate'
GUEST = 'guest'
GUEST_PASS = 1234
RESPONSE = 'response'
ERROR = 'error'
STATUS_HERE = 'all right'
STATUS = 'status'