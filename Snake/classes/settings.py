# settings file

import pygame as pg

WIDTH = 1200
HEIGHT = 800
RES = WIDTH * HEIGHT
BG_COLOR = '#336633'
BG_IMAGE = pg.image.load("assets/grass.jpg")
FOOD_COLOR = '#CCCC00'
SNAKE_HD_COLOR = '#CC0000'
SNAKE_BD_COLOR = '#3399FF'
BOARD_BORDER_COLOR = '#000000'
FPS = 60

pg.init()
pg.display.set_caption('SNAKE')
screen = pg.display.set_mode([WIDTH, HEIGHT])


