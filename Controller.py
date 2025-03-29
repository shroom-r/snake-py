import unicurses as curses
from time import sleep
from snake import Snake
from snack import Snack

class Controller:
    def __init__(self, stdscr):
        self.stdscr = stdscr
        self.snake = Snake()
        self.width = 50
        self.height = 50
        self.snack = Snack(self.height, self.width, self.snake.coordinates)

    def run(self):
        '''
        Boucle principale du jeu : gère l'affichage, les entrées utilisateur,
        le déplacement du serpent, et les collisions avec la pomme ou les murs.
        '''
        win = curses.newwin(self.height, self.width, 1, 0)
        curses.box(win, 0, 0)
        curses.nodelay(win, True)
        curses.keypad(win, True)
        curses.notimeout(win, True)

        # Draw initial snake
        for coordinate in self.snake.coordinates:
            curses.mvwaddstr(win, coordinate[1], coordinate[0], self.snake.char)

        # Draw snack
        curses.mvwaddstr(win, self.snack.position[1], self.snack.position[0], "*")

        curses.wrefresh(win)

        for i in range(5, 0, -1):
            curses.mvwaddstr(win, 1, 1, f"Game starts in {i}")
            curses.wrefresh(win)
            sleep(1)
        for i in range(1, self.width - 1):
            curses.mvwaddstr(win, 1, i, " ")

        running = True
        while running:
            key = curses.wgetch(win)
            if key == ord('q'):
                running = False
                break
            elif key == curses.KEY_UP:
                self.snake.setDirection("up")
            elif key == curses.KEY_DOWN:
                self.snake.setDirection("down")
            elif key == curses.KEY_LEFT:
                self.snake.setDirection("left")
            elif key == curses.KEY_RIGHT:
                self.snake.setDirection("right")

            old_tail = self.snake.getTailCoordinates()
            self.snake.move()
            new_head = self.snake.getHeadCoordinates()

            # Collision check: wall
            if new_head[0] <= 0 or new_head[0] >= self.width - 1 or \
               new_head[1] <= 0 or new_head[1] >= self.height - 1:
                break

            # Collision check: self
            if new_head in list(self.snake.coordinates)[:-1]:
                break

            # Draw movement
            curses.mvwaddstr(win, old_tail[1], old_tail[0], " ")
            curses.mvwaddstr(win, new_head[1], new_head[0], self.snake.char)

            # Snack eaten
            if new_head == self.snack.position:
                # Si le serpent mange la pomme, on le fait grandir et on génère une nouvelle pomme
                self.snake.grow_snake()
                self.snack = Snack(self.height, self.width, self.snake.coordinates)
                curses.mvwaddstr(win, self.snack.position[1], self.snack.position[0], "*")

            curses.wrefresh(win)
            sleep(0.1)

if __name__ == "__main__":
    stdscr = curses.initscr()
    curses.clear()
    curses.noecho()
    curses.cbreak()
    curses.nodelay(stdscr, True)
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    titlewin = curses.newwin(1, 50, 0, 0)
    curses.mvwaddstr(titlewin, 0, 0, "Snake PY")
    curses.wrefresh(titlewin)

    instrWin = curses.newwin(10, 20, 1, 51)
    curses.box(instrWin, 0, 0)
    curses.mvwaddstr(instrWin, 1, 1, "Commands:")
    curses.mvwaddstr(instrWin, 2, 1, "q : quit")
    curses.wrefresh(instrWin)

    ctrl = Controller(stdscr)
    try:
        ctrl.run()
    except KeyboardInterrupt:
        print("Game stopped!")
    finally:
        curses.nocbreak()
        curses.echo()
        curses.endwin()
