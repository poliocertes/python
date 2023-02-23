# board file

import sys
from classes.settings import *
from classes.snake import Snake


class Board(object):
    def __init__(self):
        pg.display.set_caption('SNAKE')
        self.clock = pg.time.Clock()
        self.snake = Snake()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_LEFT:
                    print('lewo')
                    self.snake.move_left()
                elif event.key == pg.K_RIGHT:
                    print('prawo')
                    self.snake.move_right()
                elif event.key == pg.K_UP:
                    print('góra')
                    self.snake.move_up()
                elif event.key == pg.K_DOWN:
                    print('dół')
                    self.snake.move_down()

    def update(self):
        self.clock.tick(FPS)
        self.snake.run()

    def draw(self):
        screen.fill(color=BG_COLOR)
        self.snake.draw()
        pg.display.flip()

    def run(self):
        while True:
            self.draw()
            self.check_events()
            self.update()

