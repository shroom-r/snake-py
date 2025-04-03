import unicurses as curses
from time import sleep

class Window:
    '''
    Creates the game window (with borders)
    Displays the snake, snack bar, and score
    Manages keyboard input'''
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.win = curses.newwin(self.height, self.width, 1, 0)
        curses.box(self.win, 0, 0)
        curses.wrefresh(self.win)
        curses.nodelay(self.win, True)
        curses.keypad(self.win, True)
        curses.notimeout(self.win, True)

    def draw_snake(self, coordinates, char):
        for x, y in coordinates:
            curses.mvwaddstr(self.win, y, x, char)

    def draw_snack(self, x, y):
        curses.mvwaddstr(self.win, y, x, "o")

    def countdown(self):
        for i in range(5, 0, -1):
            curses.mvwaddstr(self.win, 1, 1, f"Game will start in {i}")
            curses.wrefresh(self.win)
            sleep(1)
        for i in range(1, self.width - 1):
            curses.mvwaddstr(self.win, 1, i, " ")
        curses.wrefresh(self.win)

    def get_key(self):
        return curses.wgetch(self.win)

    def refresh(self):
        curses.wrefresh(self.win)

    def clear_snack_area(self, x, y):
        curses.mvwaddstr(self.win, y, x, " ")

    def write_points(self, points):
        curses.mvwaddstr(self.win, 0, 2, f"Points: {points}")
        curses.wrefresh(self.win)
