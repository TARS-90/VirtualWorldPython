from AllParams.Organisms.Plant import Plant
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game

class NightshadeBerries(Plant):
    NAME = "Wilcze jagody"
    ID = 24
    FORCE = 99
    INITIATIVE = 0
    LOOK = (75, 0, 130)

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

    def collision(self, attacker: Organism):
        self.kill(attacker)
        self.kill(self)
        self.game.add_event("zjada", attacker, self)
        self.game.add_event("zabija", self, attacker)
