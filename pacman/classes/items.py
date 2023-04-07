# ---game items file---

from classes.settings import *


class Ghost():
    def __init__(self):
        self.red_ghost_image = pg.image.load('assets/ghost_red.png')
        self.yellow_ghost_image = pg.image.load('assets/ghost_yellow.png')
        self.blue_ghost_image = pg.image.load('assets/ghost_blue.png')


class Food():
    def __init__(self):
        pass
