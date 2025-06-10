import random
from collections import deque
from AllParams.Position import Position
from AllParams.World import World
from UserInterface.GameWindow import GameWindow


class Game:
    MAX_EVENTS = 20

    def __init__(self, size_x, size_y, num_a, num_p):
        self.events = deque()
        self.world = World(size_x, size_y, self)
        self.game_window = GameWindow(self, self.world)
        self.tour = 0
        self.does_initialization_end = False

        self.init_animals(0)
        self.init_plants(0)
        self.does_initialization_end = True

    # Gettery
    def get_window(self):
        return self.game_window

    def get_world(self):
        return self.world

    def get_events(self):
        return self.events

    def initialization_done(self):
        return self.does_initialization_end

    # Inicjalizacja organizmów
    def init_organism(self, id_):
        while True:
            x = random.randint(1, self.world.size_x)
            y = random.randint(1, self.world.size_y)
            if self.world.get_organism_at(x, y) is None:
                break
        self.world.create_organism(id_, Position(x, y))
        self.world.add_all_organisms_to_be_added()

    def init_plants(self, n):
        for _ in range(n):
            id_ = random.randint(21, 25)
            self.init_organism(id_)

    def init_animals(self, n):
        self.init_organism(10)  # Human
        self.init_organism(16)  # Cyber sheep
        for _ in range(n):
            id_ = random.randint(11, 15)
            self.init_organism(id_)

    def new_game(self, size_x, size_y, tour_number):
        self.world = World(size_x, size_y, self)
        self.get_window().set_new_world(self.world)
        self.events.clear()
        self.tour = tour_number

    def save_game(self):
        try:
            with open("save.txt", "w") as save:
                save.write("#World: sizes, tour\n")
                save.write(f"{self.world.size_x} {self.world.size_y} {self.tour}\n")

                save.write("#Organisms: id, x, y, force\n")
                for o in self.world.get_organisms():
                    save.write(f"{o.id} {o.position.x} {o.position.y} {o.force}")
                    if o.id == 10:  # Human
                        save.write(f" {o.get_spell_active()} {o.get_delay()}")
                    save.write("\n")
        except FileNotFoundError as e:
            raise RuntimeError(e)

    def read_game(self):
        try:
            with open("save.txt", "r") as file:
                lines = file.readlines()

                size_x, size_y, tour = map(int, lines[1].strip().split())
                self.new_game(size_x, size_y, tour)

                for line in lines[3:]:
                    parts = list(map(int, line.strip().split()))
                    id_, x, y, force = parts[:4]
                    self.world.create_organism(id_, Position(x, y))
                    self.world.add_all_organisms_to_be_added()
                    self.world.get_organism_at(x, y).set_force(force)

                    if id_ == 10:
                        spell_active, delay = parts[4], parts[5]
                        human = self.world.get_organism_at(x, y)
                        human.set_spell_active(spell_active)
                        human.set_delay(delay)

        except FileNotFoundError as e:
            raise RuntimeError(e)

    def add_event(self, event, o1=None, o2=None, pos=None):
        if len(self.events) == self.MAX_EVENTS:
            self.events.popleft()

        if o1 and o2:
            pos1 = o1.position
            pos2 = o2.position
            sentence = f"{o1.name}({pos1.x},{pos1.y}) {event} {o2.name}({pos2.x},{pos2.y})"
        elif o1 and pos:
            sentence = f"{o1.name}({o1.position.x},{o1.position.y}) {event} ({pos.x},{pos.y})"
        else:
            sentence = event

        self.events.append(sentence)

    def next_round(self):
        self.tour += 1
        self.add_event(f"----Tura {self.tour}----")

        for o in self.world.get_organisms():
            if o.is_alive:
                o.action()

        self.world.organisms = [o for o in self.world.get_organisms() if o.is_alive]
        self.world.add_all_organisms_to_be_added()
