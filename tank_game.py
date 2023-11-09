import pygame
from backgrounds import make_background
from player import Player
from bullets import Bullets

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = make_background(screen)

player_tank = Player(screen, "images/tank_blue.png", 100, 100)

bullet_group = pygame.sprite.Group()




running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(Bullets(screen, player_tank.x, player_tank.y, player_tank.angle))

    keys = pygame.key.get_pressed() # list of pressed keys
    if keys[pygame.K_UP]:
        player_tank.speed = 1
    elif keys[pygame.K_DOWN]:
        player_tank.speed = -1
    else:
        player_tank.speed = 0
    if keys[pygame.K_LEFT]:
        player_tank.angle += 2
        player_tank.turn()
    elif keys[pygame.K_RIGHT]:
        player_tank.angle -= 2
        player_tank.turn()

    screen.blit(background, (0, 0))

    player_tank.update()
    [bullet.update() for bullet in bullet_group]


    [bullet.draw() for bullet in bullet_group]
    player_tank.draw()


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)