# tictactoe class

from classes.settings import *


class Symbol:
	def __init__(self):
		self. first = FIRST_SYMBOL
		self.second = SECOND_SYMBOL

	def draw(self):
		pass


class Tictactoe:
	def __init__(self, game):
		self.game = game
		self.is_activ = True

	def draw_grid(self):
		for i in range(COLS):
			for j in range(ROWS):
				pg.draw.rect(self.game.screen, 'black', (j * BLOCK_SIZE + 100, i * BLOCK_SIZE + 100, BLOCK_SIZE, BLOCK_SIZE), 1)

	def draw(self):
		self.draw_grid()