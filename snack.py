"""
Contient la classe Snack qui génère la position aléatoire de la pomme en évitant le serpent.
"""
import random

class Snack:
    def __init__(self, screen_height, screen_width, snake_body):
        self.position = self.generate_position(screen_height, screen_width, snake_body)

    def generate_position(self, height, width, snake_body):
        # Génère une position aléatoire qui ne chevauche pas le serpent
        while True:
            pos = (random.randint(1, width - 2), random.randint(1, height - 2))
            if pos not in snake_body:
                return pos