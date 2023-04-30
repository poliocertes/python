# tictactoe class

from classes.settings import *


class Tictactoe:
	def __init__(self, game):
		self.game = game
		self.field_is_activ = True

	def draw_grid(self):
		for i in range(COLS):
			for j in range(ROWS):
				pg.draw.rect(self.game.screen, 'black', (j * BLOCK_SIZE + (HEIGHT/4), i * BLOCK_SIZE + (WIDTH/4), BLOCK_SIZE, BLOCK_SIZE), 1)

	def mark_field_one(self):
		pg.draw.rect(self.game.screen, 'red', (WIDTH/4, HEIGHT/4, BLOCK_SIZE, BLOCK_SIZE))

	def update(self):
		pass

	def draw(self):
		self.draw_grid()

