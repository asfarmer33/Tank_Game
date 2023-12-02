import pygame
from object import *
from levels import *

def make_background(screen, level):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))

    backgrounds = get_background_level(level)

    for y in range(0, 10):
        for x in range(0, 14):
            tile = backgrounds[y][x]
            tile_type = get_tile(tile)
            tile_type = pygame.transform.scale(tile_type, (64, 64))
            background.blit(tile_type, (x*64, y*64))

    return background

def get_objects(screen, level):
    object_group = pygame.sprite.Group()
    objects = get_object_level(level)
    for y in range(0, 10):
        for x in range(0, 14):
            object = objects[y][x]
            if object == 0:
                object_group.add(Can(screen, x*64, y*64))

    return object_group

def start_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))

    one_player_box_img = pygame.image.load("images/green_button00.png")
    one_player_box_rect = one_player_box_img.get_rect()
    one_player_box_rect.x = WIDTH/2 - one_player_box_rect.width/2
    one_player_box_rect.y = HEIGHT/2

    two_player_box_img = pygame.image.load("images/green_button00.png")
    two_player_box_rect = two_player_box_img.get_rect()
    two_player_box_rect.x = WIDTH / 2 - one_player_box_rect.width / 2
    two_player_box_rect.y = HEIGHT / 2 + two_player_box_rect.height * 2

    my_font_bold = pygame.font.SysFont('fonts/kenvector_future.ttf', 100, True)
    my_font_reg = pygame.font.SysFont('fonts/kenvector_future.ttf', 40)

    title = my_font_bold.render('Tank Game', True, (255, 255, 255))
    title_back = my_font_bold.render('Tank Game', True, (0, 0, 0))
    titlex = WIDTH/2 - title.get_width()/2
    titley = HEIGHT/4 - title.get_height()/2

    one_player_text = my_font_reg.render('One Player', True, (255, 255, 255))
    one_player_text_back = my_font_reg.render('One Player', True, (100, 100, 100))
    two_player_text = my_font_reg.render('Two Players', True, (255, 255, 255))
    two_player_text_back = my_font_reg.render('Two Players', True, (100, 100, 100))

    tank_left = pygame.image.load("images/tank_blue.png")
    tank_left = pygame.transform.scale(tank_left, (150,150))
    tank_left = pygame.transform.rotate(tank_left, 180)

    bullet_left = pygame.image.load("images/blue_bullet.png")
    bullet_left = pygame.transform.scale(bullet_left, (40, 80))

    tank_right = pygame.image.load("images/tank_green.png")
    tank_right = pygame.transform.scale(tank_right, (150, 150))
    tank_right = pygame.transform.rotate(tank_right, 180)

    bullet_right = pygame.image.load("images/green_bullet.png")
    bullet_right = pygame.transform.scale(bullet_right, (40, 80))


    background.fill((83, 98, 103))
    background.blit(one_player_box_img, (one_player_box_rect.x, one_player_box_rect.y))
    background.blit(two_player_box_img, (two_player_box_rect.x, two_player_box_rect.y))
    background.blit(title_back, (titlex+2, titley+2))
    background.blit(title, (titlex, titley))
    background.blit(one_player_text_back, (one_player_box_rect.x + 22, one_player_box_rect.y + 12))
    background.blit(one_player_text, (one_player_box_rect.x + 20, one_player_box_rect.y + 10))
    background.blit(two_player_text_back, (two_player_box_rect.x + 17, two_player_box_rect.y + 12))
    background.blit(two_player_text, (two_player_box_rect.x + 15, two_player_box_rect.y + 10))
    background.blit(tank_left, (90,250))
    background.blit(bullet_left, (210, 115))
    background.blit(tank_right, (650, 250))
    background.blit(bullet_right, (650, 115))



    return background



def get_tile(tile_num):
    if tile_num == 0:
        return pygame.image.load('images/tileSand1.png')
    if tile_num == 1:
        return pygame.image.load('images/tileGrass1.png')
    if tile_num == 2:
        return pygame.image.load('images/tileGrass_transitionN.png')
    if tile_num == 3:
        return pygame.image.load('images/tileGrass_transitionE.png')
    if tile_num == 4:
        return pygame.image.load('images/tileGrass_transitionS.png')
    if tile_num == 5:
        return pygame.image.load('images/tileGrass_transitionW.png')
