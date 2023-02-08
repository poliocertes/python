# brickbreaker by @Jacek

import pygame as pg
from random import randrange

pg.init()

# constants
HEIGHT = 800
WIDTH = 800
BLUE = (0, 0, 255)
FPS = 120
PADDLE_HEIGHT = 10
PADDLE_WIDTH = 150
BALL_RADIUS = 5

screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('BRICKS BREAKER')
bg = pg.image.load('assets/sky.png').convert()


# paddle class
class Paddle(object):

    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.color = (0, 153, 0)
        self.vel = 5
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)
        pg.draw.rect(screen, self.color, pg.Rect(self.x_cord, self.y_cord, self.width, self.height), border_radius=8)

    def move_left(self):
        if self.x_cord > 5:
            self.x_cord -= self.vel

    def move_right(self):
        if self.x_cord + self.width < WIDTH - 5:
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
        self.y_vel = 4
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        self.hitbox = pg.Rect(self.x_cord, self.y_cord, self.width, self.height)
        pg.draw.rect(screen, self.color, pg.Rect(self.x_cord, self.y_cord, self.width, self.height), border_radius=8)

    def move(self):
        self.x_cord += self.x_vel
        self.y_cord += self.y_vel


# brick class
class Brick(object):

    def __init__(self):
        self.x_cord = 12
        self.y_cord = 12
        self.width = 120
        self.height = 50
        self.rows = 4
        self.cols = 6
        self.score = 0
        self.color_list = [(randrange(100, 255), randrange(100, 255), randrange(100, 255)) for i in range(self.cols) for j in
                      range(self.rows)]
        self.block_list = [pg.Rect(self.x_cord + (self.width + 11) * i, self.y_cord + (self.height + 11) * j, self.width, self.height) for i in range(self.cols) for j in range(self.rows)]

    def draw(self, gameball):
        for color, block in enumerate(self.block_list):
            pg.draw.rect(screen, self.color_list[color], block, border_radius=7)
        for i in range(self.cols):
            for j in range(self.rows):
                for item in self.block_list:
                    if item.y + item.height >= gameball.y_cord and item.x + item.width > gameball.x_cord  > item.x:
                        self.score += 1
                        gameball.y_vel *= -1
                        if self.score % 5 == 0:
                            gameball.x_vel += 1
                            gameball.y_vel += 1
                        self.block_list.remove(item)


# main function
def main():
    running = True
    lives = 5
    clock = pg.time.Clock()
    paddle = Paddle(WIDTH//2 - 50, (HEIGHT - 100), PADDLE_WIDTH, PADDLE_HEIGHT)
    gameball = GameBall(WIDTH // 2, HEIGHT - 125)
    game_over_image = pg.font.Font.render(pg.font.SysFont("", 50), "Game over. Press 'q' to exit.", True, (255, 255, 255))
    win_image = pg.font.Font.render(pg.font.SysFont("", 50), "You win. Press 'r' to reset or 'q' to exit. ", True, (255, 255, 255))
    brick = Brick()
    while running:  # main loop
        screen.blit(bg, (0, 0))
        clock.tick(FPS)
        paddle.draw()
        gameball.draw()
        gameball.move()
        brick.draw(gameball)
        pg.draw.rect(screen, 'white', pg.Rect(0, 740, 800, 5))
        show_score = pg.font.Font.render(pg.font.SysFont('Arial Bold', 40), f'Score: {brick.score}', True, (255, 255, 255))
        show_lives = pg.font.Font.render(pg.font.SysFont('Arial Bold', 40), f'Lives: {lives}', True, (255, 255, 255))

        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
                break

        keys = pg.key.get_pressed()

        if keys[pg.K_LEFT]:
            paddle.move_left()
        if keys[pg.K_RIGHT]:
            paddle.move_right()

        if gameball.y_cord >= HEIGHT - 65:
            gameball.y_vel *= -1
            lives -= 1
        if gameball.y_cord <= 2:
            gameball.y_vel *= -1

        if gameball.x_cord + gameball.width >= WIDTH:
            gameball.x_vel *= -1

        if gameball.x_cord <= 1:
            gameball.x_vel *= -1

        if lives < 1:
            screen.blit(game_over_image, (120, 300))
            gameball.x_cord = WIDTH / 2
            gameball.y_cord = HEIGHT - 130
            pg.display.update()
            if keys[pg.K_q]:
                pg.quit()
            continue

        if brick.score == 24:
            screen.blit(win_image, (105, 300))
            gameball.x_cord = WIDTH / 2
            gameball.y_cord = HEIGHT - 130
            pg.display.update()
            if keys[pg.K_r]:
                main()
            if keys[pg.K_q]:
                pg.quit()
            continue

        if paddle.x_cord + paddle.width >= gameball.x_cord > paddle.x_cord and paddle.y_cord < gameball.y_cord + gameball.height:
            gameball.y_vel *= -1

        screen.blit(show_score, (15, 760))
        screen.blit(show_lives, (650, 760))
        pg.display.update()


if __name__ == "__main__":
    main()
