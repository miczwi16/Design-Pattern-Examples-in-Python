import abc

class EnemyFact(): # enemy factory
    @abc.abstractmethod
    def generate(self):
        pass
