import pygame
import random

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
        self.width = 7
        self.height = 7
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
        self.x_cord = 5
        self.y_cord = 5
        self.width = 100
        self.height = 20
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.rows = 8
        self.cols = 6
        self.bricks = []

    def create_wall(self):
        for y in range(self.rows):
            for x in range(self.cols):
                single_brick = pygame.Rect(x, y, self.width, self.height)
                self.bricks.append(single_brick)

    def draw(self):
        for single_brick in self.bricks:
            pygame.draw.rect(screen, self.color, single_brick)


# main function
def main():
    running = True
    clock = pygame.time.Clock()
    paddle = Paddle(WIDTH//2 - 50, (HEIGHT - 10), PADDLE_WIDTH, PADDLE_HEIGHT)
    gameball = GameBall(WIDTH // 2, HEIGHT - 55)
    lives = 5
    brick = Brick()
    brick.create_wall()
    while running:  # main loop
        # screen.blit(bg, (0, 0))
        screen.fill(BLUE)
        clock.tick(FPS)
        paddle.draw()
        gameball.draw()
        gameball.move()
        brick.draw()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            paddle.move_left()
        if keys[pygame.K_RIGHT]:
            paddle.move_right()

        if gameball.y_cord >= HEIGHT:
            gameball.y_vel *= -1
        if gameball.y_cord <= 2:
            gameball.y_vel *= -1

        if gameball.x_cord >= WIDTH:
            gameball.x_vel *= -1

        if gameball.x_cord <= 1:
            gameball.x_vel *= -1

        if paddle.x_cord + paddle.width >= gameball.x_cord > paddle.x_cord and paddle.y_cord < gameball.y_cord <= paddle.y_cord + paddle.height:
            gameball.y_vel *= -1

        pygame.display.update()


if __name__ == "__main__":
    main()
