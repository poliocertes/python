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
				if current_pos < ((WIDTH/4), (HEIGHT/4)):
					print('oko')

	def screen_update(self):
		self.clock.tick(FPS)

	def game(self):
		self.screen.fill(color='brown')
		self.tictactoe.draw()
		pg.display.update()

	def run(self):
		while True:
			self.check_events()
			self.screen_update()
			self.game()