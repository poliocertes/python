# snake's food

from classes.settings import *
import random


class Food(object):
    def __init__(self):
        self.x_cord = random.randint(15, 1150)
        self.y_cord = random.randint(15, 710)
        self.width = 25
        self.height = 25
        self.foods = []
        self.food_color = FOOD_COLOR
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def create_food(self):
        if len(self.foods) >= 3:
            pass
        else:
            self.foods.append(Food)
            
    def draw_food_item(self):
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)
        for item in self.foods:
            pg.draw.rect(screen, self.food_color,(self.x_cord, self.y_cord, self.width, self.height), border_radius = 10)
                

