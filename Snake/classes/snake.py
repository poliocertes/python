# snake file


from classes.settings import *


class Snake(object):
    def __init__(self):
        self.x = WIDTH / 2
        self.y = HEIGHT / 2
        self.width = 25
        self.height = 25
        self.color = SNAKE_HD_COLOR
        self.x_vel = 0
        self.y_vel = 2
        self.snake = []
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)

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

    def check_wall_collision(self):
        if self.x < 0:
            self.x = WIDTH
        if self.x > WIDTH:
            self.x = 0
        if self.y < 0:
            self.y = HEIGHT - 65
        if self.y > HEIGHT - 65:
            self.y = 0

    def create_snake(self):
        snake_body = pg.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height))
        self.snake.append(snake_body)

    def draw_snake(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        # for item in self.snake:
        pg.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height), border_radius=10)
        self.x += self.x_vel
        self.y += self.y_vel



