from AllParams.Organisms import Plant
from AllParams.Organisms import Animal
from AllParams.Organisms import Organism
from AllParams import Position
from AllParams import World
from AllParams import Game

class Hogweed(Plant):
    NAME = "Barszcz sosnowskiego"
    ID = 25
    FORCE = 10
    INITIATIVE = 0
    LOOK = (128, 128, 0)

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
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = self._position.x + dx
                y = self._position.y + dy
                organism = self._world.get_organism_at_coords(x, y)
                if isinstance(organism, Animal):
                    self.kill(organism)
                    self._game.add_event("zabija", self, organism)

    def collision(self, attacker: Organism):
        self.kill(attacker)
        self.kill(self)
        self._game.add_event("zjada", attacker, self)
        self._game.add_event("zabija", self, attacker)
