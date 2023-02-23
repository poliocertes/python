# snake's food

from classes.settings import *
import random


class Food(object):
    def __init__(self):
        self.x_cord = random.randint(15, 730)
        self.y_cord = random.randint(15, 1155)
        self.width = 25
        self.height = 25
        self.foods = []
        self.color = FOOD_COLOR

    def draw_food(self):
        pg.draw.rect(screen, self.color, (self.x_cord, self.y_cord, self.width, self.height), border_radius=10)

