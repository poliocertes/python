# -- map file --

from classes.settings import *

x = False

first_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, x, x, x, x, x, x, x, x, x, x, x, x, x, 1],
    [1, x, 1, 1, 1, x, 1, x, 1, x, 1, 1, 1, x, 1],
    [1, x, 1, x, x, x, x, x, x, x, x, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 1, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 3, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 3, 1, x, 1, x, 1, x, 1],
    [1, x, x, x, x, x, 1, 1, 1, x, x, x, x, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, x, x, x, x, 1, 1, 1, x, x, x, x, x, 1],
    [1, x, 1, x, 1, x, 1, 3, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 3, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 1, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, x, x, x, x, x, x, x, x, 1, x, 1],
    [1, x, 1, 1, 1, x, 1, x, 1, x, 1, 1, 1, x, 1],
    [1, x, x, x, x, x, x, x, x, x, x, x, x, x, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
] 


class Wall:
    def __init__(self):
        pass


class Ghost:
    def __init__(self):
        pass


class Food:
    def __init__(self):
        self.radius = 7
        self.color = RED

    def draw(self):
        pass


class Map:
    def __init__(self):
        self.wall = Wall
        self.ghost = Ghost
        self.food = Food
        self.board_map = first_map
        self.game_map = []
        self.rows = len(self.board_map)
        self.cols = len(self.board_map[0])
        self.red_ghost_image = pg.image.load('assets/ghost_red.png')
        self.draw_map()

    def draw_map(self):
        for i, row in enumerate(self.board_map):
            for j, item in enumerate(row):
                if item == x:
                    pg.draw.circle(screen, RED, ((j*50)+25, (i*50)+25), 7)
                elif item == 1:
                    pg.draw.rect(screen, BLUE, (j*50, i*50, BLOCK_SIZE, BLOCK_SIZE))
                elif item == 2:
                    pg.draw.rect(screen, BLACK, (j*50, i*50, BLOCK_SIZE-10, BLOCK_SIZE-10), border_radius=15)
                elif item == 3:
                    pass
