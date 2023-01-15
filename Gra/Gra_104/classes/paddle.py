import pygame


PADDLE_VEL = 6


class Paddle:
	def __int__(self,x ,y , width, height):
		self.x_cord = x
		self.y_cord = y
		self.width = width
		self.height = height
		self.color = (0, 153, 0)
		self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

	def draw(self):
		pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

	def move_up(self):
		if self.y_cord > 10:
			self.y_cord -= self.PADDLE_VEL

	def move_down(self):
		if self.y_cord + self.height < HEIGHT - 10:
			self.y_cord += self.PADDLE_VEL