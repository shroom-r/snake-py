from window.window import Window
from window.gameWindow import GameWindow
import unicurses
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

        # Set title window
        titlewin = Window(50,1,0,0, False)
        titlewin.drawChar(0,0,"Snake PY")
        titlewin.refreshWindow()

        # Set command instructions window
        instrWin = Window(21, 10, 51, 1, True)
        instrWin.drawChar(1, 1, "Commands:")
        instrWin.drawChar(1, 2, "q : quit")
        instrWin.drawChar(1, 3, "arrows : move snake")
        instrWin.drawChar(1, 5, "Snacks:")
        instrWin.drawChar(1, 6, "o = normal (1pt)")
        instrWin.drawChar(1, 7, "Q = magic (3pt)")
        instrWin.refreshWindow()

        # Set informations window
        infoWin = Window(21, 10, 51, 11, True)
        infoWin.drawChar(1,1,"Informations:")
        infoWin.refreshWindow()
        self.infoWin = infoWin

        # Build game window
        self.window = GameWindow(self.width, self.height, 0, 1, True)

        self.running = True
        self.snakeThread = None

    def run(self):
        '''
        Runs the game loop
        '''
        # Draw initial snake
        self.window.draw_snake(self.snake.coordinates, self.snake.getHeadChar())

        self.writePoints()

        # Countdown to game start
        self.window.countdown()

        # Draw initial snack
        self.snack.generate_position(self.snake.coordinates)
        self.window.draw_snack(self.snack.position[0], self.snack.position[1], self.snack.char)
        
        # Run snake moving logic to another thread to keep the reactivity to key press while snake move loop sleeps
        self.snakeThread = threading.Thread(target=self.moveSnake)
        self.snakeThread.start()

        # Run game loop that essentially detects and reacts to key press
        while (self.running):
            key = self.window.get_key()
            # Leave game on q key
            if (key == ord('q')):
                self.running = False
                break
            if key in [
                unicurses.KEY_UP, \
                unicurses.KEY_RIGHT, \
                unicurses.KEY_DOWN, \
                unicurses.KEY_LEFT,
            ]:
                self.lastDirectionKey = key

    def writePoints(self):
        points = self.snake.getPoints()
        self.infoWin.drawChar(1,3,f"Points: {points}")
        self.infoWin.refreshWindow()

    def moveSnake(self):
        # executes in a thread → moves the snake, displays, updates the score
        if self.lastDirectionKey == unicurses.KEY_UP:
            self.snake.setDirection("up")
        elif self.lastDirectionKey == unicurses.KEY_RIGHT:
            self.snake.setDirection("right")
        elif self.lastDirectionKey == unicurses.KEY_DOWN:
            self.snake.setDirection("down")
        elif self.lastDirectionKey == unicurses.KEY_LEFT:
            self.snake.setDirection("left")

        # Check if next position has collision
        hasCollision = self.snake.hasCollision()
        if hasCollision:
            self.running = False
            return

        if self.hasSnack():
            # If head is on snack, grow snake and generate new 
            if (self.snack.isMagic):
                self.snake.grow(3)
            else:
                self.snake.grow()
            # If the snake reaches its max length, the game is win
            if self.snake.isWin():
                self.running = False
                print("Jeu gagné")
                return
            self.snack.generate_position(self.snake.coordinates)
            self.window.draw_snack(self.snack.position[0], self.snack.position[1], self.snack.char)
            # Move snake and draw new head position
            
        else:
            # Delete old snake tail position
            if not self.snake.isGrowing():
                oldTailCoordinates = self.snake.getTailCoordinates()
                self.window.clear_snack_area(oldTailCoordinates[0], oldTailCoordinates[1])
        # Move snake and draw new head position
        self.snake.move()
        self.writePoints()


        headChar = self.snake.getHeadChar()
        headCoordinates = self.snake.getHeadCoordinates()
        self.window.draw_snake([headCoordinates], headChar)
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