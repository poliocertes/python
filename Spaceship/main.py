# SpaceShooter by Jacek

# import
import random
from tkinter import messagebox
import pygame
import time
import sys
import os

# initialization
HEIGHT = 800
WIDTH = 1200
pygame.init()
pygame.display.init()
screen = pygame.display.set_mode([WIDTH, HEIGHT])
pygame.display.set_caption('SpaceShip')
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 18)
update_time = time.time()

# constants
FPS = 480
SPACE_SHIP = pygame.image.load('spaceship.png')
SPACE_SHIP = pygame.transform.scale(SPACE_SHIP, [100, 100])
ENEMY = pygame.image.load('enemy.png')
ENEMY = pygame.transform.scale(ENEMY, [80, 80])
BG_IMG = pygame.image.load('Night_sky.jpg')
BG_IMG = pygame.transform.scale(BG_IMG, [1200, 800])
BOMB = pygame.image.load('fireball.png')
BOMB = pygame.transform.scale(BOMB, [10, 10])

# speed settings
ship_speed = 3


# crete background class
class Background: 

    def __init__(self):
        self.x = 0
        self.y = 0
        self.image = BG_IMG
        self.width = self.image.get_width()
        self.height = self.image.get_height()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

 
# create ship class
class Ship:

    def __init__(self):
        self.x = 550
        self.y = 675
        self.image = SPACE_SHIP
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = ship_speed
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def move(self, keys, background):
        if keys[pygame.K_LEFT]:
            if self.x > 0:
                self.x -= self.speed
        if keys[pygame.K_RIGHT]:
            if self.x < background.width - self.width:
                self.x += self.speed
  
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self):
        screen.blit(SPACE_SHIP, (self.x, self.y))


# create enemy class
class Enemy:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = ENEMY
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)  

    def draw(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
        screen.blit(ENEMY, (self.x, self.y))


# create fireball
class Fireball:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image = BOMB
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)
 
    def draw(self):
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.height)            
        screen.blit(BOMB, (self.x, self.y))

        
# main function
def main():
    background = Background()
    ship = Ship()
    running = True
    bombs = []
    enemies = []
    score = 0
    clock = 0
    lives = 5
    level = 1
    enemy_speed = 0.5
    bomb_speed = 2
    draw_time_difference = 1.0
    best = open('score.txt')
    best_score = best.read()

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                file = open('score.txt', 'w')
                if os.stat('score.txt').st_size == 0 or score > int(best_score):
                    file.write(str(score))
                else:
                    pass 
                sys.exit().pygame.quit()
        clock += pygame.time.Clock().tick(FPS) / 1000
        fireball = Fireball(ship.x + 45, ship.y)
        score_label = my_font.render("Score: " + str(score), True, (255, 255, 0))
        lives_label = my_font.render("Lives: " + str(lives), True, (255, 255, 0))
        level_label = my_font.render("Level: " + str(level), True, (255, 255, 0))
        best_score_label = my_font.render("Best: " + str(best_score), True, (255, 255, 0))
        x_enemy = random.randint(10, 1130)
        y_enemy = random.uniform(-10, -5)
        enemy = Enemy(x_enemy, y_enemy)
        enemy.draw()
        keys = pygame.key.get_pressed()
        ship.move(keys, background)
        background.draw()
        ship.draw()
        screen.blit(score_label, (10, 10))
        screen.blit(lives_label, (1110, 10))
        screen.blit(level_label, (380, 10))
        screen.blit(best_score_label, (730, 10))

        if clock < draw_time_difference:
            pass
        else:
            clock = 0
            enemies.append(enemy)

        if keys[pygame.K_SPACE]: 
            bombs.append(fireball)
            # print(len(bombs))

        for bomb in bombs:
            bomb.draw()
            bomb.y -= bomb_speed

            for enemy in enemies:
                if enemy.hitbox.colliderect(bomb.hitbox):
                    del bombs[0:20]

            for enemy in enemies:
                if enemy.hitbox.colliderect(bomb.hitbox):
                    enemies.remove(enemy)
                    score += 1
                    if score > 0 and score % 5 == 0:
                        level += 1
                        enemy_speed += 0.2
                        bomb_speed += 0.3
                        if draw_time_difference > 0.3:
                            draw_time_difference -= 0.1
                        else:
                            draw_time_difference = draw_time_difference
                        break

            if bomb.y <= bomb.height:
                bombs.remove(bomb)

        for enemy in enemies: 
            enemy.draw()
            enemy.y += enemy_speed
            if enemy.y > background.height - 10:
                enemies.remove(enemy)
                lives -= 1 
                if lives == 0:
                    file = open('score.txt', 'w')
                    if os.stat('score.txt').st_size == 0 or score > int(best_score):
                        file.write(str(score))
                    elif score <= int(best_score):
                        pass
                    file.close()
                    messagebox.showinfo(title="Game Over", message='Game over!')
                    sys.exit()

            if enemy.hitbox.colliderect(ship.hitbox):
                score -= 1
                enemies.remove(enemy)
        pygame.display.update()


# main function
if __name__ == "__main__":
    main()
