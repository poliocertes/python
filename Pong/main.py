# Pong by Jacek
import pygame

pygame.init()

HEIGHT = 800
WIDTH = 1200
BLUE = (0, 0, 255)
RED = (250, 0, 0)
GRAY = (150, 150, 150)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
GREEN = (0, 153, 0)
ORAGNE = (255, 140, 0)
FPS = 120
PADDLE_HEIGHT = 150
PADDLE_WIDTH = 20
BALL_RADIUS = 5

score1 = 0
score2 = 0

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('PONG')
pygame.display.flip()


class Paddle_one:
	COLOR = GREEN
	PADDLE1_VEL = 6
	def __init__(self, x, y, width, height):
		self.x_cord = x
		self.y_cord = y
		self.width = width
		self.height = height
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw(self):
		pygame.draw.rect(screen, self.COLOR, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height), border_radius=8)

	def move_up(self):
		if self.y_cord > 10:
			self.y_cord -= self.PADDLE1_VEL

	def move_down(self):
		if self.y_cord + self.height < HEIGHT - 10:
			self.y_cord += self.PADDLE1_VEL


class Paddle_two:
	COLOR = RED
	PADDLE2_VEL = 6
	def __init__(self, x, y, width, height):
		self.x_cord = x
		self.y_cord = y
		self.width = width
		self.height = height
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw(self):
		pygame.draw.rect(screen, self.COLOR, pygame.Rect(self.x_cord - self.width/2, self.y_cord, self.width, self.height), border_radius=8)

	def move_up(self):
		if self.y_cord > 10:
			self.y_cord -= self.PADDLE2_VEL

	def move_down(self):
		if self.y_cord + self.height < HEIGHT - 10:
			self.y_cord += self.PADDLE2_VEL


class Game_ball:
	COLOR = YELLOW
	BALL_VEL = 5
	def __init__(self, x, y, radius):
		self.x_cord = self.start_x = x
		self.y_cord = self.start_y = y
		self.radius = radius
		self.x_vel = self.BALL_VEL
		self.y_vel = 1

	def draw(self, screen):
		pygame.draw.circle(screen, self.COLOR, (self.x_cord, self.y_cord), self.radius)

	def move(self):
		self.x_cord += self.x_vel
		self.y_cord += self.y_vel

	def reset(self):
		self.x_cord = self.start_x
		self.y_cord = self.start_y


def main():
	running = True
	clock = pygame.time.Clock()

	score1 = 0
	score2 = 0

	paddle_1 = Paddle_one(75, (HEIGHT // 2 - PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
	paddle_2 = Paddle_two(WIDTH - 75 - PADDLE_WIDTH, (HEIGHT // 2 - PADDLE_HEIGHT // 2), PADDLE_WIDTH, PADDLE_HEIGHT)
	game_ball = Game_ball(WIDTH // 2, HEIGHT // 2, BALL_RADIUS)
	
	if score1 or score2 >= 5:
		game_ball.BALL_VEL += 1
	while running:
		screen.fill(BLUE)
		clock.tick(FPS)
		paddle_1.draw()
		paddle_2.draw()
		game_ball.draw(screen)
		game_ball.move()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				break

		keys = pygame.key.get_pressed()

		if keys[pygame.K_w]:
			paddle_1.move_up()
		if keys[pygame.K_s]:
			paddle_1.move_down()
		if keys[pygame.K_DOWN]:
			paddle_2.move_down()
		if keys[pygame.K_UP]:
			paddle_2.move_up()

		if game_ball.y_cord + game_ball.radius >= HEIGHT - 3:
			game_ball.y_vel *= -1
		if game_ball.y_cord - game_ball.radius <= 2:
			game_ball.y_vel *= -1

		if game_ball.x_cord + game_ball.radius * 2 >= WIDTH:
			game_ball.x_vel *= -1
			if game_ball.y_cord < paddle_2.y_cord or game_ball.y_cord > paddle_2.y_cord + paddle_2.height:   
				score1 += 1

		if game_ball.x_cord <= 1:
			game_ball.x_vel *= -1
			if game_ball.y_cord < paddle_1.y_cord or game_ball.y_cord > paddle_1.y_cord + paddle_1.height: 
				score2 += 1

		if game_ball.x_cord  <= paddle_1.x_cord + paddle_1.width and game_ball.x_cord > paddle_1.x_cord and paddle_1.y_cord < game_ball.y_cord <= paddle_1.y_cord + paddle_1.height:
			game_ball.x_vel *= -1

		if game_ball.x_cord + game_ball.radius * 2 >= paddle_2.x_cord and game_ball.x_cord < paddle_2.x_cord + paddle_2.width and paddle_2.y_cord < game_ball.y_cord <= paddle_2.y_cord + paddle_2.height:
			game_ball.x_vel *= -1

		score_image_1 = pygame.font.Font.render(pygame.font.SysFont("Arial", 24), f"Score 1:  {score1}", True, (WHITE))
		score_image_2 = pygame.font.Font.render(pygame.font.SysFont("Arial", 24), f"Score 2:  {score2}", True, (WHITE))
		screen.blit(score_image_1, (20, 5))
		screen.blit(score_image_2, (1040, 5))
		pygame.display.update()


if __name__ == "__main__":
	main()
	