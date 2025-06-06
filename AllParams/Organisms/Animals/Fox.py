import random
from AllParams.Organisms import Animal
from AllParams.Organisms import Organism
from AllParams import Position
from AllParams import World
from AllParams import Game

class Fox(Animal):
    NAME = "Lis"
    ID = 13
    FORCE = 3
    INITIATIVE = 7
    LOOK = (255, 69, 0)

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
        neigh_positions = self._world.get_available_positions(self)
        if neigh_positions:
            destination = random.choice(neigh_positions)
            enemy = self._world.get_organism_at(destination)

            if enemy:
                if enemy.get_force() <= self.get_force():
                    enemy.collision(self)
            else:
                self.move(destination)
