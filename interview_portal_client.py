def terminate_session():
    print('Terminating connection to server')
    for i in range(0,10):
        print('.', end = '')
        sys.stdout.flush()
        time.sleep(0.1)
    client_socket.close()
    print('Server socket closed')
    return

def credentials():
    for i in range(0,2):
        in_data = client_socket.recv(1024)
        print(in_data.decode(), end = '')
        sys.stdout.flush()
        out_data = sys.stdin.readline()
        client_socket.send(out_data.encode())
        time.sleep(0.01)

if __name__ == "__main__":
    import sys
    import socket
    import time
    from argparse import ArgumentParser

    parser = ArgumentParser(description = 'CSC 376 Final Project : Interview Portal')
    parser.add_argument('host', type = str, help = 'Host Address of the Server')
    parser.add_argument('port', type = int, help = 'Port used to connect to Server')
    args = parser.parse_args()
    #_HOST = socket.gethostbyname(args.host)
    #_PORT = args.port
    _HOST = 'localhost'
    _PORT = 55555

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((_HOST, _PORT))
    in_data = client_socket.recv(1024)
    print(in_data.decode())

    credentials()
