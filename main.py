import unicurses
from Controller import Controller

def main():
    '''
    Initializes unicurses and
    Creates a Controller object and launches its run() method.
    '''
    stdscr = unicurses.initscr()
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
