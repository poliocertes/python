# -- player file --

from classes.settings import *


class Player:
    def __init__(self, map):
        self.x = WIDTH / 2
        self.y = (HEIGHT / 2) + 10
        self.width = 25
        self.height = 25
        self.color = PLAYER_COLOR
        self.vel = 1
        self.map = map
        self.player_image = pg.image.load('assets/pacman_icon.png')
        self.left_player_image = pg.transform.flip(self.player_image, True, False)
        # self.up_player_image =
        # self.down_player_image =

    def move(self):
        keys = pg.key.get_pressed()
        # to napisał Michał Jabłoński :) -- >
        if keys[pg.K_UP] or keys[pg.K_w]:
            self.y -= self.vel

        if keys[pg.K_DOWN] or keys[pg.K_s]:
            self.y += self.vel

        if keys[pg.K_LEFT] or keys[pg.K_a]:
            self.x -= self.vel
            self.player_image = self.left_player_image

        if keys[pg.K_RIGHT] or keys[pg.K_d]:
            self.x += self.vel
            self.player_image = self.player_image
        # < -- to napisał Michał Jabłoński :)

    def draw(self):
        screen.blit(self.player_image, (self.x, self.y))
        #pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
