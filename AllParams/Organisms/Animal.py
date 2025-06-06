import random
from typing import List
from AllParams.Organisms import Organism

class Animal(Organism):
    REPRODUCE_CHANCE = 5

    def reproduce(self, other: "Organism"):
        other_positions: List = self.world.getFreeNeighbourPositions(other)
        free_positions: List = self.world.getFreeNeighbourPositions(self)
        free_positions.extend(other_positions)

        num_of_free_pos = len(free_positions)
        if num_of_free_pos > 0:
            position = random.choice(free_positions)
            self.world.createOrganism(self.id, position)
            if self.game:
                self.game.add_event("kopuluje z", other, self)

    def action(self):
        neigh_positions: List = self.world.getAvailablePositions(self)
        num_of_neigh_pos = len(neigh_positions)

        if num_of_neigh_pos > 0:
            destination = random.choice(neigh_positions)
            enemy = self.world.getOrganismAt(destination)

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
