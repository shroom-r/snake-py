from snakes.snake import Snake

class AgileSnake(Snake):
    '''
    Snake that can collide with its body 2 times.
    The collision bonus is reset after eating 10 snacks
    '''
    def __init__(self,windowWidth, windowHeight):
        super().__init__(windowWidth, windowHeight)
        self.collsionsAllowed = 2
        self.eatenSnacksWithoutCollision = 0

    def hasCollision(self):
        '''
        Check if next position collides with body or wall.
        If eatenSnacksWithoutCollision equals 10, the collisionsAllowed count is initialised to 2.
        If it collides with body, collision is ignored it self.collisionsAllowed is not equal to 0.
        '''
        # Collision with wall ?
        if self.hasCollisionWithWall():
            return True

        # Initialise collisionsAllowed
        if self.eatenSnacksWithoutCollision >= 10:
            self.collsionsAllowed = 2
            self.eatenSnacksWithoutCollision = 0

        # Collision with body ?
        if self.hasCollisionWithBody():
            if self.collsionsAllowed:
                self.collsionsAllowed -= 1
                self.eatenSnacksWithoutCollision = 0
                return False
            else:
                return True
            
    def grow(self, increment=1):
        '''
        Grow means the snake has eaten a snack so the eatenSnackWithoutCollision can be incremented
        '''
        self.eatenSnacksWithoutCollision += 1
        return super().grow(increment)
    