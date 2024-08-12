from Valueadded.UserContext.North.Local.UserForWebService import UserForWebService
from Common.Function import CheckParams
import json

class UserResponse():
    def __init__(self,session) -> None:
        self.session = session
        self.userForWebService = UserForWebService(self.session)
        pass

    def getInfoPl(self,request_context=[]):
        request_context['request_context'] = json.loads(request_context['request_context'])
        print('pl',request_context['request_context'],type(request_context['request_context']))
        check = CheckParams(request_context['request_context'],['uid'])
        print('pl',check,request_context['request_context'])
        if check != None:
            return check
        data = self.userForWebService.getUserInfo(request_context)
        pass