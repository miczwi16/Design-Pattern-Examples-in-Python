import random

from enemy_fact import EnemyFact
from monsters import Orc
from monsters import Werewolf
from monsters import Harpy
from monsters import Ghoul
from monsters import Elemental
from monsters import Ogre
from monsters import Vampire
from monsters import Minotaur
from monsters import Warg

class MediumLevelEnemyFact(EnemyFact): # medium level enemy factory
    def generate(self):
        rn_number = random.randrange(1, 10) # random number

        if rn_number == 1:
            return Orc()
        elif rn_number == 2:
            return Werewolf()
        elif rn_number == 3:
            return Harpy()
        elif rn_number == 4:
            return Ghoul()
        elif rn_number == 5:
            return Elemental()
        elif rn_number == 6:
            return Ogre()
        elif rn_number == 7:
            return Vampire()
        elif rn_number == 8:
            return Minotaur()
        elif rn_number == 9:
            return Warg()
        else:
            raise ValueError(f"random number out of range: {rn_number}")