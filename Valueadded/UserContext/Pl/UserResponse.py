from Valueadded.UserContext.North.Local.UserForWebService import UserForWebService

class UserResponse():
    def __init__(self) -> None:
        self.userForWebService = UserForWebService()
        pass

    def getInfoPl(self,request_context=[]):
        data = self.userForWebService.getUserInfo(request_context)
        pass