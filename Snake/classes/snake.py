# snake file

from classes.settings import *


class Snake(object):
    def __init__(self):
        self.x_cord = WIDTH/2
        self.y_cord = HEIGHT/2
        self.width = 5
        self.height = 5
        self.color = SN_HEAD_COLOR
        self.body_color = SN_TAIL_COLOR
        self.vel = 2

    def draw(self):
        pg.draw.rect(self.screen, self.color, (self.x_cord, self.y_cord))

    def run(self):
        pass

