class Answer():
	def __init__(self,AID,Answer):
		self.answer = Answer
		self.aid = AID
		
	def __str__(self):
		return 'Answer: ' + str(self.aid) + ' ' + str(self.answer) + ' ' + str(self.qid)
		
	def getAnswerText(self):
		return self.answer
		
	def getAnswerID(self):
		return self.aid
		
		