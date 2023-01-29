from settings import *
from classes.gameboard import GameBoard
import pygame as pg


# pygame init
pg.init()

# global variables

colors = ['red', 'blue', 'green', 'orange', 'black']
blocks = []
score = 0
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
pg.display.set_caption('Tetris')


class Block(GameBoard):
	def __init__(self, x, y, width, height):
		super().__init__(x, y, width, height)
		pass

	def rotate(self):
		pass

	def move(self):
		pass


def main():
	running = True
	game_board = GameBoard()

	while running:
		screen.fill('blue')
		game_board.draw_grid()
		show_title = pg.font.Font.render(pg.font.SysFont('Arial', 30), 'TETRIS', True, (255, 255, 255))
		show_score = pg.font.Font.render(pg.font.SysFont('Arial', 30), f'Score: {score}', True, (255, 255, 255))
		show_next = pg.font.Font.render(pg.font.SysFont('Arial', 30), 'Next', True, (255, 255, 255))

		for event in pg.event.get():
			if event.type == pg.QUIT:
				running = False
				break
		keys = pg.key.get_pressed()

		if keys[pg.K_UP]:
			print('UP')

		if keys[pg.K_DOWN]:
			print('DOWN')

		if keys[pg.K_LEFT]:
			print('LEFT')

		if keys[pg.K_RIGHT]:
			print('RIGHT')

		screen.blit(show_title, (365, 25))
		# screen.blit(show_score, (15, 25))
		# screen.blit(show_next, (675, 25))
		pg.display.update()


if __name__ == '__main__':
	main()
