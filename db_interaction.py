import sqlite3
import user
import answer
import question
import interview
import active_interview


class db_int():
	def _init_(self):
		self.conn= sqlite3.connect( 'interview_app.db' )
		self.conn.row_factory = sqlite3.Row
		
	def closeConnection(self):
		self.conn.close()
	
	def getUser(self,username,password):
		self.conn.execute("select USERID, USER, PERMISSIONS, INTID from ACCOUNTS where USER = ? and PASSWORD = ?",(username,password))
		row = self.conn.fetchone()
		res = user.User(row['USERID'],row['USER'],row['PERMISSIONS'],row['INTID'])
		return res
	
	
	def getInterview(self,IntID):
		self.conn.execute("select ID, NAME, LENGTH from INTERVIEWS where ID = ?",(IntID,))
		row = self.conn.fetchone()
		res = interview.Interview(row['ID'],row['NAME'],row['LENGTH'])
		return res
		
	def getQuestions(self,IntID):
		self.conn.execute("select QUESTIONID, INTERVIEWID, QUESTION, QNUMBER from QUESTIONS where INTERVIEWID = ?",(IntID,))
		rows = self.conn.fetchall()
		res = {}
		for D in rows:
			res[rows['QNUMBER']] = question.Question(rows['QUESTIONID'],rows['INTERVIEWID'],rows['QUESTION'],rows['QNUMBER'])
		return res
	
	# accept's a list of the Answer objects and inserts each into the database 
	def submitAnswers(self, Answers):
		for Answer in Answers:
			self.conn.excute("insert into ANSWERS(USERID, ANSWER, QUESTIONID) values (?,?,?)",(Answer.getUID(), Answer.getAnswer(), Answer.getQID()))
		self.conn.commit()
		
	# accept's an activeInterview object and inserts the data into the database
	def makeNewInterview(self,activeInterview):
		qlist = activeInterview.getQuestions()
		interview = activeInterview.getInterview()
		IntID = self.conn.execute("insert into INTERVIEWS(ID,NAME,LENGTH) values (?,?,?)", (None,interview.getName(),interview.getNumQs())).lastrowid
		for num,q in qlist:
			self.conn.execute("insert into QUESTIONS(QUESTIONID, INTERVIEWID, QUESTION, QNUMBER) values (?,?,?,?)", (None,IntID,q.getQuestion(),num))
		self.conn.commit()
		
		
		
		







