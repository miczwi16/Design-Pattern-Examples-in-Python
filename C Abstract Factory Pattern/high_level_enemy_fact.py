import random

from enemy_fact import EnemyFact
from monsters import Dragon
from monsters import Behemoth
from monsters import Demon
from monsters import Lich
from monsters import Hydra
from monsters import Golem
from monsters import Basilisk
from monsters import Kraken
from monsters import Fenix

class HighLevelEnemyFact(EnemyFact): # high level enemy factory
    def generate(self):
        rn_number = random.randrange(1, 10) # random number

        if rn_number == 1:
            return Dragon()
        elif rn_number == 2:
            return Behemoth()
        elif rn_number == 3:
            return Demon()
        elif rn_number == 4:
            return Lich()
        elif rn_number == 5:
            return Hydra()
        elif rn_number == 6:
            return Golem()
        elif rn_number == 7:
            return Basilisk()
        elif rn_number == 8:
            return Kraken()
        elif rn_number == 9:
            return Fenix()
        else:
            raise ValueError(f"random number out of range: {rn_number}")
