import pygame.image

from settings import *
from classes.gameboard import GameBoard
from classes.block import Block
import pygame as pg


# pygame init
pg.init()

# global variables

colors = ['red', 'blue', 'green', 'orange', 'black']
blocks = []
score = 0
screen = pg.display.set_mode([WINDOW_WIDTH, WINDOW_HEIGHT])
tetris_logo = pygame.image.load('assets/tetris.png').convert()
pg.display.set_caption('Tetris')


def main():
	running = True
	game_board = GameBoard()
	block = Block()

	while running:
		screen.fill(BLUE)
		game_board.draw_grid()

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

		screen.blit(tetris_logo, (600, 50))
		screen.blit(show_next, (665, 350))
		screen.blit(show_score, (650, 700))

		pg.display.update()


if __name__ == '__main__':
	main()
