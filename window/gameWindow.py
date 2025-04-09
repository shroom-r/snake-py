from window.window import Window
import unicurses
from time import sleep

class GameWindow(Window):
    '''
    Creates the game window (with borders)
    Displays the snake, snack bar, and score
    Manages keyboard input'''
    def __init__(self, width, height, x, y,hasBorder):
        super().__init__(width, height, x, y, hasBorder)
        unicurses.nodelay(self.win, True)
        unicurses.keypad(self.win, True)
        unicurses.notimeout(self.win, True)

    def draw_snake(self, coordinates, char):
        unicurses.wattron(self.win, unicurses.color_pair(1))
        for x, y in coordinates:
            self.drawChar(x, y, char)
        unicurses.wattroff(self.win, unicurses.color_pair(1))
        self.refreshWindow()

    def draw_snack(self, x, y, char):
        if char == '(':
            unicurses.wattron(self.win, unicurses.color_pair(3))
        else:
            unicurses.wattron(self.win, unicurses.color_pair(2))

        self.drawChar(x, y, char)

        unicurses.wattroff(self.win, unicurses.color_pair(2))
        unicurses.wattroff(self.win, unicurses.color_pair(3))

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
        return unicurses.wgetch(self.win)

    def clear_snack_area(self, x, y):
        self.eraseChar(x, y)
        self.refreshWindow()
        unicurses.mvwaddstr(self.win, y, x, " ")

    def write_points(self, points):
        unicurses.mvwaddstr(self.win, 0, 2, f"Points: {points}")
        unicurses.wrefresh(self.win)