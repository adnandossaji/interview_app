import sqlite3
import user
import answer
import question
import interview
import active_interview


def getUser( username, password):
        conn= sqlite3.connect( 'interview_portal.db' )
        conn.row_factory = sqlite3.Row
        select = "SELECT UserID, UserName, UserRoleID, InterviewID "
        table = "FROM UserInformation "
        row = conn.execute(select + table + "WHERE UserName = ? AND Password = ?",(username,password)).fetchone()
        res = user.User(row['UserID'],row['UserName'],row['UserRoleID'],row['InterviewID'])
        #print(res)
        conn.close()
        return res
	
	
def getInterview(InterviewID):
        conn= sqlite3.connect( 'interview_portal.db' )
        conn.row_factory = sqlite3.Row
        SELECT = "SELECT ii.InterviewName, ir.QuestionID, qi.QuestionText, qr.AnswerID, a.AnswerText "
        FROM = "FROM InterviewInfo ii "
        JOINS = "INNER JOIN InterviewRelation ir ON ii.InterviewID = ir.InterviewID INNER JOIN QuestionInfo qi ON ir.QuestionID = qi.QuestionID INNER JOIN QuestionRelation qr ON qi.QuestionID = qr.QuestionID INNER JOIN AnswerInfo a on qr.AnswerID = a.AnswerID "
        rows = conn.execute(SELECT + FROM + JOINS + "WHERE ii.InterviewID = ?",(InterviewID,)).fetchall()
        InterviewName = rows[0]['InterviewName']
        Questions = {}
        
        for row in rows:
        	if row['QuestionID'] in Questions:
        		Questions[row['QuestionID']].putAnswer(answer.Answer(row['AnswerID'],row['AnswerText']))
        	else :
        		Questions[row['QuestionID']] = question.Question(row['QuestionID'],row['QuestionText'])
        		Questions[row['QuestionID']].putAnswer(answer.Answer(row['AnswerID'],row['AnswerText']))
	
        res = active_interview.ActiveInterview(InterviewID,InterviewName,list(Questions.values()))
        conn.close()
        #print(res)
        return res
	
	# accept's a list of the Answer objects and inserts each into the database 
def submitAnswers(ActiveInterview):
        conn= sqlite3.connect( 'interview_portal.db' )
        conn.row_factory = sqlite3.Row
        for Question in ActiveInterview.getQuestions():
        	conn.excute("INSERT INTO InterviewRelation(InterviewID, QuestionID, UserAnswerID) values (?,?,?)",(ActiveInterview.getInterviewID(), Question.getQuestionID(), Question.getUserAnswer()))
        conn.commit()
        conn.close()
		
	# accept's an activeInterview object and inserts the data into the database
def makeNewInterview(activeInterview):
        conn= sqlite3.connect( 'interview_portal.db' )
        conn.row_factory = sqlite3.Row
        qlist = activeInterview.getQuestions()
        interview = activeInterview.getInterview()
        IntID = self.conn.execute("insert into INTERVIEWS(ID,NAME,LENGTH) values (?,?,?)", (None,interview.getName(),interview.getNumQs())).lastrowid
        for num,q in qlist:
        	self.conn.execute("insert into QUESTIONS(QUESTIONID, INTERVIEWID, QUESTION, QNUMBER) values (?,?,?,?)", (None,IntID,q.getQuestion(),num))
        conn.commit()
        conn.close()
	
	
	
		

#getUser('ccastino','pw123')
#getInterview('1')






