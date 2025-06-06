import random
from AllParams.Organisms import Organism

class Plant(Organism):
    SPREAD_CHANCE = 8

    def spread(self):
        neigh_positions = self.world.getFreeNeighbourPositions(self)
        num_of_positions = len(neigh_positions)

        if num_of_positions > 0:
            position = random.choice(neigh_positions)
            self.world.createOrganism(self.id, position)
            if self.game:
                self.game.add_event("rozsiewa się na", self, position)

    def action(self):
        if random.randint(0, self.SPREAD_CHANCE - 1) == 0:
            self.spread()

    def collision(self, attacker):
        self.fight(attacker)
