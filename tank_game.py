import pygame
from backgrounds import *
from player import Player
from bullets import Bullets
from enemy_tanks import enemy_tank
from object import *

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 640
WIDTH = 896

screen = pygame.display.set_mode((WIDTH, HEIGHT))

print(screen.get_width())

background = make_background(screen)


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

object_group = get_objects(screen)

player_tank = Player(screen, "images/tank_blue.png", 100, 100, object_group, 1)
player2_tank = Player(screen, "images/tank_green.png", 100, 500, object_group, 2)

player_group.add(player_tank)
player_group.add(player2_tank)

enemy_group.add(enemy_tank(screen, 300, 500, player_tank, object_group))



running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            for tanks in player_group:
                if tanks.player == 1:
                    if event.key == pygame.K_SPACE:
                        bullet_group.add(Bullets(screen, player_tank.x, player_tank.y, player_tank.angle, enemy_group, object_group, player_group, 1, 1))
                if tanks.player == 2:
                    if event.key == pygame.K_LSHIFT:
                        bullet_group.add(Bullets(screen, player2_tank.x, player2_tank.y, player2_tank.angle, enemy_group, object_group, player_group , 1, 2))

    for enemy in enemy_group:
        if enemy.create_bullet():
            bullet_group.add(Bullets(screen, enemy.x, enemy.y, enemy.angle, enemy_group, object_group, player_group, 0, 3))

    screen.blit(background, (0, 0))


    [player.update() for player in player_group]
    [bullet.update() for bullet in bullet_group]
    [enemy.update() for enemy in enemy_group]

    [bullet.draw() for bullet in bullet_group]
    [objects.draw() for objects in object_group]
    [enemy.draw() for enemy in enemy_group]
    [player.draw() for player in player_group]


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)