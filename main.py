import unicurses
from Controller import Controller

def main():
    '''
    Initializes unicurses and
    Creates a Controller object and launches its run() method.
    '''
    stdscr = unicurses.initscr()
    unicurses.start_color()
    unicurses.init_pair(1, unicurses.COLOR_GREEN, unicurses.COLOR_BLACK)
    unicurses.init_pair(2, unicurses.COLOR_RED, unicurses.COLOR_BLACK)  
    unicurses.clear()
    unicurses.cbreak()
    unicurses.noecho()
    unicurses.curs_set(0)
    unicurses.nodelay(stdscr, True)
    unicurses.keypad(stdscr, True)

    # Instanciate controller and run game
    ctrl = Controller(stdscr)

    try:
        ctrl.run()
    except KeyboardInterrupt:
        print("Game interrupted !")
    finally:
        ctrl.running = False
        # Set terminal settings to default before leaving
        unicurses.nocbreak()
        unicurses.echo()
        unicurses.endwin()

if __name__ == "__main__":
    main()
