# board file

import sys
from classes.settings import *
from classes.snake import Snake
from classes.food import Food


class Board(object):
    def __init__(self):
        pg.display.set_caption('SNAKE')
        self.clock = pg.time.Clock()
        self.snake = Snake()
        self.food = Food()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    self.snake.move_left()
                elif event.key == pg.K_RIGHT:
                    self.snake.move_right()
                elif event.key == pg.K_UP:
                    self.snake.move_up()
                elif event.key == pg.K_DOWN:
                    self.snake.move_down()

    def update(self):
        self.clock.tick(FPS)
        self.snake.run()
        self.snake.check_collision()

    def draw_board(self):
        screen.fill(color=BG_COLOR)
        self.food.draw_food()
        self.snake.draw()
        pg.draw.rect(screen, 'black', pg.Rect(0, 750, 1200, 2))
        pg.display.flip()

    def run(self):
        while True:
            self.draw_board()
            self.check_events()
            self.update()

