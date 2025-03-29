from collections import deque

class Snake:
    '''
    Snake class manages snake functionalities.
    '''
    def __init__(self):
        '''
        Initializes snake coordinates and direction
        '''
        self.coordinates = deque([ \
            (22,24), \
            (23,24), \
            (24,24), \
            (25,24), \
            (26,24), \
        ],5)
        self.direction = "up" # Dummy setup
        self.setDirection("right")

        self.char = 0
    
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

    def move(self):
        '''
        Moves snake 1 unit in current direction
        '''
        currX = self.coordinates[-1][0]
        currY = self.coordinates[-1][1]
        newCoordinates = (currX + self.deltaX, currY + self.deltaY)
        self.coordinates.append(newCoordinates)

    def getHeadCoordinates(self):
        return self.coordinates[-1]
    
    def getTailCoordinates(self):
        return self.coordinates[0]