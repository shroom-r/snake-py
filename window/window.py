import unicurses as curses


class Window:
    '''
    Creates the game window (with borders)
    Displays the snake, snack bar, and score
    Manages keyboard input'''
    def __init__(self, width, height, x, y, hasBorder):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.win = curses.newwin(height, width, y, x)
        if hasBorder:
            curses.box(self.win, 0, 0)
        
        self.refreshWindow()

    def drawChar(self, x, y, char):
        curses.mvwaddstr(self.win, y, x, char)
    
    def eraseChar(self, x, y):
        curses.mvwaddstr(self.win, y, x, " ")

    def refreshWindow(self):
        curses.wrefresh(self.win)
