from notification import Notification

class SMSNot(Notification): # SMS notification
    def __init__(self):
        super().__init__()
        self._message = "Test SMS notification"

