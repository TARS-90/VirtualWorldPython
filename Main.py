from AllParams.Game import Game

if __name__ == "__main__":
    # Parametry startowe
    size_x = 10   # szerokość świata
    size_y = 10   # wysokość świata
    num_animals = 5
    num_plants = 10

    # Utworzenie gry – otworzy się okno UI
    game = Game(size_x, size_y, num_animals, num_plants)
    game.game_window.root.mainloop()
