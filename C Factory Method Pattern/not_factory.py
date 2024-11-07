import abc

class NotFactory(): # notification factory
    @abc.abstractmethod
    def create_not(self): # Create notification
        pass
