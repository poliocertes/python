# settings file

import pygame as pg

pg.init()

BG_COLOR = '#006600'
SN_HEAD_COLOR = '#CC6600'
SN_TAIL_COLOR = '#0000CC'
FOOD_COLOR = '#FFFF66'

SNAKE_SPEED = 3

CLOCK = pg.time.Clock()

WIDTH = 1200
HEIGHT = 800
ROWS = 80
COLS = 120
FPS = 75

screen = pg.display.set_mode([WIDTH, HEIGHT])