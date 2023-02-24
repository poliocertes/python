# board file

import sys
from classes.settings import *
from classes.snake import Snake
from classes.food import Food


class Board(object):
    def __init__(self):
        pg.display.set_caption('SNAKE')
        self.clock = CLOCK
        self.snake = Snake()
        self.food = Food()
        self.score = 22

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
        self.snake.check_wall_collision()

    def show_score(self):
        show_score = pg.font.Font.render(pg.font.SysFont('Arial Bold', 40), f'Score: {self.score}', True, (255, 255, 255))
        screen.blit(show_score, (15, 760))

    def check_snake_food_col(self):
        if self.snake.x_cord == self.food.x_cord and self.snake.y_cord == self.food.y_cord:
            print('T')

    def draw_board(self):
        screen.fill(color=BG_COLOR)
        self.food.draw_food()
        self.check_snake_food_col()
        self.show_score()
        self.snake.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.draw_board()
            self.check_events()
            self.update()

