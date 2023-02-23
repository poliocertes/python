# snake file

from classes.settings import *


class Snake(object):
    def __init__(self):
        self.x_cord = WIDTH/2
        self.y_cord = HEIGHT/2
        self.width = 25
        self.height = 25
        self.color = SN_HEAD_COLOR
        self.body_color = SN_TAIL_COLOR
        self.vel = 2

    def draw(self):
        pg.draw.rect(screen, self.color,(self.x_cord, self.y_cord, self.width, self.height), border_radius=8)

    def run(self):
        self.x_cord += self.vel

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass

