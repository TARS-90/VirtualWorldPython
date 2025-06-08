from AllParams.Organisms.Plant import Plant
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game

class Guarana(Plant):
    NAME = "Guarana"
    ID = 23
    FORCE = 0
    INITIATIVE = 0
    BONUS = 3
    LOOK = (139, 0, 0)

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
        self.increase_force(attacker, self.BONUS)
        self.fight(attacker)
