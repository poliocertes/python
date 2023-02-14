# game class
import sys

from classes.settings import *
from classes.tictactoe import Tictactoe


class Game:
    def __init__(self):
        pg.init()
        pg.display.set_caption('K & K')
        self.screen = pg.display.set_mode([WIDTH, HEIGHT])
        self.clock = pg.time.Clock()
        self.tictactoe = Tictactoe(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == pg.MOUSEBUTTONDOWN:
                current_pos = pg.mouse.get_pos()
                if current_pos[0] <= 180 and current_pos[1] < 180:
                    print('Field nr 1')
                elif 255 >= current_pos[0] > 180 > current_pos[1]:
                    print('Field nr 2')
                elif 255 < current_pos[0] < 330 and current_pos[1] < 180:
                    print('Field nr 3')
                elif current_pos[0] < 180 < current_pos[1] < 255:
                    print('Field nr 4')
                elif 180 < current_pos[0] < 255 and 180 < current_pos[1] < 255:
                    print('Field nr 5')
                elif 330 > current_pos[0] > 255 > current_pos[1] > 180:
                    print('Field nr 6')
                elif current_pos[0] < 180 and 255 < current_pos[1] < 330:  # from field 7
                    print('Field nr 7')
                elif 180 < current_pos[0] < 255 and current_pos[1] < 330:
                    print('Field nr 8')
                elif 255 < current_pos[0] < 330 and 255 < current_pos[1] < 330:
                    print('Field nr 9')

    def screen_update(self):
        self.clock.tick(FPS)

    def game(self):
        self.screen.fill(color=BOARD_COLOR)
        self.tictactoe.draw()
        pg.display.update()

    def run(self):
        while True:
            self.check_events()
            self.screen_update()
            self.game()
