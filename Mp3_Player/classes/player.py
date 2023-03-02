# player file

from classes.settings import *

class Player(object):
	def __init__(self):
		pg.display.set_caption('PLAYER')

	def draw(self):
		screen.fill(color=BG_COLOR)
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
