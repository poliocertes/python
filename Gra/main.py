from tkinter import Label

import pygame
import random

# game init
pygame.init()

# define screen settings
HEIGHT = 800
WIDTH = 1200
FPS = 240

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

Label(screen, "Hello World", 100, 100, 36)


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
		pygame.draw.rect(screen, self.COLOR, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

	def move_left(self):  # move a paddle left
		if self.x_cord > 5:
			self.x_cord -= self.PADDLE_VEL

	def move_right(self):  # move a paddle right
		if self.x_cord + self.width < WIDTH  - 5:
			self.x_cord += self.PADDLE_VEL


# class game ball
class GameBall:
	BALL_VEL = 5

	def __init__(self, x_cord, y_cord):
		self.x_cord = self.start_x = x_cord
		self.y_cord = self.start_y = y_cord
		self.width = 10
		self.height = 10
		self.x_vel = self.BALL_VEL
		self.y_vel = 8
		self.color = YELLOW
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
		self.lives = 5
		self.score = 0

	def draw_ball(self, paddle):
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
		if self.hitbox.colliderect(paddle.hitbox):
			self.y_vel *= -1

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
		self.x_cord = 5
		self.y_cord = 5
		self.width = 120
		self.height = 20
		self.cols = 10 
		self.rows = 6
		self.colors = ["sky blue", "tomato", "lime green","yellow"]
		#self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
		self.bricks = []

	def create_bricks_wall(self):
		for row in range(self.rows):
			for col in range(self.cols):
				self.color = random.choice(self.colors)
				single_block = pygame.Rect(col * self.width, row * self.height, self.width, self.height)
				self.bricks.append(single_block)

	def draw(self, gameball):
		for brick in self.bricks:
			pygame.draw.rect(screen, self.color, brick)
			pygame.draw.rect(screen, 'black', brick, 2)


def main():
	running = True
	clock = pygame.time.Clock()
	paddle = Paddle(WIDTH / 2, HEIGHT - 30, PADDLE_WIDTH, PADDLE_HEIGHT)
	gameball = GameBall(WIDTH / 2, HEIGHT - 45)
	brick = Brick()
	brick.create_bricks_wall()
	clock.tick(FPS)

	while running:
		screen.blit(pygame.image.load(picture).convert(),(0, 0))
		paddle.draw()
		gameball.draw_ball(paddle)
		gameball.move()
		brick.draw(gameball)
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


if __name__ == "__main__" :
	main()
