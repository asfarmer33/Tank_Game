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


def one_player_background(screen, lev_com, medals):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((83, 98, 103))

    yb = "images/yellow_button00.png"
    rb = "images/red_button00.png"
    medal_img = pygame.image.load("images/flat_medal4.png")

    my_font_reg = pygame.font.SysFont('fonts/kenvector_future.ttf', 65)
    my_font_bigger = pygame.font.SysFont('fonts/kenvector_future.ttf', 80)


    # load text
    top_text = my_font_bigger.render("One Player Level Select", True, (255, 255, 255))
    top_text_back = my_font_bigger.render("One Player Level Select", True, (0, 0, 0))

    lev1_text = my_font_reg.render('Level One', True, (255, 255, 255))
    lev1_text_back = my_font_reg.render('Level One', True, (100, 100, 100))

    lev2_text = my_font_reg.render('Level Two', True, (255, 255, 255))
    lev2_text_back = my_font_reg.render('Level Two', True, (100, 100, 100))

    lev3_text = my_font_reg.render('Level Three', True, (255, 255, 255))
    lev3_text_back = my_font_reg.render('Level Three', True, (100, 100, 100))

    lev4_text = my_font_reg.render('Level Four', True, (255, 255, 255))
    lev4_text_back = my_font_reg.render('Level Four', True, (100, 100, 100))

    lev5_text = my_font_reg.render('Level Five', True, (255, 255, 255))
    lev5_text_back = my_font_reg.render('Level Five', True, (100, 100, 100))

    lev6_text = my_font_reg.render('Level Six', True, (255, 255, 255))
    lev6_text_back = my_font_reg.render('Level Six', True, (100, 100, 100))

    lev7_text = my_font_reg.render('Level Seven', True, (255, 255, 255))
    lev7_text_back = my_font_reg.render('Level Seven', True, (100, 100, 100))

    lev8_text = my_font_reg.render('Level Eight', True, (255, 255, 255))
    lev8_text_back = my_font_reg.render('Level Eight', True, (100, 100, 100))

    lev9_text = my_font_reg.render('Level Nine', True, (255, 255, 255))
    lev9_text_back = my_font_reg.render('Level Nine', True, (100, 100, 100))

    lev10_text = my_font_reg.render('Level Ten', True, (255, 255, 255))
    lev10_text_back = my_font_reg.render('Level Ten', True, (100, 100, 100))

    lev11_text = my_font_reg.render('11', True, (255, 255, 255))
    lev11_text_back = my_font_reg.render('11', True, (100, 100, 100))



    # load images
    lev1_img = pygame.image.load(yb)
    lev1_img = pygame.transform.scale(lev1_img, (300, 75))

    if lev_com[0] > 0:
        lev2_img = pygame.image.load(yb)
    else:
        lev2_img = pygame.image.load(rb)
    lev2_img = pygame.transform.scale(lev2_img, (300, 75))

    if lev_com[0] > 1:
        lev3_img = pygame.image.load(yb)
    else:
        lev3_img = pygame.image.load(rb)
    lev3_img = pygame.transform.scale(lev3_img, (300, 75))

    if lev_com[0] > 2:
        lev4_img = pygame.image.load(yb)
    else:
        lev4_img = pygame.image.load(rb)
    lev4_img = pygame.transform.scale(lev4_img, (300, 75))

    if lev_com[0] > 3:
        lev5_img = pygame.image.load(yb)
    else:
        lev5_img = pygame.image.load(rb)
    lev5_img = pygame.transform.scale(lev5_img, (300, 75))

    if lev_com[0] > 4:
        lev6_img = pygame.image.load(yb)
    else:
        lev6_img = pygame.image.load(rb)
    lev6_img = pygame.transform.scale(lev6_img, (300, 75))

    if lev_com[0] > 5:
        lev7_img = pygame.image.load(yb)
    else:
        lev7_img = pygame.image.load(rb)
    lev7_img = pygame.transform.scale(lev7_img, (300, 75))

    if lev_com[0] > 6:
        lev8_img = pygame.image.load(yb)
    else:
        lev8_img = pygame.image.load(rb)
    lev8_img = pygame.transform.scale(lev8_img, (300, 75))

    if lev_com[0] > 7:
        lev9_img = pygame.image.load(yb)
    else:
        lev9_img = pygame.image.load(rb)
    lev9_img = pygame.transform.scale(lev9_img, (300, 75))

    if lev_com[0] > 8:
        lev10_img = pygame.image.load(yb)
    else:
        lev10_img = pygame.image.load(rb)
    lev10_img = pygame.transform.scale(lev10_img, (300, 75))

    lev11_img = pygame.image.load(yb)
    lev11_img = pygame.transform.scale(lev11_img, (75, 75))

    background.blit(lev1_img, (70, 100))
    background.blit(lev1_text_back, (112, 117))
    background.blit(lev1_text, (110, 115))
    if 1 in medals:
        background.blit(medal_img, (370, 100))

    background.blit(lev2_img, (70, 100 + 75 * 1.5))
    background.blit(lev2_text_back, (112, 115 + 75 * 1.5 + 2))
    background.blit(lev2_text, (110, 115 + 75 * 1.5))
    if 2 in medals:
        background.blit(medal_img, (370, 100 + 75 * 1.5))

    background.blit(lev3_img, (70, 100 + 75 * 3))
    background.blit(lev3_text_back, (92, 115 + 75 * 3 + 2))
    background.blit(lev3_text, (90, 115 + 75 * 3))
    if 3 in medals:
        background.blit(medal_img, (370, 100 + 75 * 3))

    background.blit(lev4_img, (70, 100 + 75 * 4.5))
    background.blit(lev4_text_back, (102, 115 + 75 * 4.5 + 2))
    background.blit(lev4_text, (100, 115 + 75 * 4.5))
    if 4 in medals:
        background.blit(medal_img, (370, 100 + 75 * 4.5))

    background.blit(lev5_img, (70, 100 + 75 * 6))
    background.blit(lev5_text_back, (102, 115 + 75 * 6 + 2))
    background.blit(lev5_text, (100, 115 + 75 * 6))
    if 5 in medals:
        background.blit(medal_img, (370, 100 + 75 * 6))

    background.blit(lev6_img, (526, 100))
    background.blit(lev6_text_back, (568, 117))
    background.blit(lev6_text, (566, 115))
    if 6 in medals:
        background.blit(medal_img, (826, 100))

    background.blit(lev7_img, (526, 100 + 75 * 1.5))
    background.blit(lev7_text_back, (548, 115 + 75 * 1.5 + 2))
    background.blit(lev7_text, (546, 115 + 75 * 1.5))
    if 7 in medals:
        background.blit(medal_img, (826, 100 + 75 * 1.5))

    background.blit(lev8_img, (526, 100 + 75 * 3))
    background.blit(lev8_text_back, (548, 115 + 75 * 3 + 2))
    background.blit(lev8_text, (546, 115 + 75 * 3))
    if 8 in medals:
        background.blit(medal_img, (826, 100 + 75 * 3))

    background.blit(lev9_img, (526, 100 + 75 * 4.5))
    background.blit(lev9_text_back, (558, 115 + 75 * 4.5 + 2))
    background.blit(lev9_text, (556, 115 + 75 * 4.5))
    if 9 in medals:
        background.blit(medal_img, (826, 100 + 75 * 4.5))

    background.blit(lev10_img, (526, 100 + 75 * 6))
    background.blit(lev10_text_back, (568, 115 + 75 * 6 + 2))
    background.blit(lev10_text, (566, 115 + 75 * 6))
    if 10 in medals:
        background.blit(medal_img, (826, 100 + 75 * 6))

    if len(medals) >= 10:
        background.blit(lev11_img, (425, 100 + 75 * 3))
        background.blit(lev11_text_back, (440, 117 + 75 * 3))
        background.blit(lev11_text, (438, 115 + 75 * 3))

    background.blit(top_text_back, (127, 22))
    background.blit(top_text, (125, 20))

    return background

