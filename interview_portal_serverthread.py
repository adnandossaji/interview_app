import sys
import threading
import time
import sqlite3
import db_interaction
import user
import interview
import answer
import question
import active_interview
from interview_error import CredentialsException

# Create a threading.Thread class
class ServerThread(threading.Thread):
    def __init__(self, client_socket):
        threading.Thread.__init__(self)
        self.client_socket = client_socket
        self._USER_NAME = ''
        self._USER_PW = ''
        self.currentuser=None
    ##################################################
    ##Helper function for giveInterview. Handles all##
    ##looping needed to assure a correct response   ##
    ##################################################
    def sendQuestion(self,messagestring,sendAnswers):
        correct=False
        error=False
        while correct==False:
            self.client_socket.send(messagestring.encode())
            response=self.client_socket.recv(1024).decode()
            print(response)
            for tup in sendAnswers:
                print(tup[2],"is", response)
                if response == tup[2]:
                    correct = True
                    return response
                elif error==False:
                    error=True
                    messagestring="\nINVALID RESPONSE\nPlease enter a letter exactly as it appears above\n"+messagestring


        return response

        #############################################################
        ##Gives the interview by getting the question data, storing##
        ##it in tuples, and sending the question as text. Once a   ##
        ##response is received, it validates the response and then ##
        ##sends another question. Answer data is stored in tuples. ##
        ##Uses key phrase to end the interview                     ##
        ## -Brandon M                                              ##
        #############################################################
    def giveInterview(self):
        answerlist=[]
        i=1
        currentinterview=db_interaction.getInterview(self.currentuser.getIntID())
        greetingString="Welcome to your interview!\n"+currentinterview.getInterviewName()
        self.client_socket.send(greetingString.encode())
        currentQuestion=currentinterview.getNextQuestion()
        while currentQuestion != "End of Interview":
            answers=currentQuestion.getAnswers()
            sendAnswers=[]
            firstletter='A'
            for a in answers:
                sendAnswers.append((a.getAnswerText(),a.getAnswerID(),firstletter))
                firstletter=chr(ord(firstletter)+1)
            messagestring="\n"+currentQuestion.getQuestionText()+"\n"
            for tup in sendAnswers:
                messagestring=messagestring+str(tup[2])+": "+str(tup[0])+"\n"
            response=self.sendQuestion(messagestring,sendAnswers)
            responseID=""
            for tup in sendAnswers:
                if tup[2]==response:
                    responseID=tup[1]
            #currentinterview.answerQuestion(responseID)
            currentQuestion=currentinterview.getNextQuestion()
        self.client_socket.send("End of Interview".encode())
        return

    def createInterview(self):
        greetingString="Welcome to the interview creator!\n"
        self.client_socket.send(greetingString.encode())

        askQuestionString="What is the name of this interview?"
        self.client_socket.send(askQuestionString.encode())

        name = self.client_socket.recv(1024).decode()
        interview = ActiveInterview()
        print(name)
        questions = []
        answers = []

        nextQ = True
        nextA = True

        while (nextQ):
            msg="Please type a QUESTION?"
            self.client_socket.send(msg.encode())
            question = self.client_socket.recv(1024).decode()
            questions.append(question + "?")
            print(question)
            while(nextA):
                msg="Please type an ANSWER?\n"
                self.client_socket.send(msg.encode())

                answer = self.client_socket.recv(1024).decode()

                answers.append(answer)
                print(answer)

                check = True

                while(check):

                    msg="Would you like to add another ANSWER (Y/N)?\n"
                    self.client_socket.send(msg.encode())

                    checker = self.client_socket.recv(1024).decode()

                    if (checker == 'Y'):
                        check = False
                        nextA = True
                    elif (checker == 'N'):
                        check = False
                        nextA = False
                        print("1")
                    else:
                        msg="Invalid Response?\n"
                        self.client_socket.send(msg.encode())
                        check = True

            nextA = True
            check2 = True

            while(check2):

                msg="Would you like to add another QUESTION (Y/N)?\n"
                self.client_socket.send(msg.encode())
                checker = self.client_socket.recv(1024).decode()

                if (checker == 'Y'):
                    check2 = False
                    nextQ = True
                elif (checker == 'N'):
                    check2 = False
                    nextQ = False
                else:
                    msg="Invalid Response?\n"
                    self.client_socket.send(msg.encode())
                    check = True

        msg = "End of Interview"
        self.client_socket.send(msg.encode())

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

        ###Checks to make sure that user is in the database###
        self.currentuser = db_interaction.getUser(self._USER_NAME,self._USER_PW)
        if self.currentuser!= None:
            return True
        return False
        time.sleep(0.1)

    def terminate_session(self):
        print('Terminating connection on', self.client_socket)
        sys.stdout.flush()
        for i in range(0,10):
            print('.', end='')
            sys.stdout.flush()
            time.sleep(0.15)
        self.client_socket.close()
        print('Socket closed')
        sys.stdout.flush()

    def run(self):
        self.client_socket.send(('Welcome to the Interview Portal').encode())
        time.sleep(0.1)
        _LOGIN_STATUS = self.validate()
        if _LOGIN_STATUS == True:
            print('User', self._USER_NAME, 'has a log in status of', str(_LOGIN_STATUS))
        else:
            CredentialsException()
            self.terminate_session()
            return
        ##This assumes that the user is trying to take an interview. Additional##
        ##user options could be added easily by making the giveInterview call  ##
        ##conditional

        self.client_socket.send(('{}'.format(db_interaction.getUserRole(self.currentuser.getPer()))).encode())

        if (self.currentuser.getPer() == 4): self.giveInterview()
        elif (self.currentuser.getPer() == 2): self.createInterview()

        self.terminate_session()
