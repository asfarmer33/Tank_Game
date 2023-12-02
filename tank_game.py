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

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

level = [0]
lev_com = [0]

running = True
while running:

    if level[0] == 0:
        background = start_background(screen)
        while level[0] == 0:
            print(pygame.mouse.get_pos())
            run_start_menu(screen, background, FPS, level)
    elif level[0] == 1:
        background = one_player_background(screen, lev_com)
        while level[0] == 1:
            run_one_player_level_menu(screen, background, FPS, level, lev_com)
    elif level[0] > 1 and level[0] < 50:
        background = make_background(screen, level[0])

        object_group = get_objects(screen, level[0])

        player_tank = Player(screen, "images/tank_blue.png", get_player_pos(level[0]), object_group, 1)
        player_group.add(player_tank)

        enemy_group.add(enemy_tank(screen, get_enemy_pos(level[0]), player_tank, object_group, level[0]))
        while level[0] > 1:
            run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com)
    elif level[0] == 51:
        background = two_player_background(screen)
        while level[0] == 51:
            run_two_player_level_menu(screen, background, FPS, level)
    elif level[0] >= 51:
        background = make_background(screen, level[0])

        object_group = get_objects(screen, level[0])

        player_tank = Player(screen, "images/tank_blue.png", get_player_pos(level[0]), object_group, 1)
        player2_tank = Player(screen, "images/tank_green.png", get_enemy_pos(level[0]), object_group, 2)

        player_group.add(player_tank)
        player_group.add(player2_tank)

        while level[0] >= 51:
            run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com)

