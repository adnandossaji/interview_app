import sys
import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('host', type = str)
parser.add_argument('port', type = int)
args = parser.parse_args()
_HOST = socket.gethostbyname(args.host)
_PORT = args.port

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((_HOST, _PORT))
server_socket.listen(5)

while True:
    client_socket, client_address = server_socket.accept()
    ServerThread(client_socket).start()

client_socket.close()
server_socket.close()
