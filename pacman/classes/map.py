# -- map file --

from classes.settings import *

x = False

first_map = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1],
    [1, x, 1, 1, 1, 1, 1, x, x, 1, 1, 1, 1, 1, x, 1],
    [1, x, 1, x, x, x, x, x, x, x, x, x, x, 1, x, 1],
    [1, x, 1, x, 1, 1, 1, x, x, 1, 1, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 1, 1, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, x, 1, x, 1, x, 1, x, 1],
    [1, x, x, x, x, x, 1, 1, 1, 1, x, x, x, x, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, x, x, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, x, x, x, x, 1, 1, 1, 1, x, x, x, x, x, 1],
    [1, x, 1, x, 1, x, 1, 2, 2, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 2, 2, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, 1, 1, 1, 1, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, x, x, x, x, x, x, 1, x, 1, x, 1],
    [1, x, 1, x, 1, 1, 1, x, x, 1, 1, 1, x, 1, x, 1],
    [1, x, 1, x, x, x, x, x, x, x, x, x, x, 1, x, 1],
    [1, x, 1, 1, 1, 1, 1, x, x, 1, 1, 1, 1, 1, x, 1],
    [1, x, x, x, x, x, x, x, x, x, x, x, x, x, x, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
] 


class Map:
    def __init__(self):
        self.board_map = first_map
        # self.world_map = {}
        self.game_map = []
        self.rows = len(self.board_map)
        self.cols = len(self.board_map[0])
        self.draw_map()

    # def create_map(self):
    #     for j, row in enumerate(self.board_map):
    #         for i, value in enumerate(row):
    #             if value:
    #                 self.world_map[(i, j)] = value

    # def draw(self):
        # [pg.draw.rect(screen, 'black', (pos[0] * 51, pos[1] * 51, BLOCK_SIZE, BLOCK_SIZE), 1)
        #  for pos in self.world_map]
    def draw_map(self):
        for i, row in enumerate(self.board_map):
            for j, item in enumerate(row):
                if item == 1:
                    pg.draw.rect(screen, BLUE, ((j*50)-25, (i*50)-25, BLOCK_SIZE, BLOCK_SIZE))
                elif item == x:
                    pg.draw.circle(screen, RED, (j*50, i*50), 7)
                elif item == 2:
                    pass


