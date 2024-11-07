from warrior import Warrior
from thief import Thief
from mage import Mage

class CharFactory(): # character factory
    @staticmethod
    def generate_char(class_name):
        if class_name == "Warrior":
            return Warrior()
        elif class_name == "Thief":
            return Thief()
        elif class_name == "Mage":
            return Mage()
        else:
            raise ValueError(f"Unknown class type: {class_name}")