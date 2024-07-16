from Valueadded.UserContext.Sourth.port.UserRepository import UserRepository
from Valueadded.UserContext.Domain.User import User

class UserMysqlAdapter(UserRepository):
    def __init__(self) -> None:
        self.entity = User()
        super().__init__()

    def dto(self, do=...):
        return super().dto(do)
    
    def voToDto(self, context=...):
        for key,value in context.items():
            if (self.entity.property_exists(key)):
                self.entity._set(key,value)
        return super().voToDto(context)
    
    def getUserInfo(self, context=...):
        self.voToDto(context)
        
        return self.entity