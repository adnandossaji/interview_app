import answer

class Question():
	def __init__(self,QuestionID,QuestionText,Answers=None):
		self.qid = QuestionID
		self.question = QuestionText
		self.answers = [] if Answers == None else Answers
		self.answered = 0
		
	def __str__(self):
		ret = "\n"
		for answer in self.answers:
			ret = ret + '\t\t' + str(answer) + '\n'
		return '{ QID: ' + str(self.qid) + ' Question: ' + str(self.question) + ret + '}'
		
	def getQuestionID(self):
		return self.qid
		
	def getQuestionText(self):
		return self.question
		
	def getAnswers(self):
		return self.answers
		
	def putAnswer(self, Answer):
		self.answers.append(Answer)
		
	def answerQuestion(self, AnswerID):
		self.answered = AnswerID
		
	def getUserAnswer(self):
		return self.answered