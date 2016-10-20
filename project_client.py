import sys
import socket
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('host', type = str)
parser.add_argument('port', type = int)
args = parser.parse_args()
_HOST = socket.gethostbyname(args.host)
_PORT = args.port

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.connect((_HOST, _PORT))

client_socket.close()
server_socket.close()
