from singleton_exception import SingletonException

class Session():
    __instance = None

    @staticmethod
    def open():
        Session()

    @staticmethod
    def close():
        Session.__instance = None

    @staticmethod
    def exists():
        if Session.__instance != None:
            return True
        else:
            return False

    def __init__(self):
        if Session.__instance != None:
            raise SingletonException("You are already logged in!")
        else:
            Session.__instance = self