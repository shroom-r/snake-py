import unicurses
from Controller import Controller

def main():
    '''
Initializes unicurses and
Creates a Controller object and launches its run() method.
    '''
    stdscr = unicurses.initscr()
    unicurses.cbreak()
    unicurses.noecho()
    unicurses.curs_set(0)
    unicurses.nodelay(stdscr, True)
    unicurses.keypad(stdscr, True)

    try:
        Controller(stdscr).run()
    finally:
        unicurses.endwin()

if __name__ == "__main__":
    main()
