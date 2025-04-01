import random

class Snack:
    def __init__(self, screen_height, screen_width, snake_body):
        self.all_positions = self.generate_all_positions(screen_height, screen_width)
        # On pré-calcule toutes les positions valides de la grille (sauf les bordures).
        # Cela ne se fait qu’une seule fois par pomme → très efficace.
        self.position = self.generate_position(snake_body)
        # On appelle une autre méthode pour choisir une position libre où placer la pomme.
    
    def generate_all_positions(self, height, width):
        # on crée une liste de tuples (x, y) représentant toutes les cases du plateau sauf les bordures.
        return [
            (x, y)
            for x in range(1, width - 1)
            for y in range(1, height - 1)
        ]

    def generate_position(self, snake_body):
        # Liste des positions libres
        available_positions = list(set(self.all_positions) - set(snake_body))
        # On utilise set() pour soustraire les deux listes, ce qui est très rapide 
        if not available_positions:
            raise ValueError("Plus de place pour générer une pomme !")
        return random.choice(available_positions)