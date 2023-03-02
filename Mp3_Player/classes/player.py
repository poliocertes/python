# player file

from classes.interface import Interface
from classes.function import Function
from classes.settings import *

class Player(object):
	def __init__(self):
		pg.display.set_caption('PLAYER')
		self.interface = Interface()
		self.function = Function(object)

	def draw(self):
		screen.fill(color=BG_COLOR)
		self.interface.draw()
		pg.display.flip()

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
				sys.exit()


	def play(self):
		while True:
			self.check_events()
			self.draw()
