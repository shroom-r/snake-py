from collections import deque

headChars = {
    "up" : "^",
    "down" : "v",
    "right" : ">",
    "left" : "<"
}

class Snake:
    '''
    Snake class manages snake functionalities.
    '''
    def __init__(self,windowWidth, windowHeight):
        '''
        Initializes snake coordinates and direction
        '''
        self.coordinates = deque(maxlen=5)
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.initialLength = 5
        for i in range(0, self.initialLength):
            self.coordinates.append( \
                ( \
                    windowWidth//2-self.initialLength//2+i, \
                    windowHeight//2 \
                ) \
            )
        self.deltaX = 1
        self.deltaY = 0
        self.direction = "right"

        self.nextHeadCoordinate = ()
        self.updateNextCoordinate()

        self.snakeMaxLength = (windowWidth-2) * (windowHeight-2)
        print(self.snakeMaxLength)
    
    def getPoints(self):
        return self.coordinates.maxlen - self.initialLength

    def setDirection(self, newDirection):
        '''
        Sets snake direction and updates deltaX and deltaY.
        Only allowes change going to the sides. It can not go backwards
        '''
        # Check if direction change is allowed (not going backwards)
        directionChangeAllowed = False
        if newDirection in ["left", "right"] and self.direction in ["up","down"] :
            directionChangeAllowed = True
        if newDirection in ["up","down"] and self.direction in ["left", "right"] :
            directionChangeAllowed = True
        
        if directionChangeAllowed:
            self.direction = newDirection
            self.deltaX = 0
            self.deltaY = 0
            if self.direction == "up":
                self.deltaY = -1
            if self.direction == "right":
                self.deltaX = 1
            if self.direction == "down":
                self.deltaY = 1
            if self.direction == "left":
                self.deltaX = -1
            self.updateNextCoordinate()

    def move(self):
        '''
        Moves snake 1 unit in current direction
        '''
        self.coordinates.append(self.nextHeadCoordinate)
        self.updateNextCoordinate()

    def updateNextCoordinate(self):
        self.nextHeadCoordinate = (
            self.coordinates[-1][0] + self.deltaX,
            self.coordinates[-1][1] + self.deltaY
        )

    def grow(self):
        '''
        Increases snake length by 1
        '''
        newLen = self.coordinates.maxlen + 1
        newCoordinates = deque(self.coordinates,maxlen=newLen)
        self.coordinates = newCoordinates

    def hasCollision(self):
        '''
        Checks if next position collides with snake body or
        with the walls
        '''
        return \
            self.nextHeadCoordinate in self.coordinates \
            or \
            not 1 <= self.nextHeadCoordinate[0] <= self.windowWidth -2 \
            or \
            not 1 <= self.nextHeadCoordinate[1] <= self.windowHeight -2

    def getHeadCoordinates(self):
        return self.coordinates[-1]
    
    def getTailCoordinates(self):
        return self.coordinates[0]
    
    def getHeadChar(self):
        return headChars[self.direction]
