from not_factory import NotFactory
from push_not import PushNot

class PushNotFactory(NotFactory): # push notification factory
    def create_not(self): # Create notification
        return PushNot()

