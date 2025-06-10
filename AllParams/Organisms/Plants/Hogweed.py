from AllParams.Organisms.Plant import Plant
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game

class Hogweed(Plant):
    NAME = "Barszcz sosnowskiego"
    ID = 25
    FORCE = 10
    INITIATIVE = 0
    LOOK = (128, 128, 0)

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
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                x = self.position.x + dx
                y = self.position.y + dy
                organism = self.world.get_organism_at(x, y)

                from AllParams.Organisms.Animal import Animal
                from AllParams.Organisms.Animals.CyberSheep import CyberSheep
                if isinstance(organism, Animal) and not isinstance(organism, CyberSheep):
                    self.kill(organism)
                    self.game.add_event("zabija", self, organism)

    def collision(self, attacker: Organism):
        from AllParams.Organisms.Animals.CyberSheep import CyberSheep
        if isinstance(attacker, CyberSheep):
            attacker.move(self.position)
            self.kill(self)
            self.game.add_event("zjada", attacker, self)
        else:
            self.kill(attacker)
            self.kill(self)
            self.game.add_event("zjada", attacker, self)
            self.game.add_event("zabija", self, attacker)
