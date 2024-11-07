import abc

class Enemy():
    @abc.abstractmethod
    def get_name(self):
        pass



# LOW LEVEL ENEMIES

class Goblin(Enemy):
    def get_name(self):
        return "Goblin"

class Skeleton(Enemy):
    def get_name(self):
        return "Skeleton"

class Rat(Enemy):
    def get_name(self):
        return "Rat"

class Zombie(Enemy):
    def get_name(self):
        return "Zombie"

class Imp(Enemy):
    def get_name(self):
        return "Imp"

class Spider(Enemy):
    def get_name(self):
        return "Spider"

class Slime(Enemy):
    def get_name(self):
        return "Slime"

class Bat(Enemy):
    def get_name(self):
        return "Bat"

class Wolf(Enemy):
    def get_name(self):
        return "Wolf"



# MIDDLE LEVEL ENEMIES

class Orc(Enemy):
    def get_name(self):
        return "Orc"

class Werewolf(Enemy):
    def get_name(self):
        return "Werewolf"

class Harpy(Enemy):
    def get_name(self):
        return "Harpy"

class Ghoul(Enemy):
    def get_name(self):
        return "Ghoul"

class Elemental(Enemy):
    def get_name(self):
        return "Elemental"

class Ogre(Enemy):
    def get_name(self):
        return "Ogre"

class Vampire(Enemy):
    def get_name(self):
        return "Vampire"

class Minotaur(Enemy):
    def get_name(self):
        return "Minotaur"

class Warg(Enemy):
    def get_name(self):
        return "Warg"



# HIGH LEVEL ENEMIES

class Dragon(Enemy):
    def get_name(self):
        return "Dragon"

class Behemoth(Enemy):
    def get_name(self):
        return "Behemoth"

class Demon(Enemy):
    def get_name(self):
        return "Demon"

class Lich(Enemy):
    def get_name(self):
        return "Lich"

class Hydra(Enemy):
    def get_name(self):
        return "Hydra"

class Golem(Enemy):
    def get_name(self):
        return "Golem"

class Basilisk(Enemy):
    def get_name(self):
        return "Basilisk"

class Kraken(Enemy):
    def get_name(self):
        return "Kraken"

class Fenix(Enemy):
    def get_name(self):
        return "Fenix"