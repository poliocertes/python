# settings file

import pygame as pg



BG_COLOR = '#006600'
SN_HEAD_COLOR = '#CC6600'
SN_TAIL_COLOR = '#0000CC'
FOOD_COLOR = '#FFFF66'

SNAKE_SPEED = 1

CLOCK = pg.time.Clock()

WIDTH = 1200
HEIGHT = 800
ROWS = 80
COLS = 120
FPS = 120

pg.init()
screen = pg.display.set_mode([WIDTH, HEIGHT])