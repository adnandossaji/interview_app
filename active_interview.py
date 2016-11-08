
import question
import answer
import interview


# an object that consists of an Interview object and a dictionary consisting of key value pair's, (QuestionNumber,Question)
# object can store and return a list of Answers, Answers can be stored one at a time with putAnswer() 
# a list of questions may be submitted during the construction of the object or added one at a time after construction
class ActiveInterview():
	def __init__(self,Interview, Questions=None):
		self.interview = Interview
		self.questions = {} if Questions is None else Questions
		self.answers = []
		self.curQ = 0
		
	def putQuestion(self, question):
		self.questions[question.getNumQ] = question
		
	def putAnswer(self,answer):
		self.answers.append(answer)
		
	def getInterview(self):
		return self.interview
		
	def getQuestions(self):
		return self.questions
	
	def getAnswers(self):
		return self.answers
		
	def getCurrentQNum(self):
		return self.curQ
		
	def getCurrentQuestion(self):
		return self.questions[self.curQ]
	
	# returns the current question and increments the curQ
	def getNextQuestion(self):
		res = self.questions[self.curQ]
		self.curQ = self.curQ + 1
		return res
		
	