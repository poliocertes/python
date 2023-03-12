# food file

from classes.settings import *


class Food(object):
    def __init__(self):
        self.x = rn.randint(50, 1150)
        self.y = rn.randint(50, 750)
        self.width = 15
        self.height = 15
        self.foods = []
        self.food_color = FOOD_COLOR

    def add_food(self):
        if len(self.foods) >= 3:
            pass
        else:
            self.foods .append(Food)

    def draw_food(self):
        self.hitbox = pg.Rect(self.x, self.y, self.width, self.height)
        pg.draw.rect(screen, self.food_color,(self.x, self.y, self.width, self.height), border_radius=10)