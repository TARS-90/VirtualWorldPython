from AllParams.Organisms.Animal import Animal
from AllParams.Organisms.Organism import Organism
from AllParams.Position import Position
from AllParams.World import World
from AllParams.Game import Game


class CyberSheep(Animal):
    NAME = "Cyber Owca"
    ID = 16
    FORCE = 4
    INITIATIVE = 4
    LOOK = (0, 128, 128)

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
        if len(self.world.hogweeds) > 0:
            hogweed = self.world.hogweeds[0]
            destination = Position(self.position.x, self.position.y)

            if hogweed.position.x > self.position.x:
                destination.x += 1
            if hogweed.position.x < self.position.x:
                destination.x -= 1
            if hogweed.position.y > self.position.y:
                destination.y += 1
            if hogweed.position.y < self.position.y:
                destination.y -= 1

            enemy = self.world.get_organism_at_position(destination)
            if enemy is not None and not isinstance(enemy, CyberSheep):
                enemy.collision(self)
            else:
                 self.move(destination)
        else:
            super().action()
