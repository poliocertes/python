# player file
import sys

from classes.settings import *


class Player(object):
    def __init__(self):
        pg.init()
        pg.display.set_caption('MP3 Player')
        self.screen = pg.display.set_mode(SCREEN_SIZE)
        self.clock = pg.time.Clock()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()

    def update(self):
        self.clock.tick(FPS)
        pg.display.update()

    def draw(self):
        self.screen.fill(color='green')
        pg.display.flip()

    def run(self):
        while True:
            self.check_event()
            self.update()
            self.draw()
