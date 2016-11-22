import answer

class Question():
	def __init__(self,QuestionID,QuestionText,Answers=None):
		self.qid = QuestionID
		self.question = QuestionText
		self.answers = [] if Answers == None else Answers
		self.answered = answer.Answer(-1,'default')
		
	def __str__(self):
		ret = "\n"
		for answer in self.answers:
			ret = ret + '\t\t' + str(answer) + '\n'
		return '{ QID: ' + str(self.qid) + ' Question: ' + str(self.question) + ret + '\n answered: ' + str(self.answered) + '}'
		
	def getQuestionID(self):
		return self.qid
		
	def getQuestionText(self):
		return self.question
		
	def getAnswers(self):
		return self.answers
		
	def putAnswer(self, Answer):
		self.answers.append(Answer)
		
	def answerQuestion(self, AnswerID):
		for answer in self.answers:
                        if answer.getAnswerID() == AnswerID:
                                self.answered = answer
                        else:
                                pass
		
	def getUserAnswerID(self):
		return self.answered.getAnswerID()
	
	def getUserAnswerText(self):
                return self.answered.getAnswerText()
