import pygame
from backgrounds import *
from player import Player
from bullets import Bullets
from enemy_tanks import *
from object import *
from levels import *
from game import *
from music import Music
import json

pygame.init()
FPS = pygame.time.Clock()

HEIGHT = 640
WIDTH = 896

screen = pygame.display.set_mode((WIDTH, HEIGHT))

bullet_group = pygame.sprite.Group()
enemy_group = pygame.sprite.Group()
object_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

shoot_sound = pygame.mixer.Sound("sounds/shoot.mp3")
shoot_sound.set_volume(0.1)



level = [0]
lev_com = [0]
medals = [[]]
with open('saves.txt', 'r') as f:
    contents = json.load(f)
saves = [0]
saves[0] = contents


music = Music()

running = True
while running:
    bullet_count = [0]
    enemies_killed = [0]

    if level[0] == 0: # main menu
        background = start_background(screen)
        while level[0] == 0:
            run_start_menu(screen, background, FPS, level, music)
    elif level[0] == 100: # save menu
        background = save_background(screen, saves)
        while level[0] == 100:
            run_save_screen(screen, FPS, level, music, saves, lev_com, medals)
    elif level[0] == 1: # one player menu
        background = one_player_background(screen, lev_com, medals)
        while level[0] == 1:
            run_one_player_level_menu(screen, background, FPS, level, lev_com, medals, music)
    elif level[0] > 1 and level[0] < 50: # one player levels
        background = make_background(screen, level[0])

        object_group = get_objects(screen, level[0])

        player_tank = Player(screen, "images/tank_blue.png", get_player_pos(level[0]), object_group, 1)
        player_group.add(player_tank)

        enemy_group.add(enemy_tank(screen, get_enemy_pos(level[0]), player_tank, object_group, level[0], get_enemy_dif(level[0])))
        if level[0] != 12: # if not level 11 add a stationary enemy
            enemy_group.add(st_enemy_tank(screen, get_stenemy_pos(level[0]), player_tank, object_group, level[0], get_stenemy_dif(level[0])))
        if level[0] > 4 and level[0] != 12: # levels 1-3 have only one stationary enemy
            enemy_group.add(st_enemy_tank(screen, get_stenemy2_pos(level[0]), player_tank, object_group, level[0], get_stenemy_dif(level[0])))
        if level[0] > 8 and level[0] != 12: # levels 4-7 have two stationary enemies and 8-10 have three
            enemy_group.add(st_enemy_tank(screen, get_stenemy3_pos(level[0]), player_tank, object_group, level[0], get_stenemy_dif(level[0])))
        if level[0] > 6: # 1-5 only have one moving enemy while 6-10 have two
            enemy_group.add(enemy_tank(screen, get_enemy2_pos(level[0]), player_tank, object_group, level[0], get_enemy_dif(level[0])))
        while level[0] > 1:
            run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com, medals, bullet_count, music, enemies_killed, shoot_sound)
    elif level[0] == 51: # two player menu
        background = two_player_background(screen, medals)
        while level[0] == 51:
            run_two_player_level_menu(screen, background, FPS, level, medals, music)
    elif level[0] > 51 and level[0] < 99: # two player levels
        background = make_background(screen, level[0])

        object_group = get_objects(screen, level[0])

        player_tank = Player(screen, "images/tank_blue.png", get_player_pos(level[0]), object_group, 1)
        player2_tank = Player(screen, "images/tank_green.png", get_enemy_pos(level[0]), object_group, 2)

        player_group.add(player_tank)
        player_group.add(player2_tank)

        while level[0] > 51 and level[0] < 99:
            run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com, medals, bullet_count, music, enemies_killed, shoot_sound)

