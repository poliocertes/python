import pygame
import random

pygame.init()

HEIGHT = 800
WIDTH = 500
colors = ['red', 'blue', 'green', 'orange', 'black']
blocks = []
score = 0
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Tetris')


class GameBoard:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.rows = 8
		self.cols = 5

	def draw_board(self):
		pass


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

	while running:
		screen.fill('blue')
		show_score = pygame.font.Font.render(pygame.font.SysFont('Arial', 30), f'Score: {score}', True, (255, 255, 255))
		pygame.draw.rect(screen, 'white', pygame.Rect(0, 750, 500, 1))
		pygame.draw.line(screen, 'white',(0, 50), (500, 50))
		pygame.draw.line(screen, 'white',(0, 100), (500, 100))
		pygame.draw.line(screen, 'white',(0, 150), (500, 150))
		pygame.draw.line(screen, 'white',(0, 200), (500, 200))
		pygame.draw.line(screen, 'white',(0, 250), (500, 250))
		pygame.draw.line(screen, 'white',(0, 300), (500, 300))
		pygame.draw.line(screen, 'white',(0, 350), (500, 350))
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				break
		keys = pygame.key.get_pressed()

		if keys[pygame.K_UP]:
			print('UP')

		if keys[pygame.K_DOWN]:
			print('DOWN')

		if keys[pygame.K_LEFT]:
			print('LEFT')

		if keys[pygame.K_RIGHT]:
			print('RIGHT')

		screen.blit(show_score, (15, 760))
		pygame.display.update()


if __name__ == '__main__':
	main()
