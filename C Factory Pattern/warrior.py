import random

from char import Char

class Warrior(Char):
    def __init__(self):
        super().__init__() # add random number to char attributes
        self._ste += random.randrange(6, 12)
        self._end += random.randrange(6, 12)
        self._agi += random.randrange(3, 6)
        self._spe += random.randrange(3, 6)
        self._ine += random.randrange(3, 6)
        self._wil += random.randrange(3, 6)