from interview_error import CredentialsException
import sys
import string

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
    prompt = enc.decrypt(prompt)
    answer_string=str(input(prompt))
    answer_string = enc.encrypt(answer_string)
    client_socket.send(answer_string)
    prompt=client_socket.recv(1024)
    prompt = enc.decrypt(prompt)
    answer_string=str(input(prompt))
    answer_string = enc.encrypt(answer_string)
    client_socket.send(answer_string)
#string printing loop that prints question from server and returns string answer
def startinterview():
    greeting = client_socket.recv(1024)
    greeting = enc.decrypt(greeting)
    if (len(greeting) != 0): print(greeting)
    interview_string=client_socket.recv(1024)
    interview_string = enc.decrypt(interview_string)

    while (interview_string !="End of Interview"):#keyword could be swapped out for anything
        print(interview_string)
        answer_string=str(input("Answer: "))
        answer_string = enc.encrypt(answer_string)
        client_socket.send(answer_string)
        interview_string = client_socket.recv(1024)
        interview_string = enc.decrypt(interview_string)
    print("End of Interview")

def validate(loggedInAs):
    if (len(loggedInAs) == 0):
        CredentialsException()
        return False
    print("Logged in as a", loggedInAs)
    return True

def createInterview():
    greeting = client_socket.recv(1024)
    greeting = enc.decrypt(greeting)
    if (len(greeting) != 0): print(greeting)
    interview_string=''

    while (interview_string!="End of Interview"):
        answer_string=str(input("CLIENT > "))
        answer_string = enc.encrypt(answer_string)
        client_socket.send(answer_string)
        interview_string = client_socket.recv(1024)
        interview_string = enc.decrypt(interview_string)
        print(interview_string)
        
def showInterview():
    ### code stuff###
    ###thisi funciton will take the interview ID ###
    print('YAY! you an awesome option')
    ### recieve greeting
    greeting = client_socket.recv(1024)
    greeting = enc.decrypt(greeting)
    #if (len(greeting) != 0): print(greeting)
    print(greeting)

    ###ask for interview ID
    ### id is algready requested ###
##    print('please enter an Interview ID: ')
##    sys.stdout.flush()
##    int_id = str(sys.stdin.readline())
##    int_id = enc.encrypt(int_id.rstrip())
##    client_socket.send(int_id)
    
    print('fetching interview... \nPlease wait...')

    ### recieves interview
    fetched_int = client_socket.recv(1024)
    fetched_int = enc.decrypt(fetched_int)

    print(fetched_int)
    ### prints interivew
##    while (fetched_int !="End of Interview"):#keyword could be swapped out for anything
##        print(fetched_int)
##        
##        answer_string=str(input("Answer: "))
##        answer_string = enc.encrypt(answer_string)
##        client_socket.send(answer_string)
##
##        fetched_int = client_socket.recv(1024)
##        fetched_int = enc.decrypt(fetched_int)

    print("End of Interview")
    
def lawyerOptions():
    greeting = client_socket.recv(1024)
    greeting = enc.decrypt(greeting)
    #if (len(greeting) != 0): print(greeting)
    print(greeting)
    view = "view"
    create = "create"
    
    print(loggedInAs, ' please enter an option: create OR view \n')
    sys.stdout.flush()
    option_entered = str(sys.stdin.readline())
    
    if(str(option_entered).rstrip().lower().encode() == str(create).encode()):
        c = 'c'
        c = enc.encrypt(c)
        client_socket.send(c)
        createInterview()
        #works        
    elif(str(option_entered).rstrip().lower().encode() == str(view).encode()):
        v = 'v'
        v = enc.encrypt(v)
        client_socket.send(v)
        
        print('enter an interview id to search for...')
        sys.stdout.flush()
        id_entered = str(sys.stdin.readline())
        id_entered = id_entered.rstrip()
        #send id to server#
        print(id_entered.encode())

        id_entered = enc.encrypt(id_entered)
        client_socket.send(id_entered)
        
        showInterview()
    else: print('please enter "create" or "view" next time')
        
def key_exchange():
    dif = diffieHellman()
    client_socket.send(str(dif.publicKey).encode())
    other_key = client_socket.recv(2048).decode()
    other_key = int(other_key)
    key = dif.genKey(other_key)
    return key

if __name__ == "__main__":
    import sys
    import socket
    import time
    from argparse import ArgumentParser
    from DiffieHellman import diffieHellman
    from encrypt import Encrypt
    
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
    key = key_exchange()
    enc = Encrypt(key)
    in_data = client_socket.recv(1024)
    in_data = enc.decrypt(in_data)
    print(in_data)
    credentials()
    loggedInAs = client_socket.recv(1024)
    loggedInAs = enc.decrypt(loggedInAs)
    if (validate(loggedInAs)):
        if (loggedInAs == "Interviewee"): startinterview()
        elif (loggedInAs == "Lawyer"): lawyerOptions() #createInterview()
            
    print("Logging Out...")
