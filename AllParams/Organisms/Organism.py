from abc import ABC, abstractmethod


class Organism(ABC):
    __stampCounter = 0


    def __isWin(self, attacker):
        if (self.force > attacker.force):
            return True
        return False


    def _move(self, destination):
        self.posiion = destination



    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, other):
        pass