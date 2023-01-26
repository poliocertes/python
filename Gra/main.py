from tkinter import Label

import pygame
import random
from random import randrange

pygame.init()

# constants
HEIGHT = 800
WIDTH = 800
BLUE = (0, 0, 255)

FPS = 120
PADDLE_HEIGHT = 10
PADDLE_WIDTH = 120
BALL_RADIUS = 5

screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('BRICKS BREAKER')
bg = pygame.image.load('assets/sky.png')


# paddle class
class Paddle(object):

    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.color = (0, 153, 0)
        self.vel = 5
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

    def move_left(self):
        if self.x_cord > 10:
            self.x_cord -= self.vel

    def move_right(self):
        if self.x_cord + self.width < WIDTH - 10:
            self.x_cord += self.vel


# gameball class
class GameBall(object):

    def __init__(self, x, y):
        self.x_cord = x
        self.y_cord = y
        self.width = 15
        self.height = 15
        self.color = (255, 140, 0)
        self.x_vel = 2
        self.y_vel = 3
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

    def move(self):
        self.x_cord += self.x_vel
        self.y_cord += self.y_vel


# brick class
class Brick(object):

    def __init__(self):
        self.x_cord = 15
        self.y_cord = 15
        self.width = 120
        self.height = 50
        self.rows = 4
        self.cols = 6
        self.bricks = []
        self.color_list = [(randrange(100, 255), randrange(100, 255), randrange(100, 255)) for i in range(self.cols) for j in
                      range(self.rows)]

    def draw(self):
        block_list = [pygame.Rect(self.x_cord + (self.width + 10) * i, self.y_cord + (self.height + 10) * j, self.width, self.height) for i in range(self.cols) for j in range(self.rows)]
        [pygame.draw.rect(screen, self.color_list[color], block) for color, block in enumerate(block_list)]


# main function
def main():
    running = True
    lives = 5
    score = 12
    clock = pygame.time.Clock()
    paddle = Paddle(WIDTH//2 - 50, (HEIGHT - 100), PADDLE_WIDTH, PADDLE_HEIGHT)
    gameball = GameBall(WIDTH // 2, HEIGHT - 125)
    brick = Brick()
    while running:  # main loop

        screen.fill(BLUE)
        clock.tick(FPS)
        paddle.draw()
        gameball.draw()
        gameball.move()
        brick.draw()
        pygame.draw.rect(screen, 'white', pygame.Rect(0, 740, 800, 5))
        show_score = pygame.font.Font.render(pygame.font.SysFont('Arial Bold', 40), f'Score: {score}', True, (255, 255, 255))
        show_lives = pygame.font.Font.render(pygame.font.SysFont('Arial Bold', 40), f'Lives: {lives}', True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        if gameball.y_cord >= HEIGHT - 65:
            gameball.y_vel *= -1
            lives -= 1
        if gameball.y_cord <= 2:
            gameball.y_vel *= -1

        if gameball.x_cord >= WIDTH:
            gameball.x_vel *= -1

        if gameball.x_cord <= 1:
            gameball.x_vel *= -1

        for j in range(brick.cols):
            for i in range(brick.rows):
                if gameball.y_cord < brick.x_cord + brick.height:
                    print('ttt')
        if lives < 1:
            print('game over')
        if paddle.x_cord + paddle.width >= gameball.x_cord > paddle.x_cord and paddle.y_cord < gameball.y_cord +gameball.height:
            gameball.y_vel *= -1
        screen.blit(show_score, (15, 760))
        screen.blit(show_lives, (650, 760))
        pygame.display.update()


if __name__ == "__main__":
    main()
