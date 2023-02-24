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
        self.snake_body = []
        self.y_vel = 2
        self.x_vel = 0

    def draw(self):
        pg.draw.rect(screen, self.color,(self.x_cord, self.y_cord, self.width, self.height), border_radius=10)

    def move_left(self):
        if self.x_vel < SPEED:
            self.y_vel = 0
            self.x_vel = -SPEED

    def move_right(self):
        if self.x_vel > - SPEED:
            self.y_vel = 0
            self.x_vel = SPEED

    def move_up(self):
        if self.y_vel < SPEED:
            self.y_vel = - SPEED
            self.x_vel = 0

    def move_down(self):
        if self.y_vel > - SPEED:
            self.y_vel = SPEED
            self.x_vel = 0

# collision with no wall detection.
    def check_collision(self):
        if self.y_cord > 720:
            self.y_cord = 0
        elif self.y_cord < 0:
            self.y_cord = 720

        if self.x_cord > 1200:
            self.x_cord = 0
        elif self.x_cord < 0:
            self.x_cord = 1200

    def run(self):
        self.y_cord += self.y_vel
        self.x_cord += self.x_vel
