import pygame
from bullets import Bullets

def run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com, medals, bullet_count):
    quit_game = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                level[0] = 0
                pygame.sprite.Group.empty(enemy_group)
                pygame.sprite.Group.empty(player_group)
                pygame.sprite.Group.empty(bullet_group)
                pygame.sprite.Group.empty(object_group)
                quit_game = 1
        if event.type == pygame.KEYDOWN:
            for tanks in player_group:
                if tanks.player == 1:
                    if event.key == pygame.K_SPACE:
                        if tanks.create_bullet():
                            bullet_count[0] += 1
                            bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group, bullet_group, 1, 1))
                if tanks.player == 2:
                    if event.key == pygame.K_LSHIFT:
                        if tanks.create_bullet():
                            bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group, bullet_group, 1, 2))

    for enemy in enemy_group:
        if enemy.create_bullet():
            bullet_group.add(Bullets(screen, enemy.x, enemy.y, enemy.angle, enemy_group, object_group, player_group, bullet_group, 0, 3))

    screen.blit(background, (0, 0))


    [player.update() for player in player_group]
    [bullet.update() for bullet in bullet_group]
    [enemy.update() for enemy in enemy_group]

    [bullet.draw() for bullet in bullet_group]
    [objects.draw() for objects in object_group]
    [enemy.draw() for enemy in enemy_group]
    [player.draw() for player in player_group]

    if quit_game == 0:
        if level[0] < 50:
            if len(enemy_group) <= 0 or len(player_group) <= 0:
                if len(enemy_group) <= 0:
                    if level[0] < 5:
                        if bullet_count[0] == 1:
                            if level[0] - 1 not in medals:
                                medals.append(level[0] - 1)
                    else:
                        if bullet_count[0] <= 2:
                            if level[0] - 1 not in medals:
                                medals.append(level[0] - 1)
                    if level[0] - 1 > lev_com[0]:
                        lev_com[0] = level[0] - 1
                    display_win_screen(screen, "You win")
                else:
                    display_win_screen(screen, "You lose")

                level[0] = 1
                pygame.sprite.Group.empty(enemy_group)
                pygame.sprite.Group.empty(player_group)
                pygame.sprite.Group.empty(bullet_group)
                pygame.sprite.Group.empty(object_group)
        else:
            if len(player_group) <= 1:
                for tank in player_group:
                    if tank.image_player == "images/tank_blue.png":
                        display_win_screen(screen, "Blue Wins")
                    else:
                        display_win_screen(screen, "Green Wins")
                level[0] = 51
                pygame.sprite.Group.empty(player_group)
                pygame.sprite.Group.empty(bullet_group)
                pygame.sprite.Group.empty(object_group)


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)



def run_start_menu(screen, background, FPS, level):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
                if mouse_y < (screen.get_height() / 2 + 49) and mouse_y > (screen.get_height() / 2):
                    print("test")
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 1
            if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
                if mouse_y < (screen.get_height() / 2 + 49*3) and mouse_y > (screen.get_height() / 2 + 49*2):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 51


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def run_one_player_level_menu(screen, background, FPS, level, lev_com, medals):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                level[0] = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 70 and mouse_x < 370:
                if mouse_y > 100 and mouse_y < 175:
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 2
                if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                    if lev_com[0] > 0:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 3
                if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                    if lev_com[0] > 1:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 4
                if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                    if lev_com[0] > 2:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 5
                if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                    if lev_com[0] > 3:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 6
            if mouse_x > 526 and mouse_x < 826:
                if mouse_y > 100 and mouse_y < 175:
                    if lev_com[0] > 4:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 7
                if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                    if lev_com[0] > 5:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 8
                if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                    if lev_com[0] > 6:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 9
                if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                    if lev_com[0] > 7:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 10
                if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                    if lev_com[0] > 8:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        level[0] = 11
            if mouse_x > 425 and mouse_x < 500 and mouse_y > (100 + 75 * 3) and mouse_y < (175 + 75 * 3):
                if lev_com[0] > 9 and len(medals) >= 10:
                    level[0] = 12


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def run_two_player_level_menu(screen, background, FPS, level):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                level[0] = 0
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > 70 and mouse_x < 370:
                if mouse_y > 100 and mouse_y < 175:
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 52
                if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 53
                if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 54
                if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 55
                if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 56
            if mouse_x > 526 and mouse_x < 826:
                if mouse_y > 100 and mouse_y < 175:
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 57
                if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 58
                if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 59
                if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 60
                if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 61


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def display_win_screen(screen, winner):
    n = 0
    while n < 1000:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        n += 1
        my_font_bigger = pygame.font.SysFont('fonts/kenvector_future.ttf', 80)
        text = my_font_bigger.render(winner, True, (0, 0, 0))
        screen.blit(text, (300, 300))
        pygame.display.flip()


