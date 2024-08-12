from Valueadded.UserContext.Sourth.adapter.UserMysqlAdapter import UserMysqlAdapter as Repository

class UserForWebService():
    def __init__(self,session) -> None:
        self.session = session
        self.repository = Repository(self.session)
        pass

    def getUserInfo(self,request_context=[]):
        result = self.repository.getUserInfo(request_context['request_context'])
        return result.__dict__