from abc import ABC, abstractmethod
from typing import Optional, Union, Tuple

class Organism(ABC):
    stamp_counter = 0

    def __init__(self):
        self.game = None
        self.world = None
        self.position = None
        self.name = None
        self.id = None
        self.stamp = None
        self.force = None
        self.initiative = None
        self.look = None
        self.is_alive = True

    # setters
    def set_name(self, value: str):
        self.name = value

    def set_id(self, value: int):
        self.id = value

    def set_force(self, value: int):
        self.force = value

    def set_initiative(self, value: int):
        self.initiative = value

    def set_stamp(self, value: int):
        self.stamp = value

    def set_look(self, value: Union[Tuple[int, int, int], object]):
        self.look = f'#{value[0]:02x}{value[1]:02x}{value[2]:02x}'


    # getters
    def get_name(self) -> Optional[str]:
        return self.name

    def get_id(self) -> Optional[int]:
        return self.id

    def get_position(self):
        return self.position

    def get_force(self) -> Optional[int]:
        return self.force

    def get_initiative(self) -> Optional[int]:
        return self.initiative

    def get_stamp(self) -> Optional[int]:
        return self.stamp

    def get_look(self):
        return self.look

    def is_alive_func(self) -> Optional[bool]:
        return self.is_alive


    ###########################
    #                         #
    #      OTHER METHODS      #
    #                         #
    ###########################

    def is_win(self, attacker: "Organism") -> bool:
        return self.force > attacker.force

    def move(self, position):
        self.game.add_event("porusza się na", self, pos = position)
        self.position = position

    def fight(self, attacker: "Organism"):
        if self.is_win(attacker):
            self.kill(attacker)
            self.game.add_event("zabija", self, attacker)
        else:
            attacker.position = self.position
            self.kill(self)

            from AllParams.Organisms.Plant import Plant
            if isinstance(self, Plant):
                self.game.add_event("zjada", attacker, self)
            else:
                self.game.add_event("zabija", attacker, self)

    def kill(self, organism: "Organism"):
        organism.is_alive = False

    def increase_force(self, organism: "Organism", value: int):
        if organism.force is None:
            organism.force = value
        else:
            organism.force += value

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self, organism: "Organism"):
        pass