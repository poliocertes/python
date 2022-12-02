import pygame
import sys


height = 800
width = 800
pygame.init()
pygame.display.init()
window = pygame.display.set_mode([width, height])

pygame.display.update()


def main():
	running = True
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit().pygame.quit()


if __name__ == "__main__":
	main()
