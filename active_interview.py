
import question
import answer
import interview


# an object that consists of an Interview object and a dictionary consisting of key value pair's, (QuestionNumber,Question)
# object can store and return a list of Answers, Answers can be stored one at a time with putAnswer() 
# a list of questions may be submitted during the construction of the object or added one at a time after construction
class ActiveInterview():
	def __init__(self,InterviewID,InterviewName, Questions=None):
		self.interviewID = InterviewID
		self.interviewName = InterviewName
		self.questions = [] if Questions is None else Questions
		self.iter = 0
		
	def putQuestion(self, question):
		self.questions[question.getNumQ] = question
		
	def getInterviewID(self):
		return self.interviewID
		
	def getInterviewName(self):
		return self.interviewName
		
	def getQuestions(self):
		return self.questions
	
	# returns the current question and increments the curQ
	def getNextQuestion(self):
		res = self.questions[self.iter]
		self.iter = self.iter + 1
		return res
		
	