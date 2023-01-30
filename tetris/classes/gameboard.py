# gameboard class

import pygame as pg
from settings import *


class GameBoard:
    def __init__(self):
        self.rows = 10
        self.cols = 20
        self.block_size = BLOCK_SIZE

    def draw_grid(self):
        from main import screen
        for i in range(self.cols):
            for j in range(self.rows):
                pg.draw.rect(screen, 'black', (j * self.block_size, i * self.block_size, 50, 50), 1)


