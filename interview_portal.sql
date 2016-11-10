BEGIN TRANSACTION;
CREATE TABLE "UserRole" (
	`UserRoleID`	INTEGER NOT NULL UNIQUE,
	`UserRoleDescription`	TEXT NOT NULL,
	`CreateInterview`	INTEGER,
	`ViewInterview`	INTEGER,
	`CreateQuestion`	INTEGER,
	`ModifyQuestions`	INTEGER,
	PRIMARY KEY(`UserRoleID`)
);
INSERT INTO `UserRole` (UserRoleID,UserRoleDescription,CreateInterview,ViewInterview,CreateQuestion,ModifyQuestions) VALUES (1,'System Admin',1,1,1,1),
 (2,'Lawyer',1,1,1,1),
 (3,'Legal Aide',1,1,0,0),
 (4,'Interviewee',0,0,0,0);
CREATE TABLE "UserInformation" (
	`UserID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`UserRoleID`	INTEGER NOT NULL,
	`UserName`	TEXT NOT NULL UNIQUE,
	`Password`	TEXT NOT NULL,
	`FirstName`	TEXT NOT NULL,
	`LastName`	TEXT NOT NULL,
	`StreetAddress`	TEXT NOT NULL,
	`City`	TEXT NOT NULL,
	`State`	TEXT NOT NULL,
	`ZIP`	TEXT NOT NULL,
	`InterviewID`	INTEGER UNIQUE
);
INSERT INTO `UserInformation` (UserID,UserRoleID,UserName,Password,FirstName,LastName,StreetAddress,City,State,ZIP,InterviewID) VALUES (1,1,'grahf','pw123','Jimmy','King','222 S. Riverside Plaza','Chicago','IL','60606',NULL),
 (2,4,'interview','pw123','John','Doe','123 Sesame St.','New York','NY','12345',NULL);
CREATE TABLE "QuestionRelation" (
	`QuestionID`	INTEGER,
	`AnswerID`	INTEGER,
	PRIMARY KEY(`QuestionID`)
);
CREATE TABLE "QuestionInfo" (
	`QuestionID`	INTEGER,
	`QuestionText`	TEXT,
	PRIMARY KEY(`QuestionID`)
);
CREATE TABLE "InterviewRelation" (
	`InterviewID`	INTEGER NOT NULL,
	`QuestionID`	INTEGER,
	`UserAnswerID`	INTEGER,
	PRIMARY KEY(`InterviewID`)
);
CREATE TABLE "InterviewInfo" (
	`InterviewID`	INTEGER NOT NULL UNIQUE,
	`InterviewName`	TEXT,
	PRIMARY KEY(`InterviewID`)
);
CREATE TABLE "Answers" (
	`AnswerID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`AnswerText`	TEXT NOT NULL
);
COMMIT;
