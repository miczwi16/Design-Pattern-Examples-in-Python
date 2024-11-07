from notification import Notification

class PushNot(Notification): # Push notification
    def __init__(self):
        super().__init__()
        self._message = "Test push notification"
