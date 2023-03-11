# setings file

import pygame as pg

WIDTH = 1200
HEIGHT = 800
# SCREEN_BG = pg.image.load('assets/grass.jpg')
BG_COLOR = '#336600'
FPS = 120
SNAKE_COLOR = '#009900'

clock = pg.time.Clock()
pg.init()
pg.display.set_caption("Game")
pg.mouse.set_visible(False)
screen = pg.display.set_mode([WIDTH, HEIGHT])


