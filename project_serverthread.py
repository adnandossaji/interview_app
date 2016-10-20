import sys
import threading
import time

class ServerThread(threading.Thread):
    def __init__(self, client_connection):
        threading.Thread.__init__(self)
        self.client_connection = client_connection

    def run(self):
        while True:
            in_data = self.client_connection.recv(1024)



            
            self.client_connection.send(in_data)

        self.client_connection.close()
        guests.remove(self.client_connection)
