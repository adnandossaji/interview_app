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
		select = "SELECT UserID, UserName, UserRoleID, InterviewID "
		table = "FROM UserInformation "
		self.conn.execute(select + table + "WHERE UserName = ? AND Password = ?",(username,password))
		row = self.conn.fetchone()
		res = user.User(row['UserID'],row['UserName'],row['UserRoleID'],row['InterviewID'])
		return res
	
	
	def getInterview(self,InterviewID):
		SELECT = "SELECT ii.InterviewName, ir.QuestionID, qi.QuestionText, qr.AnswerID, a.AnswerText "
		FROM = "FROM InterviewInfo ii "
		JOINS = "INNER JOIN InterviewRelation ir ON ii.InterviewID = ir.InterviewID INNER JOIN QuestionInfo qi ON ir.QuestionID = qi.QuestionID INNER JOIN QuestionRelation qr ON qi.QuestionID = qr.QuestionID INNER JOIN Answers a on qr.AnswerID = a.AnswerID "
		rows = self.conn.execute(SELECT + FROM + JOINS + "WHERE ii.InterviewID = ?",(InterviewID,)).fetchall()
		InterviewName = rows[0]['InterviewName']
		Questions = {}
		
		for row in rows:
			if row['QuestionID'] in Questions:
				Questions[row['QuestionID']].putAnswer(answer.Answer(row['AnswerID'],row['AnswerText']))
			else 
				Questions[row['QuestionID']] = question.Question(row['QuestionID'],row['QuestionText'])
				Questions[row['QuestionID']].putAnswer(answer.Answer(row['AnswerID'],row['AnswerText']))
		
		res = active_interview.ActiveInterview(InterviewID,InterviewName,list(Questions.values()))
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
		
		
		
		







