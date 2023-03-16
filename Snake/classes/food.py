# food file

import random as rn
from classes.settings import *


class Food(object):
    def __init__(self):
        self.x = rn.randint(15, WIDTH - 15)
        self.y = rn.randint(15, HEIGHT - 75)
        self.width = 25
        self.height = 25
        self.color = FOOD_COLOR
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        self.food = []

    def create_food(self):
        food = pg.draw.rect(screen, self.color,(self.x, self.y, self.width, self.height))
        if len(self.food) < 1:
            self.food.append(food)

    def draw_food(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        for food in self.food:
            pg.draw.rect(screen, self.color, food, border_radius=10)
