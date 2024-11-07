from not_factory import NotFactory
from sms_not import SMSNot

class SMSNotFactory(NotFactory): # sms notification factory
    def create_not(self): # Create notification
        return SMSNot()

