from Valueadded.UserContext.Pl.UserResponse import UserResponse

class UserAggregationService():
    def __init__(self,session) -> None:
        self.session = session
        self.userResponse = UserResponse(self.session)
    
        pass

    def getUserInfo(self,request_context=[]):
        return self.userResponse.getInfoPl(request_context)