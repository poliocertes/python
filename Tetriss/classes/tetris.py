# tetris class

from classes.settings import *
from classes.figure import Figure


class Tetris:
    def __init__(self, game):
        self.game = game
        self.sprite_group = pg.sprite.Group()
        self.figure = Figure(self)

    def control(self, key_press):
        if key_press == pg.K_LEFT:
            self.figure.move_item(direction='left')
        elif key_press == pg.K_RIGHT:
            self.figure.move_item(direction='right')
        elif key_press == pg.K_DOWN:
            self.figure.move_item(direction='down')

    def draw_grid(self):
        for i in range(COLS):
            for j in range(ROWS):
                pg.draw.rect(self.game.screen, 'black', (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE), 1)

    def update(self):
        self.figure.update()
        self.sprite_group.update()

    def draw(self):
        self.draw_grid()
        self.sprite_group.draw(self.game.screen)
