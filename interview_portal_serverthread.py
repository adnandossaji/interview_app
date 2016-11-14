import sys
import threading
import time
import sqlite3
import db_interaction
import user
import interview
import answer

# Create a threading.Thread class
class ServerThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self._USER_NAME = ''
        self._USER_PW = ''
        self.currentuser=None
    def sendQuestion(self,messagestring,sendAnswers):
        correct=False
        while correct==False:
            self.client_socket.send(messagestring.encode())
            response=self.client_socket.recv(1024).decode()
            print(response)
            for tup in sendAnswers:
                print(tup[2],"is", response)
                if response == tup[2]:
                    correct = True
                    return response

        return response
    def giveInterview(self):
        answerlist=[]
        i=1
        currentinterview=db_interaction.getInterview(self.currentuser.getIntID())
        greetingString="Welcome to your interview!\n"+currentinterview.getInterviewName()+"\n"
        self.client_socket.send(greetingString.encode())
        currentQuestion=currentinterview.getNextQuestion()
        while currentQuestion != "End of Interview":
            answers=currentQuestion.getAnswers()
            sendAnswers=[]
            firstletter='A'
            for a in answers:
                sendAnswers.append((a.getAnswerText(),a.getAnswerID(),firstletter))
                firstletter=chr(ord(firstletter)+1)
            messagestring=currentQuestion.getQuestionText()+"\n"
            for tup in sendAnswers:
                messagestring=messagestring+str(tup[2])+": "+str(tup[0])+"\n"
            response=self.sendQuestion(messagestring,sendAnswers)
            print("We made it!")
            currentQuestion=currentinterview.getNextQuestion()
        return

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
        self.currentuser=db_interaction.getUser(self._USER_NAME,self._USER_PW)
        if self.currentuser!= None:
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
        self.giveInterview()


        self.terminate_session()
