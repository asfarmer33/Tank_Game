import pygame
from backgrounds import make_background
from player import Player
from bullets import Bullets
from enemy_tanks import enemy_tank
from object import *

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 600
WIDTH = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = make_background(screen)

player_tank = Player(screen, "images/tank_blue.png", 100, 100)

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()

object_group.add(Can(screen, 400, 400))
object_group.add(Can(screen, 300, 200))
object_group.add(Can(screen, 100, 300))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(Bullets(screen, player_tank.x, player_tank.y, player_tank.angle, enemy_group, object_group))

    keys = pygame.key.get_pressed() # list of pressed keys
    if keys[pygame.K_UP]:
        player_tank.speed = 3
    elif keys[pygame.K_DOWN]:
        player_tank.speed = -3
    else:
        player_tank.speed = 0
    if keys[pygame.K_LEFT]:
        player_tank.angle += 1.4
        player_tank.turn()
    elif keys[pygame.K_RIGHT]:
        player_tank.angle -= 1.4
        player_tank.turn()

    screen.blit(background, (0, 0))

    if len(enemy_group) < 1:
        enemy_group.add(enemy_tank(screen, 300, 300, player_tank, object_group))




    player_tank.update()
    [bullet.update() for bullet in bullet_group]
    [enemy.update() for enemy in enemy_group]

    [bullet.draw() for bullet in bullet_group]
    [objects.draw() for objects in object_group]
    [enemy.draw() for enemy in enemy_group]
    player_tank.draw()


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)