#! python3

# from argparse import ArgumentParser

import sys, socket, server_globals
from server_thread import ServerThread

def usage( script_name ):
  print( 'Usage: py ' + script_name + ' <port number>' )

def main():

  # parser = ArgumentParser()
  # parser.add_argument('host', type = str)
  # parser.add_argument('port', type = int)
  # args = parser.parse_args()
  # _HOST = socket.gethostbyname(args.host)
  # _PORT = args.port

  # server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  # server_socket.bind((_HOST, _PORT))
  # server_socket.listen(5)

  # while True:
  #   client_socket, client_address = server_socket.accept()
  #   ServerThread(client_socket).start()

  # client_socket.close()
  # server_socket.close()

  argc= len( sys.argv )
  if argc != 2 :
    usage( sys.argv[0] )
    sys.exit()
  # create a server object
  serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  serversocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
  serversocket.bind(('localhost', int(sys.argv[1])))
  serversocket.listen(5)
  print( 'waiting for connections on port ' + sys.argv[1] + ' ...' )
  while True:
    # wait for a connection and accept it
    sock, addr= serversocket.accept()
    # add the connection to a list
    server_globals.connections.append(sock)
    # start a new thread to handle the connection
    ServerThread(sock).start()

if __name__ == "__main__":
  main()