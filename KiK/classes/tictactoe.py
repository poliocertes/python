# tictactoe class

from classes.settings import *


class Symbol:
	def __init__(self):
		self.image = pg.Surface([BLOCK_SIZE, BLOCK_SIZE])
		self.symbols = []

	def draw(self):
		pass


class Tictactoe:
	def __init__(self, game):
		self.game = game
		self.field_is_activ = True

	def draw_grid(self):
		for i in range(COLS):
			for j in range(ROWS):
				pg.draw.rect(self.game.screen, 'black', (j * BLOCK_SIZE + (HEIGHT/4), i * BLOCK_SIZE + (WIDTH/4), BLOCK_SIZE, BLOCK_SIZE), 1)

	def update(self):
		pass

	def draw(self):
		self.draw_grid()