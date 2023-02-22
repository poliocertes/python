# board file

import sys
from classes.settings import *
from classes.snake import Snake


class Board(object):
    def __init__(self):
        pg.display.set_caption('SNAKE')
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        self.snake = Snake()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.clock.tick(FPS)

    def draw(self):
        self.screen.fill(color=BG_COLOR)
        pg.display.flip()

    def run(self):
        while True:
            self.check_events()
            self.draw()
            self.update()

