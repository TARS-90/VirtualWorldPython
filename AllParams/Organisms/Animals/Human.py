from AllParams.Organisms.Animal import Animal
from AllParams.Position import Position
from AllParams.Organisms.Organism import Organism

class Human(Animal):
    NAME = "Człowiek"
    ID = 10
    FORCE = 5
    ADDING_FORCE = 5
    INITIATIVE = 4
    LOOK = (0, 255, 255)

    def __init__(self, world, position, game):
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
        self.spell_info = ""
        self.delay = 0
        self.spell_active = False
        self.does_acted = False
        self.direction = None

        self.game.game_window.root.bind("<Key>", self.on_key_press)
        self.game.game_window.root.focus_set()

    def set_delay(self, value):
        self.delay = value

    def set_spell_active(self, value):
        self.spell_active = (value == 1)

    def get_delay(self):
        return self.delay

    def get_spell_active(self):
        return 1 if self.spell_active else 0

    def passive_spell(self):
        if self.delay > self.ADDING_FORCE:
            self.set_force(self.get_force() - 1)

        if self.delay > 0:
            self.delay -= 1
        else:
            self.spell_active = False

    def activate_spell(self):
        self.increase_force(self, self.ADDING_FORCE)
        self.delay = self.ADDING_FORCE * 2
        self.spell_active = True
        self.spell_info = "Człowiek aktywował super umiejętność"

    def do_movement(self, direction):
        print("Wykonywanie akcji człowieka")
        enemy = self.world.get_organism_at_position(direction)
        if enemy is not None:
            enemy.collision(self)
        else:
            self.move(direction)

    def action(self):
        self.does_acted = False
        self.passive_spell()

        if self.direction is not None:
            self.do_movement(self.direction)
            self.direction = None

        if self.spell_info:
            self.game.add_event(self.spell_info)
            self.spell_info = ""

    def on_key_press(self, event):
        print(f"Naciśnięto klawisz: {event.keysym}")
        if not self.does_acted:
            key = event.keysym
            if key == "Up" and self.world.is_place_available(self, 0, -1):
                self.direction = Position(self.position.x, self.position.y - 1)
                self.does_acted = True
            elif key == "Down" and self.world.is_place_available(self, 0, 1):
                self.direction = Position(self.position.x, self.position.y + 1)
                self.does_acted = True
            elif key == "Left" and self.world.is_place_available(self, -1, 0):
                self.direction = Position(self.position.x - 1, self.position.y)
                self.does_acted = True
            elif key == "Right" and self.world.is_place_available(self, 1, 0):
                self.direction = Position(self.position.x + 1, self.position.y)
                self.does_acted = True
            elif key.lower() == "s" and not self.spell_active:
                self.activate_spell()
                self.does_acted = True
