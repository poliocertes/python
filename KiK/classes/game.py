# game class
import sys

from classes.settings import *
from classes.tictactoe import Tictactoe


class Game:
	def __init__(self):
		pg.init()
		pg.display.set_caption('K & K')
		self.screen = pg.display.set_mode([WIDTH, HEIGHT])
		self.clock = pg.time.Clock()
		self.tictactoe = Tictactoe(self)

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()
			if event.type == pg.MOUSEBUTTONDOWN:
				current_pos = pg.mouse.get_pos()
				if current_pos[0] <= 180 and current_pos[1] <= 180:
					print('UU')

	def screen_update(self):
		self.clock.tick(FPS)

	def game(self):
		self.screen.fill(color=BOARD_COLOR)
		self.tictactoe.draw()
		pg.display.update()

	def run(self):
		while True:
			self.check_events()
			self.screen_update()
			self.game()