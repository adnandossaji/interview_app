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
    prompt=client_socket.recv(1024)
    answer_string=str(input(prompt.decode()))
    client_socket.send(answer_string.encode())
    prompt=client_socket.recv(1024)
    answer_string=str(input(prompt.decode()))
    client_socket.send(answer_string.encode())
#string printing loop that prints question from server and returns string answer
def startinterview():
    print(client_socket.recv(1024).decode())
    interview_string=client_socket.recv(1024)
    while (interview_string!="endinterview"):#keyword could be swapped out for anything
        print(interview_string.decode())
        answer_string=str(input("Answer: "))
        client_socket.send(answer_string.encode())
        interview_string=client_socket.recv(1024)
    return

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
    startinterview()
