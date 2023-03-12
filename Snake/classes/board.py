# snake file
import time
import sys

from pygame import K_UP, K_DOWN
from pygame.locals import K_LEFT, K_RIGHT

from classes.settings import *
from classes.snake import Snake
from classes.food import Food


class Board(object):
	def __init__(self):
		self.screen = pg.display.set_mode([WIDTH, HEIGHT])
		self.snake = Snake()
		self.food = Food()

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()

			keys = pg.key.get_pressed()
			if keys[K_LEFT]:
				self.snake.move_left()
			if keys[K_RIGHT]:
				self.snake.move_right()
			if keys[K_UP]: 
				self.snake.move_up()
			if keys[K_DOWN]:
				self.snake.move_down()

	def check_wall_collision(self):
		if self.snake.x >= WIDTH:
			self.snake.x = 0

		if self.snake.x < 0:
			self.snake.x = WIDTH

		if self.snake.y >= HEIGHT:
			self.snake.y = 0

		if self.snake.y < 0:
			self.snake.y = HEIGHT

	def check_collision(self):
		if self.snake.hitbox.colliderect(self.food.hitbox):
			self.food.food_color = 'blue'
			
	def draw(self):
		self.screen.fill(BG_COLOR)
		self.snake.draw()
		self.food.add_food()
		for food in self.food.foods:
			self.food.draw_food()
		self.snake.run()
		self.check_wall_collision()
		self.check_collision()
		pg.display.flip()

	def run(self):
		while True:
			clock.tick(FPS)
			self.check_events()
			self.draw()
