from AllParams.Organisms import Animal
from AllParams.Organisms import Organism
from AllParams import Position
from AllParams import World
from AllParams import Game

class Wolf(Animal):
    NAME = "Wilk"
    ID = 11
    FORCE = 9
    INITIATIVE = 5
    LOOK = (105, 105, 105)

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
