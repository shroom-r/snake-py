import unicurses as curses
from time import sleep
from snake import Snake

class Controller:
    '''
    Game controller class.
    Catches user inputs and make all classes work together.
    Sets timing for snake moves, controls snake eating snack, etc.
    '''
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.snake = Snake()
        self.width = 50
        self.height = 50
        pass

    def run(self):
        '''
        Main method.
        Runs the game loop
        '''
        # Build game window
        win = curses.newwin(self.height ,self.width,1,0)
        curses.box(win,0,0) # Set border
        curses.nodelay(win, True)
        running = True
        curses.keypad(win,True)
        curses.notimeout(win, True)

        # Draw snake
        coordinates = self.snake.coordinates
        for coordinate in coordinates:
            curses.mvwaddstr(win, coordinate[1], coordinate[0], "0")
        curses.wrefresh(win)
        # Countdown to game start
        for i in range(5,0,-1):
            curses.mvwaddstr(win,1,1,f"Game will starts in {i}")
            curses.wrefresh(win)
            sleep(1)
        # Clear countdown
        for i in range(1,self.width - 1):
            curses.mvwaddstr(win,1,i," ")
            curses.wrefresh(win)
        
        while (running):
            key = curses.wgetch(win)
            # Leave game on q key
            if (key == ord('q')):
                running = False
                break
            # Change snake direction based on key
            if key == curses.KEY_UP:
                self.snake.setDirection("up")
            if key == curses.KEY_RIGHT:
                self.snake.setDirection("right")
            if key == curses.KEY_DOWN:
                self.snake.setDirection("down")
            if key == curses.KEY_LEFT:
                self.snake.setDirection("left")
            curses.flushinp()
            
            # Delete old snake tail position
            oldTailCoordinates = self.snake.getTailCoordinates()
            curses.mvwaddstr(win,oldTailCoordinates[1],oldTailCoordinates[0]," ")
            # Move snake and draw new head position
            self.snake.move()
            headCoordinates = self.snake.getHeadCoordinates()
            curses.mvwaddstr(win,headCoordinates[1],headCoordinates[0],self.snake.char)
            
            sleep(0.1)



if __name__ == "__main__":
    # Initiate curses
    stdscr = curses.initscr()
    curses.clear()
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True)
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0) # Hide cursor

    # Set title window
    titlewin = curses.newwin(1,50,0,0)
    curses.mvwaddstr(titlewin,0,0,"Snake PY")
    curses.wrefresh(titlewin)
    
    # Set command instructions window
    instrWin = curses.newwin(10,20,1,51)
    curses.box(instrWin,0,0)
    curses.mvwaddstr(instrWin,1,1,"Commands:")
    curses.mvwaddstr(instrWin,2,1,"q : quit")
    curses.wrefresh(instrWin)

    # Instanciate controller and run game
    ctrl = Controller(stdscr)
    try:
        ctrl.run()
    except KeyboardInterrupt:
        print("Game stopped !")
    finally:
        # Set terminal settings to default before leaving
        curses.nocbreak()
        curses.echo()
        curses.endwin()