import pygame
from random import randint
from sounds import *

resolution = (1280, 700)


class Physic:
    def __init__(self, x, y, width, height, acc, max_vel):
        self.gravity = 0.7
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.hor_velocity = 0
        self.ver_velocity = 0
        self.acc = acc
        self.max_vel = max_vel
        self.previous_x = x
        self.previous_y = y
        self.jump = False
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def physic_tick(self, floors):
        self.ver_velocity += 1.0
        self.x_cord += self.hor_velocity
        self.y_cord += self.ver_velocity

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        for floor in floors:
            if not floor.hitbox.colliderect(self.hitbox):
                continue
            if self.x_cord + self.width >= floor.x_cord + 1 > self.previous_x + self.width:
                self.x_cord = self.previous_x
                self.hor_velocity = 0
            if self.x_cord <= floor.x_cord + floor.width - 1 < self.previous_x:
                self.x_cord = self.previous_x
                self.hor_velocity = 0
            if self.y_cord + self.height >= floor.y_cord + 1 > self.previous_y + self.height:
                self.y_cord = self.previous_y
                self.jump = False
                self.ver_velocity = 0
            if self.jump is True:
                if self.y_cord <= floor.y_cord + floor.width - 1:
                    self.ver_velocity = 0

        self.previous_x = self.x_cord
        self.previous_y = self.y_cord


