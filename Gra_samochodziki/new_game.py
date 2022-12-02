from cars import *

resolution = (1280, 700)

pygame.init()
pygame.display.set_caption('Gra Monisi i Michała')
window = pygame.display.set_mode((resolution))

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
    game_over = False
    #restart_button = Button(620, 300, "/home/jacek/Game/start")

    game_over_image = pygame.font.Font.render(pygame.font.SysFont("arial", 28), f"Koniec gry", True, (255, 255, 255))
    background = pygame.image.load("tlo.png")

    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        clock2 += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        #restart_button.tick()

        if game_over:
            window.blit(game_over_image,(500, 300)) 
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

        window.blit(background, (0, 0))
        window.blit(score_image_1, (20,0))
        window.blit(score_image_2, (1100,0))
        auto1.draw()
        auto2.draw()
        for obiekt in  obiekty_red:
            obiekt.draw()

        for man in people:
            man.draw()
        #restart_button.draw(window)
        pygame.display.update()

if __name__ =="__main__":
    main()