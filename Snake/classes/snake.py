# snake file

from classes.settings import *


class Snake(object):
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.width = 15
        self.height = 15
        self.x_vel = 0
        self.y_vel = 1
        self.snake = []

    def draw(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, SNAKE_COLOR,(self.x, self.y, self.width, self.height), border_radius=10)

    def run(self):
        self.y += self.y_vel
        self.x += self.x_vel

    def move_left(self):
        if self.x_vel < 1:
            self.y_vel = 0
            self.x_vel = -1

    def move_right(self):
        if self.x_vel > -1:
            self.y_vel = 0
            self.x_vel = 1

    def move_up(self):
        if self.y_vel < 1:
            self.y_vel = -1
            self.x_vel = 0

    def move_down(self):
        if self.y_vel > -1:
            self.y_vel = 1
            self.x_vel = 0
