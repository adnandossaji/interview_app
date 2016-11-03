import sys
import threading
import time
import sqlite3

# Create a threading.Thread class
class ServerThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self._USER_NAME = ''
        self._USER_PW = ''

    def validate(self):
        time.sleep(0.1)
        self.client_socket.send(('Username > ').encode())
        in_data = self.client_socket.recv(1024)
        self._USER_NAME = in_data.decode().rstrip()
        print('SERVER > Username :', self._USER_NAME)
        # VALIDATE USERNAME
        self.client_socket.send(('Password > ').encode())
        in_data = self.client_socket.recv(1024)
        self._USER_PW = in_data.decode().rstrip()
        print('SERVER > Password :', self._USER_PW)
        # VALIDATE PASSWORD
        # VALIDATION STATUS
        if True:
            return 1
            #return 2 # Testing
        time.sleep(0.1)

    def terminate_session(self):
        print('Terminating connection on', self.client_socket)
        sys.stdout.flush()
        for i in range(0,10):
            print('.', end = '')
            sys.stdout.flush()
            time.sleep(0.15)
        self.client_socket.close()
        print('Socket closed')
        sys.stdout.flush()

    def run(self):
        self.client_socket.send(('Welcome to the Interview Portal').encode())
        time.sleep(0.1)
        _LOGIN_STATUS = self.validate()
        if _LOGIN_STATUS == 1:
            print('User', self._USER_NAME, 'has a log in status of', str(_LOGIN_STATUS))
        else:
            print('Invalid username or password')
            self.terminate_session()
            return
        time.sleep(3)
        self.terminate_session()
