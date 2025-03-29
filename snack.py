"""
Contient la classe Snack qui génère la position aléatoire de la pomme en évitant le serpent.
"""
import random
from point import Point #  classe utilitaire qui représente un point (Y, X) dans la grille du jeu.

class Snack:
    def __init__(self, screen_height, screen_width, snake_body): # screen_height et screen_width : taille de l'écran (hauteur et largeur).
        self.position = self.generate_position(screen_height, screen_width, snake_body)

    def generate_position(self, height, width, snake_body):
        while True:
            pos = Point(random.randint(1, height - 2), random.randint(1, width - 2))
            if pos not in snake_body: # pas sur le serpent
                return pos
