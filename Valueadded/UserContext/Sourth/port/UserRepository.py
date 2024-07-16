from Common.Share.BaseRepository import BaseRepository
from abc import ABC, abstractmethod

class UserRepository(BaseRepository):

    @abstractmethod
    def getUserInfo(self,context=[]):
        pass