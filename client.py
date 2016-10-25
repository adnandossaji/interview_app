#! python3

# from argparse import ArgumentParser

import sys, socket

def usage( script_name, tack ):
  switch = {
    '--signup': 'Usage: py ' + script_name + ' --signup -u <username> -p <password> -P <port number>',
    '--chat': 'Usage: py ' + script_name + ' --chat <port number>',
  }

  return print(switch.get(tack))

def chat(argv):
  script_name = argv[0]
  tack = argv[1]

  if argv[1] == "--chat":

    argc= len( argv )
    if argc != 2 :
      usage(script_name, tack)
      sys.exit()
    # create a communicator object
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', int(argv[1])))

    while True:
      # read a message from standard input
      print( 'Enter a message: ', end= '' )
      sys.stdout.flush()
      message= sys.stdin.readline()
      if not message:
        break
      # transmit the message as bytes (which is what send/recv uses)
      #print( 'attempting to send message using utf-8 encoding ...' )
      sock.send( message.encode() )
      # receive the return message from the server
      print( 'Waiting for message...' )
      return_msg= sock.recv( 1024 )
      print( 'Received: ' + return_msg.decode(), end= '' )
    print( 'Closing socket...' )
    sock.close()

def signup(argv):
  script_name = argv[0]
  tack = argv[1]

  if tack == "--signup":

    argc = len( sys.argv )
    
    if argc != 8 : return usage(script_name, tack)
    if argv[2] != "-u": return usage(script_name, tack)
    if argv[4] != "-p": return usage(script_name, tack)
    if argv[6] != "-P": return usage(script_name, tack)

    username = str(argv[3])
    password = str(argv[5])
    port = int(argv[7])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(('localhost', port))

    sock.send( " ".join(argv).encode() )

    print( 'Waiting for message...' )
    return_msg = sock.recv( 1024 )

    print( 'Received: ' + return_msg.decode(), end= '' )

    if return_msg == str:

      print( 'Closing socket...' )
      sock.close()



def main():
  tack = sys.argv[1]

  return {
    '--signup': signup(sys.argv),
    '--chat': chat(sys.argv)
  }[tack]

  # parser = ArgumentParser()
  # parser.add_argument('host', type = str)
  # parser.add_argument('port', type = int)
  # args = parser.parse_args()
  # _HOST = socket.gethostbyname(args.host)
  # _PORT = args.port

  # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  # server_socket.connect((_HOST, _PORT))

  # client_socket.close()
  # server_socket.close()


if __name__ == "__main__":
  main()