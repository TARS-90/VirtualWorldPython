import random
from AllParams.Organisms.Plant import Plant
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game

class Milkweed(Plant):
    NAME = "Mlecz"
    ID = 22
    FORCE = 0
    INITIATIVE = 0
    LOOK = (255, 255, 0)

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

    def action(self):
        for _ in range(3):
            if random.randint(0, self.SPREAD_CHANCE - 1) == 0:
                self.spread()
                break
