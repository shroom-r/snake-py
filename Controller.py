import unicurses as curses
from time import sleep
from snake import Snake
import threading
import random

class Controller:
    '''
    Game controller class.
    Catches user inputs and make all classes work together.
    Sets timing for snake moves, controls snake eating snack, etc.
    '''
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.width = 50
        self.height = 50
        self.snake = Snake(self.width, self.height)
        self.lastDirectionKey = None
        self.snakeWin = None
        self.running = True
        self.snakeThread = None

    def run(self):
        '''
        Main method.
        Runs the game loop
        '''
        # Build game window
        win = curses.newwin(self.height ,self.width,1,0)
        self.snakeWin = win
        curses.box(win,0,0) # Set border
        curses.wrefresh(win)
        curses.nodelay(win, True)
        curses.keypad(win,True)
        curses.notimeout(win, True)

        # Draw snake
        coordinates = self.snake.coordinates
        char = self.snake.getHeadChar()
        for coordinate in coordinates:
            curses.mvwaddstr(win, coordinate[1], coordinate[0], char)
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
        
        self.snakeThread = threading.Thread(target=self.moveSnake)
        self.snakeThread.start()

        while (self.running):
            key = curses.wgetch(win)
            # Leave game on q key
            if (key == ord('q')):
                self.running = False
                break
            if key in [
                curses.KEY_UP, \
                curses.KEY_RIGHT, \
                curses.KEY_DOWN, \
                curses.KEY_LEFT,
            ]:
                self.lastDirectionKey = key

    def moveSnake(self):
        if self.lastDirectionKey == curses.KEY_UP:
            self.snake.setDirection("up")
        if self.lastDirectionKey == curses.KEY_RIGHT:
            self.snake.setDirection("right")
        if self.lastDirectionKey == curses.KEY_DOWN:
            self.snake.setDirection("down")
        if self.lastDirectionKey == curses.KEY_LEFT:
            self.snake.setDirection("left")
        if self.isHeadOnSnack():
            self.snake.grow()
        else:
            # Delete old snake tail position
            oldTailCoordinates = self.snake.getTailCoordinates()
            curses.mvwaddstr(self.snakeWin,oldTailCoordinates[1],oldTailCoordinates[0]," ")
        # Check if next position has collision
        hasCollision = self.snake.hasCollision()
        if hasCollision:
            self.running = False
            return
        # Move snake and draw new head position
        self.snake.move()
        headChar = self.snake.getHeadChar()
        headCoordinates = self.snake.getHeadCoordinates()
        curses.mvwaddstr(self.snakeWin,headCoordinates[1],headCoordinates[0], headChar)
        if self.running:
            sleep(0.1)
            self.snakeThread = threading.Thread(target=self.moveSnake)
            self.snakeThread.start()
    
    def isHeadOnSnack(self):
        '''
        Returns True if snakes head has the same coordinates as snack
        '''
        # TO BE DEFINED, RETURNS TRUE OR FALSE RANDOMLY TO TEST

        return random.choice([True,False,False,False])




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
        print("Game interrupted !")
    except Exception as err:
        print(err)
    finally:
        ctrl.running = False
        # Set terminal settings to default before leaving
        curses.nocbreak()
        curses.echo()
        curses.endwin()