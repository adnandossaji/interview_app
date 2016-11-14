class Answer():
	def __init__(self,AID,Answer):
		self.answer = Answer
		self.aid = AID
		
	def __str__(self):
		return '[ AnswerID: ' + str(self.aid) + ' AnswerText: ' + str(self.answer) + ']\n'
		
	def getAnswerText(self):
		return self.answer
		
	def getAnswerID(self):
		return self.aid
		
		