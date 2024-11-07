from notification import Notification

class EmailNot(Notification): # Email notification
    def __init__(self):
        super().__init__()
        self._message = "Test email notification"

