import pygame


class GameBall:
    COLOR = (255, 140, 0)

    def __init__(self, x, y, radius):
        self.x_cord = self.start_x = x
        self.y_cord = self.start_y = y
        self.radius = radius
        self.x_vel = 3
        self.y_vel = 4

    def draw(self):
        pygame.draw.circle(screen, self.COLOR, (self.x_cord, self.y_cord), self.radius)

    def move(self):
        self.x_cord += self.x_vel
        self.y_cord += self.y_vel

    def reset(self):
        self.x_cord = self.start_x
        self.y_cord = self.start_y