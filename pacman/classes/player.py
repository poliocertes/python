# -- player file --

from classes.settings import *


class Player:
    def __init__(self, game):
        self.x = BLOCK_SIZE
        self.y = BLOCK_SIZE
        self.x_vel = 1
        self.y_vel = 1
        self.game = game
        self.color = PLAYER_COLOR
        self.player_image = PLAYER
        self.left_side_image = pg.transform.flip(self.player_image, True, False)
        self.right_side_image = self.player_image
        self.up_side_image = pg.transform.rotate(self.player_image, 90)
        self.down_side_image = pg.transform.rotate(self.player_image, -90)
        self.width = self.player_image.get_width()
        self.height = self.player_image.get_height()
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)

    def move(self):
        keys = pg.key.get_pressed()

        # to napisał Michał Jabłoński :) -- >

        if keys[pg.K_UP] or keys[pg.K_w]:
            if self.y >= BLOCK_SIZE:
                self.y -= self.y_vel
            self.player_image = self.up_side_image

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            if self.y <= HEIGHT - BLOCK_SIZE - self.height:
                self.y += self.y_vel
            self.player_image = self.down_side_image

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            if self.x >= BLOCK_SIZE:
                self.x -= self.x_vel
            self.player_image = self.left_side_image

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            if self.x <= WIDTH - BLOCK_SIZE - self.width:
                self.x += self.x_vel
            self.player_image = self.right_side_image

        # <-- to napisał Michał Jabłoński :)

    def draw(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        screen.blit(self.player_image, (self.x, self.y))
