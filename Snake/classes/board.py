# snake file
import time
import sys
from classes.settings import *
from classes.snake import Snake

class Board(object):
	def __init__(self):
		self.screen = pg.display.set_mode([WIDTH, HEIGHT])
		self.snake = Snake()

	def check_events(self):
		for event in pg.event.get():
			if event.type == pg.QUIT:
				time.sleep(1)
				pg.quit()
				sys.exit()
			elif event.type == pg.MOUSEBUTTONDOWN:
				print('Myszka wciśnięta....')

	def draw(self):
		# self.screen.blit(SCREEN_BG,(0, 0))  # wallpaper (alternative)
		self.screen.fill(BG_COLOR)  # Background color
		self.snake.draw()
		pg.display.flip()

	def run(self):
		while True:
			clock.tick(FPS)
			self.check_events()
			self.draw()
