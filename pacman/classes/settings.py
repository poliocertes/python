# -- settings file --

import pygame as pg

WIDTH = 750
HEIGHT = 1200
RES = WIDTH, HEIGHT
FPS = 0
BG_COLOR = '#005500'
PLAYER_COLOR = '#CC6600'
BLOCK_SIZE = 50
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
RED = (255,0,0)

screen = pg.display.set_mode([WIDTH, HEIGHT])
red_ghost_image = pg.image.load('assets/ghost_red.png')
blue_ghost_image = pg.image.load('assets/ghost_blue.png')
green_ghost_image = pg.image.load('assets/ghost_green.png')
player_image = pg.image.load('assets/pacman/pacman01.png')

icon_size = (48, 48)

RED_GHOST = pg.transform.scale(red_ghost_image, icon_size)
BLUE_GHOST = pg.transform.scale(blue_ghost_image, icon_size)
GREEN_GHOST = pg.transform.scale(green_ghost_image, icon_size)
PLAYER = pg.transform.scale(player_image, icon_size)