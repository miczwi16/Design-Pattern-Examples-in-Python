from not_factory import NotFactory
from email_not import EmailNot

class EmailNotFactory(NotFactory): # email notification factory
    def create_not(self): # Create notification
        return EmailNot()

