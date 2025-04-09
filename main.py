import unicurses
from Controller import Controller

def main():
    '''
    Initializes unicurses and
    Creates a Controller object and launches its run() method.
    '''
    print('Select snake.')
    print('1: Normal snake. Weak, loses on every collision')
    print('2: Agile snake. Is agile. Jumps over its own body (some times at least...)')
    snakeId = input("Enter number and press Enter: ")

    stdscr = unicurses.initscr()
    unicurses.start_color()
    unicurses.init_pair(1, unicurses.COLOR_GREEN, unicurses.COLOR_BLACK)
    unicurses.init_pair(2, unicurses.COLOR_RED, unicurses.COLOR_BLACK)  
    unicurses.init_pair(3, unicurses.COLOR_YELLOW, unicurses.COLOR_BLACK)
    unicurses.clear()
    unicurses.cbreak()
    unicurses.noecho()
    unicurses.curs_set(0)
    unicurses.nodelay(stdscr, True)
    unicurses.keypad(stdscr, True)

    # Instanciate controller and run game
    ctrl = Controller(stdscr, snakeId)


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
