from data import *

pygame.init()
pygame.display.set_caption('Gra')
window = pygame.display.set_mode(resolution)

pygame.mixer.init()
pygame.mixer.music.load(file_main_music)
pygame.mixer.music.play(-1)


def main():
    run = True
    pause: bool = False
    ghost = Ghost(400, 300)
    background = Background()
    object = Object()
    heart = Heart()
    pause_image = pygame.font.Font.render(pygame.font.SysFont("", 50), "Pauza", True, (255, 255, 255))
    game_over_image = pygame.font.Font.render(pygame.font.SysFont("", 50), "Koniec Gry", True, (255, 255, 255))
    hero = Hero()
    balls = []
    hearts = []
    clock = 0
    clock_counter = 0
    score = 0
    floors = [
        Floor(1, 700, 5200, 10)
        ]
    while run:
        clock += pygame.time.Clock().tick(60) / 1000
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                pause = not pause

        keys = pygame.key.get_pressed()
        if pause:
            window.blit(pause_image, (630, 300))
            pygame.display.update()
            continue

        if not hero.alive:
            window.blit(game_over_image, (600, 300))
            pygame.display.update()
            continue

        if clock < 5:
            pass
        else:
            clock = 0
            clock_counter += 1
            balls.append(Object())

        if clock_counter / 3 == 1:
            hearts.append(Heart())
            clock_counter = 0

        hero.tick(keys, floors, [ghost, ], ghost)
        object.tick()

        for object in balls:
            if hero.hitbox.colliderect(object.hitbox):
                score += 1
                balls.remove(object)

        for heart in hearts:
            if hero.hitbox.colliderect(heart.hitbox):
                hero.health += 5
                hearts.remove(heart)

            if ghost.hitbox.colliderect(heart.hitbox):
                ghost.health += 5
                hearts.remove(heart)
                score -= 1

        background.tick(hero)
        score_image_1 = pygame.font.Font.render(pygame.font.SysFont("Arial Bold", 40), f"Score: {score}", True,
                                              (255, 255, 255))
        background.draw(window)
        window.blit(score_image_1, (620, 0))
        heart.tick()

        ghost.tick(floors, hero)

        if not ghost.alive:
            ghost_x = randint(0, background.width)
            ghost_y = randint(50, 400)
            ghost = Ghost(ghost_x, ghost_y)

        hero.draw(window, background)

        ghost.draw(window, background.x_cord)
        for floor in floors:
            floor.draw(window, background.x_cord)
        for object in balls:
            object.draw(window, background.x_cord)
        for heart in hearts:
            heart.draw(window, background.x_cord)
        pygame.display.update()


if __name__ == "__main__":
    main()




