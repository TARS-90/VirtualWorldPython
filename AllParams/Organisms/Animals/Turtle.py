import random
from AllParams.Organisms import Animal
from AllParams.Organisms import Organism
from AllParams import Position
from AllParams import World
from AllParams import Game


class Turtle(Animal):
    NAME = "Żółw"
    ID = 14
    FORCE = 2
    INITIATIVE = 1
    LOOK = (85, 107, 47)

    def __init__(self, world: World, position: Position, game: Game):
        self._world = world
        self._position = position
        self._game = game

        # Stamp counter incrementation
        Organism.stamp_counter += 1
        self.set_stamp(Organism.stamp_counter)

        self.set_name(self.NAME)
        self.set_id(self.ID)
        self.set_force(self.FORCE)
        self.set_initiative(self.INITIATIVE)
        self.set_look(self.LOOK)

    def action(self):
        chance_to_move = random.randint(0, 3)
        if chance_to_move == 0:
            super().action()

    def collision(self, attacker: Organism):
        if attacker.get_id() == self.get_id():
            if random.randint(0, super().REPRODUCE_CHANCE - 1) == 0:
                self.reproduce(attacker)
        elif attacker.get_force() < 5:
            self._game.add_event("odbija atak", self, attacker)
        else:
            self.fight(attacker)
