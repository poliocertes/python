import pygame
import random
import time

# game init
pygame.init ( )

# define screen settings
HEIGHT = 800
WIDTH = 1200
FPS = 480

# define colours
BLUE = (0, 0, 255)
RED = (250, 0, 0)
GREEN = (0, 153, 0)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
LIGHTBLUE = (0, 176, 240)

# paddle and ball size
PADDLE_HEIGHT = 10
PADDLE_WIDTH = 200


# pygame settings
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Brick breaker')
pygame.display.flip()
picture = 'assets/stars.png'


# class Paddle
class Paddle:
	COLOR = RED
	PADDLE_VEL = 11

	def __init__(self, x, y, width, height):
		self.x_cord = x
		self.y_cord = y
		self.width = width
		self.height = height
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw(self):  # paddle draw function
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
		pygame.draw.rect(screen, self.COLOR, pygame.Rect(self.x_cord - self.width / 2, self.y_cord, self.width, self.height))

	def move_left(self):  # move a paddle left
		if self.x_cord > self.width / 2 + 10:
			self.x_cord -= self.PADDLE_VEL

	def move_right(self):  # move a paddle right
		if self.x_cord + self.width < WIDTH + self.width / 2 - 10:
			self.x_cord += self.PADDLE_VEL


# class game ball
class Game_ball:
	BALL_VEL = 5

	def __init__(self, x_cord, y_cord):
		self.x_cord = self.start_x = x_cord
		self.y_cord = self.start_y = y_cord
		self.width = 10
		self.height = 10
		self.x_vel = self.BALL_VEL
		self.y_vel = 9
		self.color = YELLOW
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw_ball(self):
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

	def move(self):
		if self.y_cord >= HEIGHT:
			self.y_vel *= -1
		if self.y_cord < 10:
			self.y_vel *= -1
		if self.x_cord > WIDTH - 10:
			self.x_vel *= -1
		if self.x_cord < 10:
			self.x_vel *= -1
		self.x_cord -= self.x_vel
		self.y_cord -= self.y_vel

	def reset(self):
		self.x_cord = self.start_x
		self.y_cord = self.start_y


class Brick:
	def __init__(self):
		pass


def main():
	running = True
	clock = pygame.time.Clock()
	paddle = Paddle(WIDTH / 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
	game_ball = Game_ball(WIDTH / 2, HEIGHT - 45)

	clock.tick(FPS)
	brick_breaker = Brick()

	while running:
		screen.blit(pygame.image.load (picture).convert(), (0, 0))
		paddle.draw()
		game_ball.draw_ball()
		game_ball.move()
		keys = pygame.key.get_pressed()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				break

		if keys[pygame.K_RIGHT]:
			paddle.move_right()
		if keys[pygame.K_LEFT]:
			paddle.move_left()

		pygame.display.update()

		if game_ball.hitbox.colliderect(paddle.hitbox):
			print('OOO')

if __name__ == "__main__":
	main()
