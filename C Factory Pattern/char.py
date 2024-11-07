class Char(): # character
    def __init__(self): # init char attributes to base params
        self._ste = 6 # strength
        self._end = 6 # endurance
        self._agi = 6 # agility
        self._spe = 6 # speed
        self._ine = 6 # intelligence
        self._wil = 6 # willpower

    def get_strength(self):
        return self._ste

    def get_endurance(self):
        return self._end

    def get_agility(self):
        return self._agi

    def get_speed(self):
        return self._spe

    def get_intelligence(self):
        return self._ine

    def get_willpower(self):
        return self._wil