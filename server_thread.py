#! python3

import threading, server_globals
from user import User

class ServerThread( threading.Thread ):
  def __init__(self, connection):
    threading.Thread.__init__(self)
    self.connection= connection

  def signup(self, argv):
    script_name = argv[0]
    tack = argv[1]

    if tack == "--signup":

      try:

        username = str(argv[3])
        password = str(argv[5])

        user = User(username, password)

        user.signup()

        print( 'relaying message...' )
        for current_connection in server_globals.connections:
          # if current_connection is not self.connection:
          current_connection.send("Account Created!\n".encode())

      except:
        for current_connection in server_globals.connections:
            # if current_connection is not self.connection:
          current_connection.send("Username already exists!\n".encode())
        raise

  def chat(self, argv):
    script_name = argv[0]
    tack = argv[1]

    if tack == "--chat":
      print("Chat here!")
    
  def run(self):

    while True:
      # wait for a message from this connection
      print( 'waiting for message...' )
      msg_bytes= self.connection.recv(1024)
      if len(msg_bytes):
        print( 'received: ' + msg_bytes.decode(), end= '\n' )
      else: # no bytes received
        print( 'received no bytes; closing socket...' )
        self.connection.close()
        # remove the connection from the list
        server_globals.connections.remove( self.connection )
        break

      client_argv = msg_bytes.decode().split(" ")

      tack = client_argv[1]

      return {
        '--signup': self.signup(client_argv),
        '--chat': self.chat(client_argv)
      }[tack]
      
      # # relay the message to all other connections
      # print( 'relaying message...' )
      # for current_connection in server_globals.connections:
      #   # if current_connection is not self.connection:
      #   current_connection.send(msg_bytes)
