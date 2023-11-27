import pygame
from backgrounds import *
from player import Player
from bullets import Bullets
from enemy_tanks import enemy_tank
from object import *

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 640
WIDTH = 768

screen = pygame.display.set_mode((WIDTH, HEIGHT))

background = make_background(screen)


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()

object_group = get_objects(screen)

player_tank = Player(screen, "images/tank_blue.png", 100, 100, object_group)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_group.add(Bullets(screen, player_tank.x, player_tank.y, player_tank.angle, enemy_group, object_group, 1))

    for enemy in enemy_group:
        if enemy.create_bullet():
            bullet_group.add(Bullets(screen, enemy.x, enemy.y, enemy.angle, enemy_group, object_group, 0))

    keys = pygame.key.get_pressed() # list of pressed keys
    if keys[pygame.K_LEFT]:
        player_tank.angle += 1.4
        player_tank.turn(1.4)
    elif keys[pygame.K_RIGHT]:
        player_tank.angle -= 1.4
        player_tank.turn(-1.4)

    screen.blit(background, (0, 0))

    if len(enemy_group) < 1:
        enemy_group.add(enemy_tank(screen, 300, 500, player_tank, object_group))




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