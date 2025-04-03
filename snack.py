import random

class Snack:
    def __init__(self, screen_width, screen_height):
        self.all_positions = self.generate_all_positions(screen_width, screen_height)
        # We pre-calculate all valid grid positions (except borders).
        self.position = ()
    
    def generate_all_positions(self, width, height):
        # we create a list of tuples (x, y) representing all the squares on the board except the borders.
        return [
            (x, y)
            for x in range(1, width - 2)
            for y in range(1, height - 2)
        ]

    def generate_position(self, snake_body):
        available_positions = list(set(self.all_positions) - set(snake_body))
        # We use set() to subtract the two lists, which is very fast 
        self.position = random.choice(available_positions)