import unicurses as curses



class Controller:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        pass

    def run(self):
        while True:
            curses.mvaddstr(10,100, "T")
            curses.refresh()

            
        
        

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    # curses.keypad(True)
    ctrl = Controller(stdscr)
    try:
        ctrl.run()
    except KeyboardInterrupt:
        print("Game stopped !")
    finally:
        curses.nocbreak()
        # curses.keypad(False)
        curses.echo()
        curses.endwin()