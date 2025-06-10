import tkinter as tk
from tkinter import Canvas, Text, END

from AllParams.Position import Position


class GameWindow:
    TILE_SIZE = 30

    def __init__(self, game, world):
        self.game = game
        self.world = world

        self.root = tk.Tk()
        self.root.title("Symulacja świata")

        self.canvas = Canvas(
            self.root,
            width=world.size_x * self.TILE_SIZE,
            height=world.size_y * self.TILE_SIZE,
            bg="white"
        )
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_canvas_click)

        self.event_log = Text(self.root, height=20, width=50, state="disabled", wrap="word")
        self.event_log.pack(pady=10)

        self.next_turn_button = tk.Button(self.root, text="Następna tura", command=self.next_turn)
        self.next_turn_button.pack(pady=10)

        self.save_button = tk.Button(self.root, text="Zapisz", command=game.save_game)
        self.save_button.pack(pady=10)

        self.read_button = tk.Button(self.root, text="Wczytaj", command=self.read_game)
        self.read_button.pack(pady=10)

        self.tour_label = tk.Label(self.root, text="Tura: 0")
        self.tour_label.pack()

        self.draw_world()


    def read_game(self):
        self.game.read_game()
        self.draw_world()


    def draw_world(self):
        self.canvas.delete("all")

        for organism in self.world.get_organisms():
            x = organism.position.x - 1
            y = organism.position.y - 1
            self.draw_square(x, y, organism.look)

    def draw_square(self, x, y, color):
        x1 = x * self.TILE_SIZE
        y1 = y * self.TILE_SIZE
        x2 = x1 + self.TILE_SIZE
        y2 = y1 + self.TILE_SIZE
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")

    def next_turn(self):
        self.game.next_round()
        self.tour_label.config(text=f"Tura: {self.game.tour}")
        self.draw_world()
        self.update_event_log(self.game.events)

    def set_new_world(self, world):
        self.world = world
        self.canvas.config(
            width=self.world.size_x * self.TILE_SIZE,
            height=self.world.size_y * self.TILE_SIZE
        )
        self.draw_world()

    def update_event_log(self, events):
        self.event_log.config(state="normal")
        self.event_log.delete("1.0", END)
        for event in events:
            self.event_log.insert(END, event + "\n")
        self.event_log.config(state="disabled")

    def on_canvas_click(self, event):
        tile_x = event.x // self.TILE_SIZE + 1
        tile_y = event.y // self.TILE_SIZE + 1

        self.open_tile_menu(tile_x, tile_y)

    def open_tile_menu(self, x, y):
        popup = tk.Toplevel(self.root)
        popup.geometry("400x400")
        popup.title(f"Dodaj organizm na ({x}, {y})")

        add_plant_button = tk.Button(popup, text="Wilk", command=lambda: (self.world.create_organism(11, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Owca", command=lambda: (self.world.create_organism(12, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Lis", command=lambda: (self.world.create_organism(13, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Żółw", command=lambda: (self.world.create_organism(14, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Antylopa", command=lambda: (self.world.create_organism(15, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Trawa", command=lambda: (self.world.create_organism(21, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Mlecz", command=lambda: (self.world.create_organism(22, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Guarana", command=lambda: (self.world.create_organism(23, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Wilcze jagody", command=lambda: (self.world.create_organism(24, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

        add_plant_button = tk.Button(popup, text="Barszcz Sosnowskiego", command=lambda: (self.world.create_organism(25, Position(x, y)), popup.destroy()))
        add_plant_button.pack(pady=3)

