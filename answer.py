class Answer():
	def __init__(self,UID,Answer,QID):
		self.answer = Answer
		self.qid = QID
		self.uid = UID
		
	def __str__(self):
		return 'Answer: ' + str(self.aid) + ' ' + str(self.answer) + ' ' + str(self.qid)
		
	def getAnswer(self):
		return self.answer
		
	def getQID(self):
		return self.qid
		
	def getUID(self):
		return self.uid
		
		