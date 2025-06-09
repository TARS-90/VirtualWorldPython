from collections import deque
from AllParams.Position import Position

class World:
    def __init__(self, size_x, size_y, game):
        self.size_x = size_x
        self.size_y = size_y
        self.game = game
        self.organisms = []
        self.organisms_to_add = []

    def get_organisms(self):
        return sorted(self.organisms, key=lambda o: (-o.initiative, o.stamp))

    def get_size_x(self):
        return self.size_x

    def get_size_y(self):
        return self.size_y

    def cross_the_borders(self, organism, dx, dy):
        new_x = organism.position.x + dx
        new_y = organism.position.y + dy
        return not (1 <= new_x <= self.size_x and 1 <= new_y <= self.size_y)

    def is_another_place(self, dx, dy):
        return not (dx == 0 and dy == 0)

    def is_place_available(self, organism, dx, dy):
        if not self.is_another_place(dx, dy) or self.cross_the_borders(organism, dx, dy):
            return False
        new_x = organism.position.x + dx
        new_y = organism.position.y + dy
        for other in self.organisms_to_add:
            if other.position.x == new_x and other.position.y == new_y:
                return False
        return True

    def get_organism_at(self, x, y):
        for organism in self.organisms:
            if organism.position.x == x and organism.position.y == y:
                return organism
        return None

    def get_organism_at_position(self, pos):
        return self.get_organism_at(pos.x, pos.y)

    def get_free_neighbour_positions(self, organism):
        result = []
        for dx in range(-1, 2):
            for dy in range(-1, 2):
                new_x = organism.position.x + dx
                new_y = organism.position.y + dy
                if self.is_place_available(organism, dx, dy) and self.get_organism_at(new_x, new_y) is None:
                    result.append(Position(new_x, new_y))
        return result

    def get_available_positions(self, organism):
        from AllParams.Organisms.Animals.Antelope import Antelope
        result = []
        range_ = 2 if isinstance(organism, Antelope) else 1
        for dx in range(-range_, range_ + 1):
            for dy in range(-range_, range_ + 1):
                if self.is_place_available(organism, dx, dy):
                    new_x = organism.position.x + dx
                    new_y = organism.position.y + dy
                    result.append(Position(new_x, new_y))
        return result

    def create_organism(self, id_, position):
        from AllParams.Organisms.Animals import Human, Wolf, Sheep, Fox, Turtle, Antelope
        from AllParams.Organisms.Plants import Grass, Milkweed, Guarana, NightshadeBerries, Hogweed

        cls_map = {
            10: Human.Human,
            11: Wolf.Wolf,
            12: Sheep.Sheep,
            13: Fox.Fox,
            14: Turtle.Turtle,
            15: Antelope.Antelope,
            21: Grass.Grass,
            22: Milkweed.Milkweed,
            23: Guarana.Guarana,
            24: NightshadeBerries.NightshadeBerries,
            25: Hogweed.Hogweed
        }
        organism_class = cls_map.get(id_)
        if organism_class:
            new_org = organism_class(self, position, self.game)
            self.organisms_to_add.append(new_org)

    def add_all_organisms_to_be_added(self):
        self.organisms.extend(self.organisms_to_add)
        self.organisms_to_add.clear()
