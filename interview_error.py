class CredentialsException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,"Username or password incorrect.",**kwargs)
        print("Username or password incorrect.")
        
    def startInterview(self, InterviewID):
        try:
            self.Interview = db_interaction.getInterview(self.InterviwID)
        except:
            print('Sorry No Interview Found')
            raise CredentialsException('No Ineterview Found!')
        else:
            print('Now Starting the Interview')
