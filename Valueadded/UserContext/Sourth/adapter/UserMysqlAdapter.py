from Valueadded.UserContext.Sourth.port.UserRepository import UserRepository
from Valueadded.UserContext.Domain.User import User

class UserMysqlAdapter(UserRepository):
    def __init__(self) -> None:
        self.entity = User()
        super().__init__()

    def dto(self, do=...):
        return super().dto(do)
    
    def voToDto(self, context=...):
        return super().voToDto(context)
    
    def getUserInfo(self, context=...):
        return self.entity