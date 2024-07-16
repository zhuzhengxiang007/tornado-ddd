import uuid
from Common.Share.BaseEntity import BaseEntity
class User(BaseEntity):
    def __init__(self,
                 uid=None,
                 account=None,
                 password=None,
                 inner=None,
                 role=None,
                 power=None,
                 member_id=None
                 ) -> None:
        self.uid = uid if uid != None else 'user' + str(uuid.uuid4())
        self.account = account
        self.password = password
        self.inner = inner
        self.role = role
        self.power = power
        self.member_id = member_id
        pass

    # 实体渲染
    def setAll(self):

        pass