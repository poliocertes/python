# -- game file --

from classes.settings import *
from classes.map import Map
from classes.player import Player


class Game:
    def __init__(self):
        pg.init()
        self.map = Map()
        self.player = Player(self)
        self.clock = pg.time.Clock()
        pg.display.set_caption('pacman')

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def update(self):
        self.player.move()
        pg.display.flip()

    def draw(self):
        screen.fill(BG_COLOR)
        self.map.draw_map()
        self.player.draw()

    def run(self):
        while True: 
            self.check_events()
            self.update()
            self.draw()

