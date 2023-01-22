import pygame

pygame.init()
game_window = pygame.display.set_mode([800, 800])
bg = pygame.image.load('assets/sky.png')
game_window.blit(bg, (0, 0))


class Paddle(object):
    PADDLE_VEL = 6

    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = 'blue'

    def draw_paddle(self):
        pygame.draw.rect(game_window, self.color, pygame.Rect(self.x, self.y, self.width, self.height))

    def move_left(self):
        if self.x > 5:
            self.x += self.PADDLE_VEL

    def move_right(self):
        if self.x < 750:
            self.x -= self.PADDLE_VEL


def main():

    running = True
    while running:
        paddle = Paddle(330, 775, 120, 20)
        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        if keys[pygame.K_LEFT]:
            print('l')
            paddle.move_left()

        if keys[pygame.K_RIGHT]:
            print('r')
            paddle.move_right()

        paddle.draw_paddle()

        pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()