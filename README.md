# Virtual World Simulator (Python)

An academic project implementing a turn-based virtual world simulator with a 2D grid structure of $N \times M$ dimensions. The world is inhabited by diverse life forms (both dynamic animal organisms and static plant organisms), each characterized by distinct behavior, unique statistics, and specific interactions.

The application has been fully implemented in Python, strictly adhering to the Object-Oriented Programming (OOP) paradigm and utilizing a graphical library to visualize the state of the board.

## 🚀 Key Features

* **Priority-Based Turn Mechanics:** The execution order of actions performed by organisms is determined by their initiative and age (the seniority principle applies in case of identical initiative values).
* **Advanced Collision System:** Combat resolution is based on strength (with the aggressor gaining the advantage in the event of a tie), alongside mechanics for animal reproduction and plant spreading.
* **Player Control (Human):** A unique, sequence-controlled character moved via arrow keys, equipped with a time-limited special ability that features a specific cooldown period.
* **Game State Management:** Full support for saving (Save) and loading (Load) the current state of the world to and from an external file.
* **Interactive Board:** The ability to dynamically add new organisms to the grid by clicking on empty cells with the mouse.
* **Event Log:** A dedicated text-based live feed reporting all key events happening on the map in real-time (such as combat results, births, or plants being consumed).
