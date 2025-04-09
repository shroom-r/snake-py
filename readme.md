# Python snake project

CAS-IDD 2025 / Python

Rafael Teixeira & Ayman Akram

## Project goal
The goal of this project is to explore the basic concepts of python and object oriented programming learned in CAS-IDD Python course.

We choose to create a game inspired on the well-known snake from 90's-2000's Nokia phones.

The base is the same : The snake can move in four directions inside a rectangle. It has to eat snacks, growing one unit each time it does. The game ends when the snake fills the entire rectangle (win) or if it collides with the walls or with its body (lose).

## Dependencies
[Unicurses](https://github.com/unicurses/unicurses)

## Initialize the game
1. Clone git repo
2. Move to snake-py folder
3. Create virtual env. with `python -m venv .venv`
4. Activate virtual env with `source .venv/Scripts/activate` if you are on Windows or with another command depending on the system : [Commands](https://docs.python.org/3/library/venv.html#how-venvs-work)
5. Install dependencies with `pip install -r requirements.txt`
6. Make sure the terminal is large enough (fullscreen recommended) and [Run game](#run-game)

Learn more about virtual env :
[Documentation](https://docs.python.org/3/library/venv.html#creating-virtual-environments)

## Run the game
1. Run the game with `python main.py`
