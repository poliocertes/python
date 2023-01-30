# game class

import sys


from classes.settings import *
from classes.tetris import Tetris


class Game:
    def __init__(self):
        pg.init()
        self.keys = pg.key.get_pressed()
        pg.display.set_caption('TETRIS')
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.logo = pg.image.load('assets/tetris.png')
        self.clock = pg.time.Clock()
        self.tetris = Tetris(self)
        
    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                self.tetris.control(key_press=event.key)

    def draw_logo(self):
        self.screen.blit(self.logo, (475, 50))

    def screen_update(self):
        self.tetris.update()
        self.clock.tick(FPS)

    def game(self):
        self.screen.fill(color=BROWN)
        self.tetris.draw()
        self.draw_logo()
        self.draw_logo()
        pg.display.update()

    def run(self):
        while True:
            self.check_event()
            self.screen_update()
            self.game()
            self.draw_logo()

