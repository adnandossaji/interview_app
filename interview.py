class Interview():
	def __init__(self,IntID,Title,NumQs):
		self.intid = IntID
		self.title = Title
		self.numqs = NumQs
		
	def __str__(self):
		return 'ID: ' + str(self.intid) + ' Title: ' + str(self.title) + ' NumQs: ' + str(self.numqs)
		
	def getIntID(self):
		return self.intid
		
	def getName(self):
		return self.title
		
	def getNumQs(self):
		return self.numqs