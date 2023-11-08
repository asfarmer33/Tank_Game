import pygame

def make_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))
    sand_tile = pygame.image.load('images/tileSand1.png')

    tile_width = sand_tile.get_width()
    tile_height = sand_tile.get_height()

    for x in range(0, WIDTH, tile_width):
        for y in range(0, HEIGHT, tile_height):
            background.blit(sand_tile, (x, y))

    return background