def two_player_background(screen):
    WIDTH = screen.get_width()
    HEIGHT = screen.get_height()
    background = pygame.Surface((WIDTH, HEIGHT))
    background.fill((83, 98, 103))

    yb = "images/yellow_button00.png"

    my_font_reg = pygame.font.SysFont('fonts/kenvector_future.ttf', 65)
    my_font_bigger = pygame.font.SysFont('fonts/kenvector_future.ttf', 80)


    # load text
    top_text = my_font_bigger.render("Two Player Level Select", True, (255, 255, 255))
    top_text_back = my_font_bigger.render("Two Player Level Select", True, (0, 0, 0))

    lev1_text = my_font_reg.render('Level One', True, (255, 255, 255))
    lev1_text_back = my_font_reg.render('Level One', True, (100, 100, 100))

    lev2_text = my_font_reg.render('Level Two', True, (255, 255, 255))
    lev2_text_back = my_font_reg.render('Level Two', True, (100, 100, 100))

    lev3_text = my_font_reg.render('Level Three', True, (255, 255, 255))
    lev3_text_back = my_font_reg.render('Level Three', True, (100, 100, 100))

    lev4_text = my_font_reg.render('Level Four', True, (255, 255, 255))
    lev4_text_back = my_font_reg.render('Level Four', True, (100, 100, 100))

    lev5_text = my_font_reg.render('Level Five', True, (255, 255, 255))
    lev5_text_back = my_font_reg.render('Level Five', True, (100, 100, 100))

    lev6_text = my_font_reg.render('Level Six', True, (255, 255, 255))
    lev6_text_back = my_font_reg.render('Level Six', True, (100, 100, 100))

    lev7_text = my_font_reg.render('Level Seven', True, (255, 255, 255))
    lev7_text_back = my_font_reg.render('Level Seven', True, (100, 100, 100))

    lev8_text = my_font_reg.render('Level Eight', True, (255, 255, 255))
    lev8_text_back = my_font_reg.render('Level Eight', True, (100, 100, 100))

    lev9_text = my_font_reg.render('Level Nine', True, (255, 255, 255))
    lev9_text_back = my_font_reg.render('Level Nine', True, (100, 100, 100))

    lev10_text = my_font_reg.render('Level Ten', True, (255, 255, 255))
    lev10_text_back = my_font_reg.render('Level Ten', True, (100, 100, 100))

    # load images
    lev1_img = pygame.image.load(yb)
    lev1_img = pygame.transform.scale(lev1_img, (300, 75))

    lev2_img = pygame.image.load(yb)
    lev2_img = pygame.transform.scale(lev2_img, (300, 75))

    lev3_img = pygame.image.load(yb)
    lev3_img = pygame.transform.scale(lev3_img, (300, 75))

    lev4_img = pygame.image.load(yb)
    lev4_img = pygame.transform.scale(lev4_img, (300, 75))

    lev5_img = pygame.image.load(yb)
    lev5_img = pygame.transform.scale(lev5_img, (300, 75))

    lev6_img = pygame.image.load(yb)
    lev6_img = pygame.transform.scale(lev6_img, (300, 75))

    lev7_img = pygame.image.load(yb)
    lev7_img = pygame.transform.scale(lev7_img, (300, 75))

    lev8_img = pygame.image.load(yb)
    lev8_img = pygame.transform.scale(lev8_img, (300, 75))

    lev9_img = pygame.image.load(yb)
    lev9_img = pygame.transform.scale(lev9_img, (300, 75))

    lev10_img = pygame.image.load(yb)
    lev10_img = pygame.transform.scale(lev10_img, (300, 75))

    background.blit(lev1_img, (70, 100))
    background.blit(lev1_text_back, (112, 117))
    background.blit(lev1_text, (110, 115))

    background.blit(lev2_img, (70, 100 + 75 * 1.5))
    background.blit(lev2_text_back, (112, 115 + 75 * 1.5 + 2))
    background.blit(lev2_text, (110, 115 + 75 * 1.5))

    background.blit(lev3_img, (70, 100 + 75 * 3))
    background.blit(lev3_text_back, (92, 115 + 75 * 3 + 2))
    background.blit(lev3_text, (90, 115 + 75 * 3))

    background.blit(lev4_img, (70, 100 + 75 * 4.5))
    background.blit(lev4_text_back, (102, 115 + 75 * 4.5 + 2))
    background.blit(lev4_text, (100, 115 + 75 * 4.5))

    background.blit(lev5_img, (70, 100 + 75 * 6))
    background.blit(lev5_text_back, (102, 115 + 75 * 6 + 2))
    background.blit(lev5_text, (100, 115 + 75 * 6))

    background.blit(lev6_img, (526, 100))
    background.blit(lev6_text_back, (568, 117))
    background.blit(lev6_text, (566, 115))

    background.blit(lev7_img, (526, 100 + 75 * 1.5))
    background.blit(lev7_text_back, (548, 115 + 75 * 1.5 + 2))
    background.blit(lev7_text, (546, 115 + 75 * 1.5))

    background.blit(lev8_img, (526, 100 + 75 * 3))
    background.blit(lev8_text_back, (548, 115 + 75 * 3 + 2))
    background.blit(lev8_text, (546, 115 + 75 * 3))

    background.blit(lev9_img, (526, 100 + 75 * 4.5))
    background.blit(lev9_text_back, (558, 115 + 75 * 4.5 + 2))
    background.blit(lev9_text, (556, 115 + 75 * 4.5))

    background.blit(lev10_img, (526, 100 + 75 * 6))
    background.blit(lev10_text_back, (568, 115 + 75 * 6 + 2))
    background.blit(lev10_text, (566, 115 + 75 * 6))

    background.blit(top_text_back, (127, 22))
    background.blit(top_text, (125, 20))

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
