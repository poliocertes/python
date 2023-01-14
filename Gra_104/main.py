import pygame
import random

HEIGHT = 800
WIDTH = 1200
BLUE = (0, 0, 255)
RED = (250, 0, 0)
GREEN = (0, 153, 0)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
ORANGE = (255, 140, 0)
LIGHTBLUE = (0,176,240)
FPS = 480
PADDLE_HEIGHT = 10
PADDLE_WIDTH = 200
BALL_RADIUS = 15

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('Brick breaker')
pygame.display.flip()
keys = pygame.key.get_pressed()
picture = 'background.png'


class Paddle:
	COLOR = RED
	PADDLE_VEL = 6

	def __init__(self, x, y, width, height):
		self.x_cord = x
		self.y_cord = y
		self.width = width
		self.height = height
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw(self):
		pygame.draw.rect(screen, self.COLOR, pygame.Rect(self.x_cord - self.width / 2, self.y_cord, self.width, self.height))

	def move_left(self):
		if self.x_cord > self.width/2 + 10:
			self.x_cord -= self.PADDLE_VEL

	def move_right(self):
		if self.x_cord + self.width < WIDTH + self.width/2 - 10:
			self.x_cord += self.PADDLE_VEL


class Game_ball:
	COLOR = YELLOW
	BALL_VEL = 5

	def __init__(self, x, y, radius):
		self.x_cord = self.start_x = x
		self.y_cord = self.start_y = y
		self.radius = radius
		self.x_vel = self.BALL_VEL
		self.y_vel = 5

	def draw_ball(self):
		pygame.draw.circle(screen, self.COLOR, (self.x_cord, self.y_cord), self.radius)

	def move(self):
		self.x_cord -= self.x_vel
		self.y_cord -= self.y_vel

	def reset(self):
		self.x_cord = self.start_x
		self.y_cord = self.start_y


class Brick:

	def __init__(self):
		self.width = 150 
		self.height = 20
		self.x_cord = 20
		self.y_cord = 20
		self.colors = [GRAY, GREEN, ORANGE, RED, LIGHTBLUE]
		self.color = random.choice(self.colors)
		self.bricks = []

	def draw_brick(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord , self.y_cord, self.width, self.height))





def main():
	running = True
	clock = pygame.time.Clock()

	lives = 3
	game_score = 0

	paddle = Paddle(WIDTH/2, HEIGHT-30, PADDLE_WIDTH, PADDLE_HEIGHT)
	game_ball = Game_ball(WIDTH/2, HEIGHT - 45, BALL_RADIUS)
	brick = Brick()

	while running:
		background = pygame.image.load(picture)
		screen.blit(background, (0, 0))
		clock.tick(FPS)
		paddle.draw()
		game_ball.draw_ball()
		brick.draw_brick()
		game_ball.move()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				break

		if game_ball.y_cord > HEIGHT -5:
			lives -= 1
			print(lives)
			game_ball.y_vel *= -1
		if game_ball.y_cord < 10:
			game_ball.y_vel *= -1
		if game_ball.x_cord > WIDTH - 10:
			game_ball.x_vel *= -1
		if game_ball.x_cord < 10:
			game_ball.x_vel *= -1

		if game_ball.y_cord + game_ball.radius >= paddle.y_cord and (paddle.x_cord < game_ball.x_cord < (game_ball.x_cord + paddle.x_cord+PADDLE_WIDTH)):
			game_ball.y_vel *= -1

		if lives == 0:
			quit()

		keys = pygame.key.get_pressed()

		if keys[pygame.K_RIGHT]:
			paddle.move_right()
		if keys[ pygame.K_LEFT]:
			paddle.move_left()

		pygame.display.update()


if __name__ == "__main__":
	main()
