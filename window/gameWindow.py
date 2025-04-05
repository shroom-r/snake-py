from window.window import Window
import unicurses as curses
from time import sleep

class GameWindow(Window):
    '''
    Creates the game window (with borders)
    Displays the snake, snack bar, and score
    Manages keyboard input'''
    def __init__(self, width, height, x, y,hasBorder):
        super().__init__(width, height, x, y, hasBorder)
        curses.nodelay(self.win, True)
        curses.keypad(self.win, True)
        curses.notimeout(self.win, True)

    def draw_snake(self, coordinates, char):
        for x, y in coordinates:
            self.drawChar(x, y, char)
        self.refreshWindow()

    def draw_snack(self, x, y, char):
        self.drawChar(x, y, char)
        self.refreshWindow()

    def countdown(self):
        for i in range(5, 0, -1):
            self.drawChar(1, 1, f"Game will start in {i}")
            self.refreshWindow()
            sleep(1)
        for i in range(1, self.width - 1):
            self.eraseChar(i, 1)
        self.refreshWindow()

    def get_key(self):
        return curses.wgetch(self.win)

    def clear_snack_area(self, x, y):
        self.eraseChar(x, y)
        self.refreshWindow()
        curses.mvwaddstr(self.win, y, x, " ")

    def write_points(self, points):
        curses.mvwaddstr(self.win, 0, 2, f"Points: {points}")
        curses.wrefresh(self.win)