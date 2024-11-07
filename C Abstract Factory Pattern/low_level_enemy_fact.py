import random

from enemy_fact import EnemyFact
from monsters import Goblin
from monsters import Skeleton
from monsters import Rat
from monsters import Zombie
from monsters import Imp
from monsters import Spider
from monsters import Slime
from monsters import Bat
from monsters import Wolf

class LowLevelEnemyFact(EnemyFact): # low level enemy factory
    def generate(self):
        rn_number = random.randrange(1, 10) # random number

        if rn_number == 1:
            return Goblin()
        elif rn_number == 2:
            return Skeleton()
        elif rn_number == 3:
            return Rat()
        elif rn_number == 4:
            return Zombie()
        elif rn_number == 5:
            return Imp()
        elif rn_number == 6:
            return Spider()
        elif rn_number == 7:
            return Slime()
        elif rn_number == 8:
            return Bat()
        elif rn_number == 9:
            return Wolf()
        else:
            raise ValueError(f"random number out of range: {rn_number}")