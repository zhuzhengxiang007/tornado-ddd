class BaseEntity:
    def __init__(self) -> None:
        pass

    def property_exists(self,key):
        if hasattr(self, key):
            return True
        else:
            return False
        
    def _set(self,key,value):
        setattr(self, key, value)
        return None