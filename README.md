# interview_app

CSC 376 Distributed Systems
Fall 2016-2017
DePaul University
Karen Heart, Instructor

# Usage

## How to create an Interview:
1. sign into the client portal lawyer permissions or higher
2. select 1 and press enter 
3. enter the name of the interview and press enter
4. enter a question, then an answer. if you would like to add more than one answer type 'Y' and press enter
5. when you are finished adding the questions you can assign the interview to a user by entering 'Y'

## How to take an Interview:
1. sign into the client portal with interviewee permissions using the username and password given
2. the assigned interview should show up with the first question. 
3. Answer by typing one of the letter options shown and pressing enter
3. continue answering the questions until the interview ends and you are logged out
4. the program will automatically save your answers and will be available to the lawyer who assigned it for a later date

## How to assign an Interview:
1. log into the client portal with lawyer permissions
2. select option 3
3. enter the interview ID number you would like to assign
4. if the interview you wish to assign is already taken you have to option to assign a different interview

## How to review an Interview:
1. log in with the correct credentails
2. select option 2
3. enter the username of the interviewee you would like to view the interview for

# Structured Interviews

* Attorneys and their staff could create a structured interview by drafting questions and possible answers, as well as establishing the order in which questions are asked. >>>>> Done!
* Interviewees answer the questions, and the software records their answers. >>>>> Done!
* After completion of interviews, attorneys and their staff may view the answers, along with the associated questions. >>>>> Karen working on this
* All parties using the structured interviewing system must be authenticated.   >>>> Done!
* Users must also be authorized, meaning that only the attorneys and their designated staff members may create, modify, or delete structured interviews, as well as review the answers provided by interviewees. >>>> User Roles... Done!

# Documentation

### **User(** *UserID, UserName, UserRoleID, InterviewID* **)**
A basic user class that is used to model our User table in our database

**\__str\__()** > return String

**getID()** > return UserID

**getName()** > return UserName

**getPer()** > return UserRoleID

**getIntID()** > return InterviewID


### **Question(** *QuestionID, QuestionText, Answers* **)**
A basic question class that is used to model our Question table in our database

**\__str\__()** > return String

**getQuestionId()** > return QuestionID

**getQuestionText()** > return QuestionText

**getAnswers()** > return Answers

**getAnswer()** > return String

**putAnswer()**

**answerQuestion()**

**getUserAnswer()** > return String


### **Answer(** *AID, Answer* **)**
A basic answer class that is used to model our Answer table in our database

**\__str\__()** > return String

**getAnswerText()** > return Answer

**getAnswerID()** > return AID


### **Interview(** *IntID, Title, NumQs* **)**
A basic interview class that is used to model our Interview table in our database

**getIntID()** > return IntID

**getName()** > return Title

**getNumQs()** > return NumQs

### **ActiveInterview(** *InterviewID, InterviewName, Questions* **)**
An active interview class that is used keep an active interview in session

**putQuestion()**

**getInterviewID()** > return InterviewID

**getInterviewName()** > return InterviewName

**getQuestions()** > return Questions

**getQuestion()** > return Question()

**answerQuestion(** *AnswerID* **)**

**resetIter()**

**getNextQuestion(** *AnswerID* **)** return String

**\__str\__()** > return String


### **CredentialsException(** *Exception* **)**
A basic exception class to handle authentication exceptions

**startInterview(** *InterviewID* **)** raise CredentiasException()


### **diffieHellman()**
The diffie hellman key exchange class is an algorithm used to establish a shared secret between two parties. In our case the client and server.

**genRandom(** *bits* **)** > return Integer

**genKey(** *otherKey* **)** > return String


### **Encrypt(** *key* **)**
The encryption class takes a string 16, 24,or 32 digit key as a string and is converted to bytes by the constructor. Use by instantiating anEncrypt object with the key passed and callencrypt or decrypt with a string passed as msg.

**genRandom(** *message, key_size*, **)** > return String

**genKey(** *ciphertext* **)** > return String


# Group Project Credits

Project Name: Structured Interview Portal

List each group member, followed by a brief description of 
the member's coding contribution
Example: 
Bob Hackworth    wrote main(. and the point scoring functions
 
NOTE:  List one group member per line
 
Group Member      Contribution

### Adnan Dossaji
1. Second iteration of Server/ServerThread/Client framework (REVAMPED by James King)
2. Part of database structure (Pair programming w/ James King)
3. First iteration of User class (id, username, password)
4. Added init. Error Handling for CredentialExceptions
5. Added init. lawyer interface (Work in progress)

### Arshad Khan
1. Added startInterview for error handling in CredentialExceptions

### Brandon Meng
1. Created interview taking procedures on client
2. Created interview administration on server
3. Implemented answer saving
4. Various debugging issues

### Cody Castino
1. Created the User, Interview, Question, Answer, and Active_Interview obj's for data manipulation
2. Actively updated and tailored the above objects as needed by other code as developed
3. Created and was the major contributor for db_Interaction

### James King
1. Final iteration of Server/ServerThread/Client framework
2. Main database structure
3. Admin Menu

### Karen Cardenas
1. reviewInterview()

### Keaton Zonca
1. added code to assign a interview to a user when creating a new interview
2. assign interview from adminMenu
2. assignUser, checkIntAssigned, and  etUserInterviewID in db_interaction
3. added logging to server and serverThread and created logging.ini

### Khalid Alrawaf
1. def validate()
2. authentication process

## Matthew Current
1. allowed to assign multiple interverviews at once

### Tom Plutz
1. Wrote the encryption class.
2. Wrote a Diffie Hellmann KeyExchange class for the server and client to use.
3. Wrote function to import and install needed modules using pip.
