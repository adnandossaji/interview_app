from interview_error import CredentialsException

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
    greeting = client_socket.recv(1024).decode()
    if (len(greeting) != 0): print(greeting)
    interview_string=client_socket.recv(1024)

    while (interview_string.decode()!="End of Interview"):#keyword could be swapped out for anything
        print(interview_string.decode())
        answer_string=str(input("Answer: "))
        client_socket.send(answer_string.encode())
        interview_string=client_socket.recv(1024)
    print("End of Interview")

def validate(loggedInAs):
    if (len(loggedInAs) == 0):
        CredentialsException()
        return False
    print("Logged in as a", loggedInAs)
    return True

def createInterview():
    greeting = client_socket.recv(1024).decode()
    if (len(greeting) != 0): print(greeting)
    interview_string=''

    while (interview_string!="End of Interview"):
        answer_string=str(input("CLIENT > "))
        client_socket.send(answer_string.encode())
        interview_string=client_socket.recv(1024).decode()
        print(interview_string)
        
def key_exchange():
    dif = diffieHellman()
    client_socket.send(str(dif.publicKey).encode())
    other_key = client_socket.recv(2048).decode()
    other_key = int(other_key)
    key = dif.genKey(other_key)
    return key

def showInterview():
### code to pulling interview and putting it on the screen -KC ###

	## code stuff ##
	## don't forget to encode! ##
	
	greeting = client_socket.recv(1024).decode()
	if (len(greeting) != 0): 
		print(greeting) 
	#ask/ get InterviewID to look up#
	print('Please enter an interview ID: ')
	sys.stdout.flush()	
	### get interviewID here. need to send to the server -KC ###
	interviewID_string = sys.stdin.readline()
	interview_string = ''
	
	### recieves and prints out interview here -KC ###
	
	while (interview_string !="End of Interview"):#keyword could be swapped out for anything
            print(interview_string.decode())
            answer_string=str(input("Answer: "))
            client_socket.send(answer_string.encode())
            interview_string=client_socket.recv(1024)
            print('End of Interview')

###this function works###        
def lawyer_options(option):
### created function to chose create or view an interview -KC ###
	if (option.lower() == "create"):
		createInterview()
	elif (option.lower() == "view"):
	### ask for interview ID then go to showInterview() -KC ###
		showInterview()
	else:
		print('That was not a valid option. Please try again some other time.')
	
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
    in_data = client_socket.recv(1024)
    print(in_data.decode())
    key = key_exchange()
    enc = Encrypt(key)
    credentials()
    loggedInAs = client_socket.recv(1024).decode()
    if (validate(loggedInAs)):
        if (loggedInAs == "Interviewee"): startinterview()
        elif (loggedInAs == "Lawyer"): # createInterview()
        
        ### add viewInterview option here -KC ###
            ###this part works ###
                print(loggedInAs, ' please enter and option: create OR view:\n', end='') 
                ### recieves option chosen. sends to server ### 
                sys.stdout.flush()
                option_entered = sys.stdin.readline()
                ### next line not needed ###
              #  if (option_entered != ''): print('Please try again')
                
                lawyer_options(option_entered)
                
			
    print("Logging Out...")
