# snake file

from classes.settings import *


class Snake(object):
    def __init__(self):
        self.x = WIDTH/2
        self.y = HEIGHT/2
        self.width = 15
        self.height = 15
        self.x_vel = 1
        self.y_vel = 0

    def draw(self):
        pg.draw.rect(screen, SNAKE_COLOR,(self.x, self.y, self.width, self.height), border_radius=10)
        self.x += self.x_vel

    def move_left(self):
        pass

    def move_right(self):
        pass

    def move_up(self):
        pass

    def move_down(self):
        pass
