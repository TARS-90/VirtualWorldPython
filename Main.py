from AllParams.Game import Game

if __name__ == "__main__":
    # Starting parameters
    size_x = 10   # world width
    size_y = 10   # world height
    num_animals = 5
    num_plants = 10

    game = Game(size_x, size_y, num_animals, num_plants)
    game.game_window.root.mainloop()
