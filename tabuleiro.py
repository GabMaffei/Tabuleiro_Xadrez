import numpy as np


class Tabuleiro:
    def __init__(self):
        self.tabuleiro = np.zeros([8, 8])

    def __str__(self):
        return str(self.tabuleiro)
