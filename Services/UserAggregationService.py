from Valueadded.UserContext.Pl.UserResponse import UserResponse

class UserAggregationService():
    def __init__(self) -> None:
        self.userResponse = UserResponse()
        pass

    def getUserInfo(self,request_context=[]):
        return self.userResponse.getInfoPl(request_context)