# -- player file --

from classes.settings import *


class Player:
    def __init__(self, game):
        self.x = WIDTH/2 - 12
        self.y = BLOCK_SIZE + 25
        self.game = game
        self.color = PLAYER_COLOR
        self.map = map
        self.player_image = pg.image.load('assets/pacman/pacman01.png')
        self.left_side_image = pg.transform.flip(self.player_image, True, False)
        self.right_side_image = self.player_image
        self.up_side_image = pg.transform.rotate(self.player_image, 90)
        self.down_side_image = pg.transform.rotate(self.player_image, -90)
        self.width = self.player_image.get_width()

    def move(self):
        x_vel = 1
        y_vel = 1
        keys = pg.key.get_pressed()

        # to napisał Michał Jabłoński :) -- >

        if keys[pg.K_UP] or keys[pg.K_w]:
            self.y -= y_vel
            self.player_image = self.up_side_image

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.y += y_vel
            self.player_image = self.down_side_image

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.x -= x_vel
            self.player_image = self.left_side_image

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.x += x_vel
            self.player_image = self.right_side_image

        # # < -- to napisał Michał Jabłoński :)

    def draw(self):
        screen.blit(self.player_image, (self.x, self.y))


