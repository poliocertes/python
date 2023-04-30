import sys
from classes.settings import *


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption("Snake")
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def screen_update(self):
        pass

    def draw(self):
        self.screen.fill(BG_COLOR)
        pg.display.update()

    def run(self):
        while True:
            self.check_events()
            self.draw()
