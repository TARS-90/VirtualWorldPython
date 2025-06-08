import random
from typing import List
from AllParams.Organisms.Organism import Organism

class Animal(Organism):
    REPRODUCE_CHANCE = 5

    def reproduce(self, other: "Organism"):
        other_positions: List = self.world.get_free_neighbour_positions(other)
        free_positions: List = self.world.get_free_neighbour_positions(self)
        free_positions.extend(other_positions)

        num_of_free_pos = len(free_positions)
        if num_of_free_pos > 0:
            position = random.choice(free_positions)
            self.world.create_organism(self.id, position)
            if self.game:
                self.game.add_event("kopuluje z", other, self)

    def action(self):
        neigh_positions: List = self.world.get_available_positions(self)
        num_of_neigh_pos = len(neigh_positions)

        if num_of_neigh_pos > 0:
            destination = random.choice(neigh_positions)
            enemy = self.world.get_organism_at(destination.x, destination.y)

            if enemy is not None:
                enemy.collision(self)
            else:
                self.move(destination)

    def collision(self, attacker: "Organism"):
        if attacker.get_id() == self.id:
            if random.randint(0, self.REPRODUCE_CHANCE - 1) == 0:
                self.reproduce(attacker)
        else:
            self.fight(attacker)
