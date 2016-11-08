class Question():
	def __init__(self,QID,IntID,Question,QuestionNumber):
		self.qid = QID
		self.intid = IntID
		self.question = Question
		self.qnum = QuestionNumber
		
	def __str__(self):
		return 'QID: ' + str(self.qid) + ' IntID: ' + str(self.intid) + ' Question: ' + str(self.question) + ' Qnum: ' + str(self.qnum) + ' AnsID: ' + str(self.aid)
		
	def getQID(self):
		return self.qid
		
	def getIntID(self):
		return self.intid
		
	def getQuestion(self):
		return self.question
		
	def getQNum(self):
		return self.qnum
		