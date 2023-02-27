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
        self.score = 0

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

    def create_food(self):
        if len(self.food.foods) >=3:
            pass
        else:
            self.food.foods.append(self.food)

    def show_score(self):
        show_score = pg.font.Font.render(pg.font.SysFont('Arial Bold', 40), f'Score: {self.score}', True, (0, 0, 0))
        screen.blit(show_score, (15, 760))

    def draw_board_end(self):
        pg.draw.rect(screen, 'black', pg.Rect(0, 740, 1200, 3))

    def draw_board(self):
        screen.fill(color=BG_COLOR)
        self.show_score()
        self.snake.draw()
        self.draw_board_end()
        pg.display.flip()

    def run(self):
        while True:
            self.draw_board()
            self.check_events()
            self.update()

