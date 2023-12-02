import pygame
from backgrounds import *
from player import Player
from bullets import Bullets
from enemy_tanks import enemy_tank
from object import *
from levels import *
from game import *

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 640
WIDTH = 896

screen = pygame.display.set_mode((WIDTH, HEIGHT))

level = 99

print(screen.get_width())

background = make_background(screen, level)


bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

object_group = get_objects(screen, level)

player_tank = Player(screen, "images/tank_blue.png", get_player_pos(level), object_group, 1)
#player2_tank = Player(screen, "images/tank_green.png", (0,0), object_group, 2)

player_group.add(player_tank)
#player_group.add(player2_tank)

enemy_group.add(enemy_tank(screen, get_enemy_pos(level), player_tank, object_group, level))



running = True
while running:


    if level == 0:
        background = start_background(screen)
        while level == 0:
            run_start_menu(screen, background)
    if level > 0:
        run_game(screen, player_group, enemy_group, bullet_group, object_group, background)

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)
