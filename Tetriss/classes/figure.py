# figure class

from classes.settings import *
import random


class Brick(pg.sprite.Sprite):
    def __init__(self, figure, pos):
        self.figure = figure
        self.pos = vec(pos) + INITIAL_POSITION_OFFSET
        super().__init__(figure.tetris.sprite_group)
        self.image = pg.Surface([BLOCK_SIZE, BLOCK_SIZE])
        pg.draw.rect(self.image, 'green', (1, 1, BLOCK_SIZE - 2, BLOCK_SIZE - 2), border_radius=8)
        self.rect = self.image.get_rect()

    def position(self):
        self.rect.topleft = self.pos * BLOCK_SIZE

    def update(self):
        self.position()
        pg.time.wait(200)

    def collision(self, pos):
        x, y = int(pos.x), int(pos.y)
        if 0 <= x < BLOCK_SIZE*8 and y < BLOCK_SIZE *16:
            return False
        return True


class Figure:
    def __init__(self, tetris):
        self.tetris = tetris
        self.shape = random.choice(list(FIGURES.keys()))
        self.bricks = [Brick(self, pos) for pos in FIGURES[self.shape]]

    def collison(self, brick_pos):
        return any(map(Brick.collision, self.bricks, brick_pos))

    def move_item(self, direction):
        move_dir = MOVE_OPTIONS[direction]
        new_position = [brick.pos + move_dir for brick in self.bricks]
        collision = self.collison(new_position)
        if not collision:
            for brick in self.bricks:
                brick.pos += move_dir

    def update(self):
        self.move_item(direction='down')

