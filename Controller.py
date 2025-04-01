import unicurses as curses
from time import sleep
from snake import Snake
from snack import Snack
import threading

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
        self.snack = Snack(self.width, self.height)
        self.lastDirectionKey = None
        self.snakeWin = None
        self.running = True
        self.snakeThread = None

    def run(self):
        '''
        Main method.
        Runs the game loop
        '''
        global infoWin
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

        self.writePoints()

        # Countdown to game start
        for i in range(5,0,-1):
            curses.mvwaddstr(win,1,1,f"Game will start in {i}")
            curses.wrefresh(win)
            sleep(1)
        # Clear countdown
        for i in range(1,self.width - 1):
            curses.mvwaddstr(win,1,i," ")
            curses.wrefresh(win)

        # Draw snack
        self.snack.generate_position(self.snake.coordinates)
        curses.mvwaddstr(win, self.snack.position[1], self.snack.position[0], "o")
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

    def writePoints(self):
        global infoWin
        points = self.snake.getPoints()
        curses.mvwaddstr(infoWin,3,1,f"Points: {points}")
        curses.wrefresh(infoWin)

    def moveSnake(self):
        if self.lastDirectionKey == curses.KEY_UP:
            self.snake.setDirection("up")
        elif self.lastDirectionKey == curses.KEY_RIGHT:
            self.snake.setDirection("right")
        elif self.lastDirectionKey == curses.KEY_DOWN:
            self.snake.setDirection("down")
        elif self.lastDirectionKey == curses.KEY_LEFT:
            self.snake.setDirection("left")

        # Check if next position has collision
        hasCollision = self.snake.hasCollision()
        if hasCollision:
            self.running = False
            return

        if self.hasSnack():
            # If head is on snack, grow snake and generate new snack
            self.snake.grow()
            self.snack.generate_position(self.snake.coordinates)
            curses.mvwaddstr(self.snakeWin, self.snack.position[1], self.snack.position[0], "o")
            # Move snake and draw new head position
            
        else:
            # Delete old snake tail position
            oldTailCoordinates = self.snake.getTailCoordinates()
            curses.mvwaddstr(self.snakeWin,oldTailCoordinates[1],oldTailCoordinates[0]," ")
            # Move snake and draw new head position
        self.snake.move()
        self.writePoints()


        headChar = self.snake.getHeadChar()
        headCoordinates = self.snake.getHeadCoordinates()
        curses.mvwaddstr(self.snakeWin,headCoordinates[1],headCoordinates[0], headChar)
        if self.running:
            sleep(0.1)
            self.snakeThread = threading.Thread(target=self.moveSnake)
            self.snakeThread.start()
    
    def hasSnack(self):
        '''
        Returns True if snakes head will move on snack on next move
        '''
        newHeadCoordinate = self.snake.nextHeadCoordinate
        return newHeadCoordinate == self.snack.position

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

    # Set informations window
    infoWin = curses.newwin(10,20,11,51)
    curses.box(infoWin,0,0)
    curses.mvwaddstr(infoWin,1,1,"Informations:")
    curses.wrefresh(infoWin)

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
