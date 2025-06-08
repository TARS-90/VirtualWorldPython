from AllParams.Organisms.Animal import Animal
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game


class Sheep(Animal):
    NAME = "Owca"
    ID = 12
    FORCE = 4
    INITIATIVE = 4
    LOOK = (211, 211, 211)

    def __init__(self, world: World, position: Position, game: Game):
        super().__init__()
        self.world = world
        self.position = position
        self.game = game

        # Stamp counter incrementation
        Organism.stamp_counter += 1
        self.set_stamp(Organism.stamp_counter)

        self.set_name(self.NAME)
        self.set_id(self.ID)
        self.set_force(self.FORCE)
        self.set_initiative(self.INITIATIVE)
        self.set_look(self.LOOK)