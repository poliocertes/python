import pygame


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


class Paddle:

    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.color = (0, 153, 0)
        self.vel = 5
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x_cord, self.y_cord, self.width, self.height))

    def move_left(self):
        if self.x_cord > 10:
            self.x_cord -= self.vel

    def move_right(self):
        if self.x_cord + self.width < WIDTH - 10:
            self.x_cord += self.vel


class GameBall:
    COLOR = (255, 140, 0)

    def __init__(self, x, y, radius):
        self.x_cord = self.start_x = x
        self.y_cord = self.start_y = y
        self.radius = radius
        self.x_vel = 4
        self.y_vel = 5

    def draw(self):
        pygame.draw.circle(screen, self.COLOR, (self.x_cord, self.y_cord), self.radius)

    def move(self):
        self.x_cord += self.x_vel
        self.y_cord += self.y_vel

    def reset(self):
        self.x_cord = self.start_x
        self.y_cord = self.start_y


class Brick:
    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.color = 'red'
        self.rows = 8
        self.cols = 6
        self.bricks = []

    def create_brick_wall(self):
        for y in range(self.rows):
            for x in range(self.cols):
                single_brick = pygame.Rect(x, y, self.width, self.height)
                self.bricks.append(single_brick)

    def draw(self):
        for single_brick in self.bricks:
            pygame.draw.rect(screen, self.color, single_brick)


def main():
    running = True
    clock = pygame.time.Clock()
    paddle = Paddle(WIDTH//2 - 50, (HEIGHT - 20), PADDLE_WIDTH, PADDLE_HEIGHT)
    gameball = GameBall(WIDTH // 2, HEIGHT - 35 , BALL_RADIUS)
    lives = 5
    brick = Brick(5, 5, 100, 25)
    brick.create_brick_wall()

    while running:
        screen.blit(bg, (0, 0))
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

        if gameball.y_cord + gameball.radius >= HEIGHT - 5:
            gameball.y_vel *= -1
            lives -= 1
            print(lives)
        if gameball.y_cord - gameball.radius <= 2:
            gameball.y_vel *= -1

        if gameball.x_cord + gameball.radius * 2 >= WIDTH:
            gameball.x_vel *= -1

        if gameball.x_cord <= 1:
            gameball.x_vel *= -1

        if paddle.x_cord + paddle.width >= gameball.x_cord > paddle.x_cord and paddle.y_cord < gameball.y_cord <= paddle.y_cord + paddle.height:
            gameball.y_vel *= -1

        if gameball.y_cord <= brick.y_cord + brick.height and brick.x_cord + brick.width > gameball.x_cord > brick.x_cord :
            print('gol')

        pygame.display.update()


if __name__ == "__main__":
    main()
