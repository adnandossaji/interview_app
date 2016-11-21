import sys
import threading
import time
import sqlite3
import db_interaction
import user
import interview
from answer import *
from question import *
from active_interview import *
import logging
import logging.config
logger = logging.getLogger(__name__)
from interview_error import CredentialsException
from encrypt import Encrypt
from DiffieHellman import diffieHellman

enc = ""


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
        global enc
        correct=False
        error=False
        while correct==False:
            messagestring = enc.encrypt(messagestring)
            self.client_socket.send(messagestring)
            messagestring = enc.decrypt(messagestring)
            response=self.client_socket.recv(1024)
            response = enc.decrypt(response)
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
        global enc
        answerlist=[]
        i=1
        currentinterview=db_interaction.getInterview(self.currentuser.getIntID())
        logger.info('User {} started interview {}'.format(self.currentuser.getName(), self.currentuser.getIntID()))
        greetingString="Welcome to your interview!\n"+currentinterview.getInterviewName()
        greetingString = enc.encrypt(greetingString)
        self.client_socket.send(greetingString)
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
        self.client_socket.send(enc.encrypt("End of Interview"))
        logger.info('User {} completed interview {}'.format(self.currentuser.getName(), self.currentuser.getIntID()))
        return

    def createInterview(self):
        global enc
        greetingString="Welcome to the interview creator!"
        greetingString = enc.encrypt(greetingString)
        self.client_socket.send(greetingString)

        askQuestionString="What is the name of this interview?"
        askQuestionString = enc.encrypt(askQuestionString)
        self.client_socket.send(askQuestionString)

        name = self.client_socket.recv(1024)
        name = enc.decrypt(name)

        logger.info('User {} created interview {}'.format(self._USER_NAME, name))
        print(name)
        questions = []

        nextQ = True
        nextA = True

        while (nextQ):
            answers = []
            msg="Please type a QUESTION?"
            msg = enc.encrypt(msg)
            self.client_socket.send(msg)
            question = self.client_socket.recv(1024)
            question = enc.decrypt(question)
            print(question)
            while(nextA):
                msg="Please type an ANSWER?\n"
                self.client_socket.send(enc.encrypt(msg))

                answer = self.client_socket.recv(1024)
                answer = enc.decrypt(answer)
                answerObj = Answer(1000, answer)

                answers.append(answerObj)
                print(answer)

                check = True

                while(check):
                    msg = "Would you like to add another ANSWER (Y/N)?\n"
                    self.client_socket.send(enc.encrypt(msg))
                    
                    checker = self.client_socket.recv(1024)
                    checker = enc.decrypt(checker)
                    print(checker)
                    if (checker == 'Y'):
                        check = False
                        nextA = True
                    elif (checker == 'N'):
                        check = False
                        nextA = False
                        print("1")
                    else:
                        msg="Invalid Response?\n"
                        self.client_socket.send(enc.encrypt(msg))
                        check = True
            
            questionObj = Question(1000,question,answers)
            questions.append(questionObj)
            nextA = True
            check2 = True

            while(check2):
                msg= 'Would you like to add another QUESTION (Y/N)?\n'
                self.client_socket.send(enc.encrypt(msg))
                
                checker = self.client_socket.recv(1024)
                checker = enc.decrypt(checker)

                if (checker == 'Y'):
                    check2 = False
                    nextQ = True
                elif (checker == 'N'):
                    check2 = False
                    nextQ = False
                else:
                    msg="Invalid Response?\n"
                    self.client_socket.send(enc.encrypt(msg))
                    check = True

        interview = ActiveInterview(1000, name, questions)

        print(questions)

        interviewID = db_interaction.makeNewInterview(interview, self.currentuser.getID())
        assigning = True
        msg= 'Would you like to assign this interview to a user (Y/N)?\n'
        self.client_socket.send(enc.encrypt(msg))
                
        checker = self.client_socket.recv(1024)
        checker = enc.decrypt(checker)
        while (assigning):
            if (checker == 'Y'):
                msg= 'Enter a user to assign to\n'
                msg = enc.encrypt(msg)
                self.client_socket.send(msg)
                assignTo = self.client_socket.recv(1024)
                assignTo = enc.decrypt(assignTo)
                print(assignTo)
                db_interaction.assignUser(interviewID, assignTo)
                assigning = False
            elif (checker == 'N'):
                assigning = False
                break
            else:
                msg="Invalid Response?\n"
                self.client_socket.send(enc.encrypt(msg))
                    
        
        msg = "End of Interview"
        self.client_socket.send(enc.encrypt(msg))



    def validate(self):
        global enc
        time.sleep(0.1)
        self.client_socket.send((enc.encrypt('Username > ')))
        in_data = self.client_socket.recv(1024)
        in_data = enc.decrypt(in_data)
        self._USER_NAME = in_data.rstrip()
        print('SERVER > Username :', self._USER_NAME)
        # VALIDATE USERNAME
        self.client_socket.send((enc.encrypt('Password > ')))
        in_data = self.client_socket.recv(1024)
        in_data = enc.decrypt(in_data)
        self._USER_PW = in_data.rstrip()
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
        global enc
        print('Terminating connection on', self.client_socket)
        logger.info('connection terminated: {}'.format(self.client_socket))
        sys.stdout.flush()
        for i in range(0,10):
            print('.', end='')
            sys.stdout.flush()
            time.sleep(0.15)
        self.client_socket.close()
        print('Socket closed')
        sys.stdout.flush()

    
    def key_exchange(self):
        dif = diffieHellman()
        other_key = self.client_socket.recv(2048).decode()
        other_key = int(other_key)
        self.client_socket.send(str(dif.publicKey).encode())
        key = dif.genKey(other_key)
        return key


    def run(self):
        global enc
        key = self.key_exchange()
        enc = Encrypt(key)
        self.client_socket.send(enc.encrypt(('Welcome to the Interview Portal')))
        time.sleep(0.1)
        _LOGIN_STATUS = self.validate()
        if _LOGIN_STATUS == True:
            print('User', self._USER_NAME, 'has a log in status of', str(_LOGIN_STATUS))
            logger.info('User {} has a login status of {}'.format(self._USER_NAME, str(_LOGIN_STATUS)))
        else:
            logger.warning('Invalid login attempt with username {}'.format(self._USER_NAME))
            CredentialsException()
            self.terminate_session()
            return
        ##This assumes that the user is trying to take an interview. Additional##
        ##user options could be added easily by making the giveInterview call  ##
        ##conditional
        self.client_socket.send(enc.encrypt(str('{}'.format(db_interaction.getUserRole(self.currentuser.getPer())))))
        if (self.currentuser.getPer() == 4): self.giveInterview()
        elif (self.currentuser.getPer() == 2): self.createInterview()

        self.terminate_session()
