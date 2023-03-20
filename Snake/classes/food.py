# food file
import random as rn
from classes.settings import *


class Food:
    def __init__(self):
        self.color = FOOD_COLOR
        self.x = rn.randint(15, WIDTH - 15)
        self.y = rn.randint(15, HEIGHT - 15)
        self.width = 25
        self.height = 25
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        self.food = []

    def create_food(self):
        food = pg.Rect(self.x, self.y, self.width, self.height)
        self.food.append(food)

    def draw(self):
        self.create_food()
        for food in self.food:
            pg.draw.rect(screen, self.color, food, border_radius=15)
