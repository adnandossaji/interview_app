class CredentialsException(Exception):
    def __init__(self,*args,**kwargs):
        Exception.__init__(self,"Username or password incorrect.",**kwargs)
        print("Username or password incorrect.")