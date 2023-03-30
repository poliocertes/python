# -- player file --

from classes.settings import *


class Player:
    def __init__(self, game):
        self.x = WIDTH / 2
        self.y = (HEIGHT / 2) + 10
        self.game = game
        self.player_image = pg.image.load('assets/pacman/pacman01.png')
        self.width = self.player_image.get_width()
        self.height = self.player_image.get_height()
        self.color = PLAYER_COLOR
        self.map = map
        self.player_image = pg.image.load('assets/pacman/pacman01.png')
        self.left_side_image = pg.transform.flip(self.player_image, True, False)
        self.right_side_image = self.player_image
        self.up_side_image = pg.transform.rotate(self.player_image, 90)
        self.down_side_image = pg.transform.rotate(self.player_image, -90)

    def check_free_place(self, x, y):
        print(x, y)
        return(x, y) not in self.game.map.world_map

    def check_collision(self, x_vel, y_vel):
        if self.check_free_place(int(self.x + x_vel), int(self.y)):
            self.x += x_vel
        elif self.check_free_place(int(self.x), int(self.y + y_vel)):
            self.y += y_vel

    def move(self):
        x_vel = 1.5
        y_vel = 1.5
        keys = pg.key.get_pressed()

        # to napisał Michał Jabłoński :) -- >
        
        if (self.x, self.y) in self.game.map.world_map:
            print('IN')
        else:
            if keys[pg.K_UP] or keys[pg.K_w]:
                if self.y > BLOCK_SIZE:
                    self.check_collision(x_vel, y_vel)
                    self.y -= y_vel
                    self.player_image = self.up_side_image

            if keys[pg.K_DOWN] or keys[pg.K_s]:
                if self.y < HEIGHT - BLOCK_SIZE - self.height:
                    self.y += y_vel
                    self.player_image = self.down_side_image

            if keys[pg.K_LEFT] or keys[pg.K_a]:
                if self.x > 50:
                    self.x -= x_vel
                    self.player_image = self.left_side_image

            if keys[pg.K_RIGHT] or keys[pg.K_d]:
                if self.x < (WIDTH - BLOCK_SIZE) - self.width:
                    self.x += x_vel
                    self.player_image = self.right_side_image

        # # < -- to napisał Michał Jabłoński :)

    def draw(self):
        screen.blit(self.player_image, (self.x, self.y))
        # pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), border_radius=15)
