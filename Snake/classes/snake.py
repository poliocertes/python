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
        self.y_vel = 2
        self.x_vel = 0

    def draw(self):
        pg.draw.rect(screen, self.color,(self.x_cord, self.y_cord, self.width, self.height), border_radius=10)

    def move_left(self):
        if self.x_vel < 2:
            self.y_vel = 0
            self.x_vel = -2

    def move_right(self):
        if self.x_vel > -2:
            self.y_vel = 0
            self.x_vel = 2

    def move_up(self):
        if self.y_vel < 2:
            self.y_vel = -2
            self.x_vel = 0

    def move_down(self):
        if self.y_vel > -2:
            self.y_vel = 2
            self.x_vel = 0

    def run(self):
        self.y_cord += self.y_vel
        self.x_cord += self.x_vel


