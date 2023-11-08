import pygame
from backgrounds import make_background
from player import Player

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = make_background(screen)

player_tank = Player(screen, "images/tank_blue.png")




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_tank.speed += 1
            if event.key == pygame.K_DOWN:
                player_tank.speed -= 1

    screen.blit(background, (0, 0))

    player_tank.update()

    player_tank.draw()


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)