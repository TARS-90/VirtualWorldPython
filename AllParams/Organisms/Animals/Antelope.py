import random
from AllParams.Organisms.Animal import Animal
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game

class Antelope(Animal):
    NAME = "Antylopa"
    ID = 15
    FORCE = 4
    INITIATIVE = 4
    LOOK = (255, 165, 0)

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

    def _run_away(self, attacker: Organism):
        free_positions = self.world.get_free_neighbour_positions(self)
        if free_positions:
            new_position = random.choice(free_positions)
            self.game.add_event("ucieka na", self, pos = self.position)
            self.position = new_position
        else:
            self.fight(attacker)

    def collision(self, attacker: Organism):
        if attacker.get_id() == self.get_id():
            if random.randint(0, super().REPRODUCE_CHANCE - 1) == 0:
                self.reproduce(attacker)
        else:
            if random.randint(0, 1) == 1:
                self._run_away(attacker)
            else:
                self.fight(attacker)
