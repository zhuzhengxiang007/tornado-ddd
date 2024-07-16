from abc import ABC, abstractmethod

class BaseRepository(ABC):

    @abstractmethod
    def dto(self,do=[]):
        pass

    @abstractmethod
    def voToDto(self,context=[]):
        pass