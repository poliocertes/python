# -- game file --

from classes.settings import *
from classes.map import Map
from classes.player import Player


class Game:
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.map = Map()
        self.player = Player(self)
        pg.display.set_caption('PACMAN')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        pg.display.flip()

    def draw(self):
        screen.fill(BG_COLOR)
        self.player.draw()
        self.map.draw()

    def run(self):
        while True: 
            self.check_events()
            self.player.move()
            self.update()
            self.draw()

