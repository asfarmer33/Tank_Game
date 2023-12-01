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
