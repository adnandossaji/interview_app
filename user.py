class User():
	def __init__(self,UserID,UserName,UserRoleID,InterviewID):
		self.uid = UserID
		self.user = UserName
		self.permissions = UserRoleID
		self.intid = InterviewID
		
	def __str__(self):
		return 'User: ' + str(self.uid) + ' Name: ' + str(self.user) + ' Permissions: ' + str(self.permissions) + str(self.intid)
		
	def getID(self):
		return self.uid
		
	def getName(self):
		return self.user
	
	def getPer(self):
		return self.permissions
		
	def getIntID(self):
		return self.intid
		