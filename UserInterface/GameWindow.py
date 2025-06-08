import tkinter as tk
from tkinter import Canvas


class GameWindow:
    TILE_SIZE = 30  # Rozmiar pojedynczego pola (kwadratu)

    def __init__(self, game, world):
        self.game = game
        self.world = world

        self.root = tk.Tk()
        self.root.title("Symulacja świata")

        # Kanwa do rysowania organizmów
        self.canvas = Canvas(
            self.root,
            width=world.size_x * self.TILE_SIZE,
            height=world.size_y * self.TILE_SIZE,
            bg="white"
        )
        self.canvas.pack()

        # Przycisk do przejścia do kolejnej tury
        self.next_turn_button = tk.Button(self.root, text="Następna tura", command=self.next_turn)
        self.next_turn_button.pack(pady=10)


        self.save_button = tk.Button(self.root, text="Zapisz", command=game.save_game)
        self.save_button.pack(pady=10)


        self.read_button = tk.Button(self.root, text="Wczytaj", command=self.read_game)
        self.read_button.pack(pady=10)

        # Label na aktualną turę
        self.tour_label = tk.Label(self.root, text="Tura: 0")
        self.tour_label.pack()

        self.draw_world()


    def read_game(self):
        self.game.read_game()
        self.draw_world()


    def draw_world(self):
        self.canvas.delete("all")

        for organism in self.world.get_organisms():
            x = organism.position.x - 1  # tkinter zaczyna od 0
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

    def set_new_world(self, world):
        self.world = world
        self.canvas.config(
            width=self.world.size_x * self.TILE_SIZE,
            height=self.world.size_y * self.TILE_SIZE
        )
        self.draw_world()
