import sys, pygame
from random import randint

resolution = (1280, 700)

pygame.init()
pygame.display.set_caption('Gra Monisi i Michała')
window = pygame.display.set_mode((resolution))

class Auto1:
    def __init__(self):
        self.x_cord = 50
        self.y_cord = 350
        self.image = pygame.image.load("auto_1.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 12
        
    def tick(self, keys):
        if keys[pygame.K_w]:
            if self.y_cord >= -25:
                self.y_cord -= self.speed
        if keys[pygame.K_a]:
            if self.x_cord >=-20:
                self.x_cord -= self.speed
        if keys[pygame.K_s]:
            if self.y_cord <= 635:
                self.y_cord += self.speed
        if keys[pygame.K_d]:
            if self.x_cord <= 1180:
                self.x_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width - 45, self.height - 25)

    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

class Auto2:
    def __init__(self):
        self.x_cord = 1100
        self.y_cord = 350
        self.image = pygame.image.load("auto_2.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.speed = 12
        
    def tick(self, keys):
        if keys[pygame.K_RIGHT]:
            if self.x_cord <= 1185:
                self.x_cord += self.speed
        if keys[pygame.K_LEFT]:
            if self.x_cord >=-20:
                self.x_cord -= self.speed
        if keys[pygame.K_UP]:
            if self.y_cord >= -25:
                self.y_cord -= self.speed
        if keys[pygame.K_DOWN]:
            if self.y_cord <= 635:
                self.y_cord += self.speed

        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width - 45, self.height - 25)

    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

class Passenger:
    def __init__(self):
        self.x_cord = 640
        self.y_cord = 350
        self.image = pygame.image.load("gracz.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

class Objekt_red:
    def __init__(self):
        self.x_cord = randint(0, 1230)
        self.y_cord = randint(0, 650)
        self.image = pygame.image.load("ball.png")
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def tick(self):
        self.hitbox = pygame.Rect(self.x_cord, self.y_cord, self.width, self.height)

    def draw(self):
        window.blit(self.image,(self.x_cord, self.y_cord))

def main():
    run = True
    auto1 = Auto1()
    auto2 = Auto2()
    passenger = Passenger()
    clock = 0
    clock2 = 0
    score_1 = 0
    score_2 = 0
    obiekty_red = []
    people = []
    collison_with_wall = False
    game_over = False
    game_over_image = pygame.font.Font.render(pygame.font.SysFont("arial", 28), f"Koniec gry", True, (255, 255, 255))
    background = pygame.image.load("tlo.png")
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        clock2 += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if game_over:
            window.blit(game_over_image,(500, 300))
            pygame.draw.rect(window, (150, 150, 150), [590, 415, 80 , 30])
            pygame.display.update()
            continue

        keys = pygame.key.get_pressed()

        if clock >= 2:
            clock = 0
            obiekty_red.append (Objekt_red())

        if clock2 >= 5:
            clock2 = 0
            people.append (Passenger())


        auto1.tick(keys)
        for obiekt in obiekty_red:
            obiekt.tick()
        for obiekt in obiekty_red:
            if auto1.hitbox.colliderect(obiekt.hitbox):
                obiekty_red.remove(obiekt)
                score_1 += 1
        score_image_1 = pygame.font.Font.render(pygame.font.SysFont("arial", 28), f"Gracz 1: {score_1}", True, (255, 255, 255))

        for man in people:
            man.tick()
        for man in people:
            if auto1.hitbox.colliderect(passenger.hitbox):
                people.remove(man)
                score_1 +=3 

        auto2.tick(keys)
        for obiekt in obiekty_red:
            obiekt.tick()
        for obiekt in obiekty_red:
            if auto2.hitbox.colliderect(obiekt.hitbox):
                obiekty_red.remove(obiekt)
                score_2 += 1
        score_image_2 = pygame.font.Font.render(pygame.font.SysFont("arial", 28), f"Gracz 2: {score_2}", True, (255, 255, 255))

        for man in people:
            man.tick()
        for man in people:
            if auto2.hitbox.colliderect(passenger.hitbox):
                people.remove(man)
                score_2 +=3 

        if auto1.hitbox.colliderect(auto2.hitbox): 
            game_over = not game_over

        if score_1 or score_2 >= 15:
            game_over = not game_over

        window.blit(background, (0, 0))
        window.blit(score_image_1, (20,0))
        window.blit(score_image_2, (1100,0))
        auto1.draw()
        auto2.draw()
        for obiekt in  obiekty_red:
            obiekt.draw()

        for man in people:
            man.draw()

        pygame.display.update()
            
if __name__ =="__main__":
    main()