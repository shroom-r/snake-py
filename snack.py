import random

class Snack:
    def __init__(self, screen_width, screen_height):
        self.all_positions = self.generate_all_positions(screen_width, screen_height)
        # On pré-calcule toutes les positions valides de la grille (sauf les bordures).
        # Cela ne se fait qu’une seule fois par pomme → très efficace.
        self.position = ()
    
    def generate_all_positions(self, width, height):
        # on crée une liste de tuples (x, y) représentant toutes les cases du plateau sauf les bordures.
        return [
            (x, y)
            for x in range(1, width - 2)
            for y in range(1, height - 2)
        ]

    def generate_position(self, snake_body):
        # Liste des positions libres
        available_positions = list(set(self.all_positions) - set(snake_body))
        # On utilise set() pour soustraire les deux listes, ce qui est très rapide 
        self.position = random.choice(available_positions)