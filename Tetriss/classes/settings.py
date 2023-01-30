# settings

import pygame as pg

vec = pg.math.Vector2

WIDTH = 600
HEIGHT = 1000
BLUE = (0, 0, 204)
GREEN = (0, 204, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
BLACK = (0, 0, 0)
PINK = (255, 0, 255)
BROWN = (222, 184, 135)
BLOCK_SIZE = 50
ROWS = 8
COLS = 16
FPS = 240

INITIAL_POSITION_OFFSET = vec((8//2)-1, 0)
MOVE_OPTIONS = {'left': vec(-1, 0), 'right': vec(1, 0), 'down': vec(0, 1)}

FIGURES = {
    'T': [(0, 0), (-1, 0), (1, 0), (0, -1)],
    'O': [(0, 0), (0, -1), (1, 0), (1, -1)],
    'J': [(0, 0), (-1, 0), (0, -1), (0, -2)],
    'L': [(0, 0), (1, 0), (0, -1), (0, -2)],
    'I': [(0, 0), (0, 1), (0, -1), (0, -2)],
    'S': [(0, 0), (-1, 0), (0, -1), (1, -1)],
    'Z': [(0, 0), (1, 0), (0, -1), (-1, -1)]
}

