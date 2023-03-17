# game file

from classes.settings import *
from classes.snake import Snake
from classes.food import Food
import sys


class Game(object):
    def __init__(self):
        pg.display.set_caption('Game')
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food()
        self.score = 0

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.snake.move_left()
                if event.key == pg.K_RIGHT:
                    self.snake.move_right()
                if event.key == pg.K_UP:
                    self.snake.move_up()
                if event.key == pg.K_DOWN:
                    self.snake.move_down()

    def check_item_collision(self):
        for item in self.food.food:
            if self.food.hitbox.colliderect(self.snake.hitbox):
                self.food.food.remove(item)
                self.food.color = 'red'

    def draw_board_border(self):
        end_line = pg.draw.rect(screen, BOARD_BORDER_COLOR, (0, 750, 1200, 5))
        return end_line

    def update(self):
        self.snake.check_wall_collision()
        self.food.create_food()
        self.check_item_collision()
        self.clock.tick(FPS)

    def draw(self):
        screen.fill(color=BG_COLOR)
        self.food.draw_food()
        self.snake.draw_snake()
        self.draw_board_border()
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()
