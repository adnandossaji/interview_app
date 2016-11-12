import answer

class Question():
	def __init__(self,QuestionID,QuestionText,Answers=None):
		self.qid = QuestionID
		self.question = QuestionText
		self.answers = Answers if Answers == None else []
		self.answered = 0
		
	def __str__(self):
		return 'QID: ' + str(self.qid) + ' IntID: ' + str(self.intid) + ' Question: ' + str(self.question) + ' Qnum: ' + str(self.qnum) + ' AnsID: ' + str(self.aid)
		
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