class Object:
    def __init__(self):
        self.x_cord = randint(0, 5000)
        self.y_cord = randint(520, 620)
        self.image = pygame.image.load("mushroom.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window, background_x):
        window.blit(self.image, (self.x_cord + background_x, self.y_cord))


class Heart:
    def __init__(self):
        self.x_cord = randint(0, 5000)
        self.y_cord = randint(470, 650)
        self.image = pygame.image.load("heart.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window, background_x):
        window.blit(self.image, (self.x_cord + background_x, self.y_cord))


class Floor:
    def __init__(self, x, y, width, height):
        self.x_cord = x
        self.y_cord = y
        self.width = width
        self.height = height
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self, window, background_x):
        pygame.draw.rect(window, (255, 255, 255), (self.x_cord + background_x, self.y_cord, self.width, self.height))


class Health:
    def __init__(self, max_health=100):
        self.health = max_health
        self.max_health = max_health
        self.alive = True

    def damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.health = 0
            self.alive = False

    def draw_health_bar(self, window, x, y, max_width, height):
        percent_width = self.health / self.max_health
        width = round(max_width * percent_width)
        if self.health > 50:
            color = (30, 255, 30)
        elif 50 >= self.health > 35:
            color = (255, 165, 0)
        else:
            color = (255, 30, 30)
        pygame.draw.rect(window, (30, 30, 30), (x, y, max_width, height))
        pygame.draw.rect(window, color, (x, y, width, height))


class Background:
    def __init__(self):
        self.x_cord = 0
        self.y_cord = 0
        self.image = pygame.image.load("background.png").convert()
        self.width = self.image.get_width()

    def tick(self, hero):
        if self.width - resolution[0] / 2 > hero.x_cord >= resolution[0] / 2:
            self.x_cord = -hero.x_cord + resolution[0] / 2
        elif hero.x_cord >= self.width - resolution[0] / 2:
            self.x_cord = - self.width + resolution[0]
        else:
            self.x_cord = 0

    def draw(self, window):
        window.blit(self.image, (self.x_cord, self.y_cord))


class Hero(Physic, Health):
    def __init__(self):
        self.image = pygame.image.load("hero_main.png")
        width = self.image.get_width()
        height = self.image.get_height()
        Health.__init__(self, 100)
        Physic.__init__(self, 0, 500, width, height, 0.5, 3)
        self.weapon = Weapon(20, 1)

    def tick(self, keys, floors, enemies, ghost):
        self.physic_tick(floors)
        self.weapon.tick(floors, self, enemies)
        if ghost.x_cord < self.x_cord:
            if keys[pygame.K_c]:
                weapon_image_flip = pygame.image.load("gun.png")
                self.weapon.image = pygame.transform.flip(weapon_image_flip, True, False)
                self.weapon.shoot_left()
                pygame.mixer.music.load(file_shoot)
                pygame.mixer.music.play(-1)
        elif ghost.x_cord > self.x_cord:
            self.weapon.image = pygame.image.load("gun.png")
            if keys[pygame.K_c]:
                self.weapon.shoot_right()
                pygame.mixer.music.load(file_shoot)
                pygame.mixer.music.play(-1)
        if keys[pygame.K_RIGHT] and self.hor_velocity > self.max_vel * -1:
            self.image = pygame.image.load("hero_R.png")
            self.hor_velocity += self.acc

        if keys[pygame.K_LEFT] and self.hor_velocity < self.max_vel:
            image_flip = pygame.image.load("hero_R.png")
            self.image = pygame.transform.flip(image_flip, True, False)
            self.hor_velocity -= self.acc
            if self.x_cord <= 15:
                self.hor_velocity = 0
        if keys[pygame.K_SPACE] and self.jump is False:
            self.ver_velocity -= 18
            self.jump = True
        if not (keys[pygame.K_RIGHT] or keys[pygame.K_LEFT]):
            if self.hor_velocity > 0:
                self.hor_velocity -= self.acc
            elif self.hor_velocity < 0:
                self.hor_velocity += self.acc
            self.image = pygame.image.load("hero_main.png")
            self.hor_velocity = 0

    def draw(self, window, background):
        if background.width - resolution[0] / 2 > self.x_cord >= resolution[0] / 2:
            x_screen = resolution[0] / 2
        elif self.x_cord >= background.width - resolution[0] / 2:
            x_screen = self.x_cord - background.width + resolution[0]
        else:
            x_screen = self.x_cord
        if self.x_cord >= background.width - 30:
            self.hor_velocity = 0

        self.draw_health_bar(window, x_screen, self.y_cord - 15, self.width, 5)
        window.blit(self.image, (x_screen, self.y_cord))
        self.weapon.draw(window, self.x_cord, background.x_cord)


class Ghost(Physic, Health):
    def __init__(self, x, y):
        self.image = pygame.image.load("ghost.png")
        width, height = self.image.get_size()
        Physic.__init__(self, x, y, width, height, 1, 3)
        Health.__init__(self, 100)
        self.gravity = 0.3
        self.alive = True

    def move_left(self):
        if -self.hor_velocity < self.max_vel:
            self.hor_velocity -= self.acc

    def move_right(self):
        if self.hor_velocity < self.max_vel:
            self.hor_velocity += self.acc

    def move_up(self):
        if - self.hor_velocity < self.max_vel:
            self.ver_velocity -= self.gravity + self.acc

    def tick(self, floors, hero):
        self.physic_tick(floors)
        if self.hitbox.colliderect(hero.hitbox):
            hero.damage(0.5)
        if not self.hitbox.colliderect(hero.hitbox):
            if self.y_cord > hero.y_cord + 10:
                self.move_up()
            if self.x_cord > hero.x_cord + 10:
                self.move_left()
                self.image = pygame.image.load("ghost.png")
            elif self.x_cord < hero.x_cord - 10:
                self.move_right()
                ghost_image = pygame.image.load("ghost.png")
                self.image = pygame.transform.flip(ghost_image, True, False)
        if randint(0, 20) == 15:
            self.move_up()
        if randint(0, 20) == 15:
            self.move_left()
            self.move_left()
        if randint(0, 20) == 15:
            self.move_right()
            self.move_right()

    def draw(self, window, background_x):
        window.blit(self.image, (self.x_cord + background_x, self.y_cord))
        self.draw_health_bar(window, self.x_cord + background_x, self.y_cord - 15, self.width, 5)


class Bullet(Physic):
    def __init__(self, weapon, speed, damage):
        super().__init__(weapon.x_cord, weapon.y_cord, 3, 2, 0, speed)
        self.gravity = 0.1
        self.max_bullets = 250
        self.hor_velocity = speed
        self.damage = damage
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)
        self.exist = True

    def tick(self, floors, enemies):
        self.physic_tick(floors)
        for enemy in enemies:
            if enemy.hitbox.colliderect(self.hitbox):
                enemy.damage(self.damage)
                self.exist = False

    def draw(self, window, background_x):
        pygame.draw.rect(window, (5, 5, 5), ((self.x_cord +10) + background_x, self.y_cord + 35, 5, 3))


class Weapon:
    def __init__(self, speed, damage):
        self.x_cord = 0
        self.y_cord = 0
        self.damage = damage
        self.speed = speed
        self.bullets = []
        self.image = pygame.image.load("gun.png")
        self.x_screen = 0
        self.world_x = 0
        self.width = self.image.get_width()

    def shoot_right(self):
        self.bullets.append(Bullet(self, self.speed, self.damage))

    def shoot_left(self):
        self.bullets.append(Bullet(self, - self.speed, self.damage))

    def tick(self, floors, hero, enemies):
        self.x_cord = hero.x_cord
        self.y_cord = hero.y_cord
        for bullet in self.bullets:
            bullet.tick(floors, enemies)

    def draw(self, window, x_screen, background_x):
        for bullet in self.bullets:
            bullet.draw(window, background_x)
        window.blit(self.image, ((x_screen + background_x) - 10, self.y_cord + 20))


