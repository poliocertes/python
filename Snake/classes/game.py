# game file

from classes.settings import *
from classes.snake import Snake
from classes.food import Food


class Game:
    def __init__(self):
        pg.display.set_caption('Game')
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.snake.move_left()

                if event.key == pg.K_RIGHT:
                    self.snake.move_right()

                if event.key == pg.K_UP:
                    self.snake.move_up()

                if event.key == pg.K_DOWN:
                    self.snake.move_down()

    def check_collision(self):
        for food in self.food.food:
            if self.snake.hitbox.colliderect(self.food.hitbox):
                self.food.food.remove(food)
                self.food.color = 'black'

    def update(self):
        self.clock.tick(FPS)
        self.snake.check_wall_col()
        self.check_collision()

    def draw(self):
        screen.fill(BG_COLOR)
        self.snake.draw()
        self.food.draw()
        pg.display.update()

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()
