class User():
	def __init__(self,UID,User,Permissions,IntID):
		self.uid = UID
		self.user = User
		self.permissions = Permissions
		self.intid = IntID
		
	def __str__(self):
		return 'User: ' + str(self.uid) + ' Name: ' + str(self.user) + ' Permissions: ' + str(self.permissions)
		
	def getID(self):
		return self.uid
		
	def getName(self):
		return self.user
	
	def getPer(self):
		return self.permissions
		
	def getIntID(self):
		return self.intid
		