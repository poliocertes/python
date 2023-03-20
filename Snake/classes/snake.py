# snake file
import random as rn
from classes.settings import *


class Snake:
    def __init__(self):
        self.color = SNAKE_COLOR
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.width = 25
        self.height = 25
        self.x_vel = 3
        self.y_vel = 0
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        self.snake = []

    def move_left(self):
        if self.x_vel < 3:
            self.y_vel = 0
            self.x_vel = -3

    def move_right(self):
        if self.x_vel > -3:
            self.y_vel = 0
            self.x_vel = 3

    def move_up(self):
        if self.y_vel < 3:
            self.y_vel = -3
            self.x_vel = 0

    def move_down(self):
        if self.y_vel > -3:
            self.y_vel = 3
            self.x_vel = 0

    def draw(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
        self.x += self.x_vel
        self.y += self.y_vel
