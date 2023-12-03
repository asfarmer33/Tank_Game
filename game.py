import pygame
from bullets import Bullets
from music import Music
from enemy_tanks import enemy_tank
from levels import *
import json
from backgrounds import save_background

def run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS, level, lev_com, medals, bullet_count, music, enemies_killed):
    quit_game = 0
    music.update(level[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                # if you press escape take you to the menu and clear all objects
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
                            # create a bullet for player 1
                            bullet_count[0] += 1
                            bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group, bullet_group, 1, 1))
                            shoot_sound = pygame.mixer.Sound("sounds/shoot.mp3")
                            shoot_sound.set_volume(0.1)
                            shoot_sound.play()
                if tanks.player == 2:
                    if event.key == pygame.K_LSHIFT:
                        if tanks.create_bullet():
                            # create a bullet for player 2
                            bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group, bullet_group, 1, 2))
                            shoot_sound = pygame.mixer.Sound("sounds/shoot.mp3")
                            shoot_sound.set_volume(0.1)
                            shoot_sound.play()

    for enemy in enemy_group:
        if enemy.create_bullet():
            # create a bullet for enemy
            bullet_group.add(Bullets(screen, enemy.x, enemy.y, enemy.angle, enemy_group, object_group, player_group, bullet_group, 0, 3))
            if level[0] != 12:
                # level 12 had too much sound going on
                shoot_sound = pygame.mixer.Sound("sounds/shoot.mp3")
                shoot_sound.set_volume(0.3)
                shoot_sound.play()

    screen.blit(background, (0, 0))

    # update everything
    [player.update() for player in player_group]
    [bullet.update() for bullet in bullet_group]
    [enemy.update() for enemy in enemy_group]

    # draw everything
    [bullet.draw() for bullet in bullet_group]
    [objects.draw() for objects in object_group]
    [enemy.draw() for enemy in enemy_group]
    [player.draw() for player in player_group]

    if quit_game == 0: # if you did not quit
        if level[0] == 12 and enemies_killed[0] < 10: # for level 12 keep spawning enemies
            if len(enemy_group) < 2:
                for tank in player_group:
                    if tank.player == 1:
                        enemies_killed[0] += 1
                        enemy_group.add(enemy_tank(screen, get_enemy_pos(level[0]), tank, object_group, level[0], get_enemy_dif(level[0])))
        if level[0] < 50:
            if len(enemy_group) <= 0 or len(player_group) <= 0:
                if len(enemy_group) <= 0:
                    # all these caclulate whether to give a medal or not depending on how many shots you had to get medal shots = number of enemies
                    if level[0] == 12:
                        if level[0] - 1 not in medals[0]:
                            medals[0].append(level[0] - 1)
                            medal_sound = pygame.mixer.Sound("sounds/medal_sound.wav")
                            medal_sound.set_volume(0.3)
                            medal_sound.play()
                    if level[0] < 5:
                        if bullet_count[0] <= 2:
                            if level[0] - 1 not in medals[0]:
                                medals[0].append(level[0] - 1)
                                medal_sound = pygame.mixer.Sound("sounds/medal_sound.wav")
                                medal_sound.set_volume(0.3)
                                medal_sound.play()
                    elif level[0] < 7:
                        if bullet_count[0] <= 3:
                            if level[0] - 1 not in medals[0]:
                                medals[0].append(level[0] - 1)
                                medal_sound = pygame.mixer.Sound("sounds/medal_sound.wav")
                                medal_sound.set_volume(0.3)
                                medal_sound.play()
                    elif level[0] < 9:
                        if bullet_count[0] <= 4:
                            if level[0] - 1 not in medals[0]:
                                medals[0].append(level[0] - 1)
                                medal_sound = pygame.mixer.Sound("sounds/medal_sound.wav")
                                medal_sound.set_volume(0.3)
                                medal_sound.play()
                    else:
                        if bullet_count[0] <= 5:
                            if level[0] - 1 not in medals[0]:
                                medals[0].append(level[0] - 1)
                                medal_sound = pygame.mixer.Sound("sounds/medal_sound.wav")
                                medal_sound.set_volume(0.3)
                                medal_sound.play()
                    if level[0] - 1 > lev_com[0]:
                        lev_com[0] = level[0] - 1
                    display_win_screen(screen, "You Win", music)
                else: # if the enemies remain you lose
                    display_win_screen(screen, "You Lose", music)

                level[0] = 1 # go back to level select
                # empty all the groups, so you can respawn stuff for later levels
                pygame.sprite.Group.empty(enemy_group)
                pygame.sprite.Group.empty(player_group)
                pygame.sprite.Group.empty(bullet_group)
                pygame.sprite.Group.empty(object_group)
        else: # for two players check to see who wins when someone dies
            if len(player_group) <= 1:
                for tank in player_group:
                    if tank.image_player == "images/tank_blue.png":
                        display_win_screen(screen, "Blue Wins", music)
                    else:
                        display_win_screen(screen, "Green Wins", music)
                level[0] = 51
                pygame.sprite.Group.empty(player_group)
                pygame.sprite.Group.empty(bullet_group)
                pygame.sprite.Group.empty(object_group)


    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)



def run_start_menu(screen, background, FPS, level, music):
    music.update(level[0])
    # check to see if you click on a box
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
                if mouse_y < (screen.get_height() / 2 + 49) and mouse_y > (screen.get_height() / 2):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 1
            if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
                if mouse_y < (screen.get_height() / 2 + 49*3) and mouse_y > (screen.get_height() / 2 + 49*2):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 51
            if mouse_x > 10 and mouse_x < 210:
                if mouse_y > 10 and mouse_y < 60:
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    level[0] = 100


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def run_one_player_level_menu(screen, background, FPS, level, lev_com, medals, music):
    music.update(level[0])
    # check to see if you click on a box
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
                if lev_com[0] > 9 and len(medals[0]) >= 10:
                    level[0] = 12


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def run_two_player_level_menu(screen, background, FPS, level, medals, music):
    music.update(level[0])
    # check to see if you click on a box
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
            if mouse_x > 425 and mouse_x < 500 and mouse_y > (100 + 75 * 3) and mouse_y < (175 + 75 * 3):
                if len(medals[0]) >= 11:
                    level[0] = 62



    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def run_save_screen(screen, FPS, level, music, saves, lev_com, medals):
    background = save_background(screen, saves)
    music.update(level[0])
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                level[0] = 0

        if event.type == pygame.MOUSEBUTTONDOWN:
            keys = pygame.key.get_pressed()
            mouse_x, mouse_y = pygame.mouse.get_pos()
            # if you click on a box while pressing ctr del the save
            if keys[pygame.K_LCTRL]:
                print("test")
                if mouse_x > 520 and mouse_x < 820:
                    if mouse_y > 100 and mouse_y < 175:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        print("test")
                        sound.play()
                        saves[0]['1'] = [0, []]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        saves[0]['2'] = [0, []]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        saves[0]['3'] = [0, []]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        saves[0]['4'] = [0, []]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        saves[0]['5'] = [0, []]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)

            # if you click on a box while pressing shift save
            elif keys[pygame.K_LSHIFT]:
                print("test2")
                if mouse_x > 520 and mouse_x < 820:
                    if mouse_y > 100 and mouse_y < 175:
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        with open('saves.txt', 'r') as f:
                            contents = json.load(f)
                        saves[0] = contents
                        saves[0]['1'] = [lev_com[0], medals[0]]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        with open('saves.txt', 'r') as f:
                            contents = json.load(f)
                        saves[0] = contents
                        saves[0]['2'] = [lev_com[0], medals[0]]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        with open('saves.txt', 'r') as f:
                            contents = json.load(f)
                        saves[0] = contents
                        saves[0]['3'] = [lev_com[0], medals[0]]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        with open('saves.txt', 'r') as f:
                            contents = json.load(f)
                        saves[0] = contents
                        saves[0]['4'] = [lev_com[0], medals[0]]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)
                    if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                        sound = pygame.mixer.Sound("sounds/click.wav")
                        sound.play()
                        with open('saves.txt', 'r') as f:
                            contents = json.load(f)
                        saves[0] = contents
                        saves[0]['5'] = [lev_com[0], medals[0]]
                        with open('saves.txt', 'w') as f:
                            json.dump(saves[0], f)

            # if you click on a box load
            elif mouse_x > 520 and mouse_x < 820:
                if mouse_y > 100 and mouse_y < 175:
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    with open('saves.txt', 'r') as f:
                        contents = json.load(f)
                    saves[0] = contents
                    lev_com[0] = saves[0]['1'][0]
                    medals[0] = saves[0]['1'][1]
                if mouse_y > (100 + 75 * 1.5) and mouse_y < (100 + 75 * 1.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    with open('saves.txt', 'r') as f:
                        contents = json.load(f)
                    saves[0] = contents
                    lev_com[0] = saves[0]['2'][0]
                    medals[0] = saves[0]['2'][1]
                if mouse_y > (100 + 75 * 3) and mouse_y < (100 + 75 * 3 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    with open('saves.txt', 'r') as f:
                        contents = json.load(f)
                    saves[0] = contents
                    lev_com[0] = saves[0]['3'][0]
                    medals[0] = saves[0]['3'][1]
                if mouse_y > (100 + 75 * 4.5) and mouse_y < (100 + 75 * 4.5 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    with open('saves.txt', 'r') as f:
                        contents = json.load(f)
                    saves[0] = contents
                    lev_com[0] = saves[0]['4'][0]
                    medals[0] = saves[0]['4'][1]
                if mouse_y > (100 + 75 * 6) and mouse_y < (100 + 75 * 6 + 75):
                    sound = pygame.mixer.Sound("sounds/click.wav")
                    sound.play()
                    with open('saves.txt', 'r') as f:
                        contents = json.load(f)
                    saves[0] = contents
                    lev_com[0] = saves[0]['5'][0]
                    medals[0] = saves[0]['5'][1]



    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

def display_win_screen(screen, winner, music):
    n = 0
    music.stop()
    # stop for a little and display win message and play music
    if winner != "You Lose":
        win_sound = pygame.mixer.Sound("sounds/win_sound.mp3")
        win_sound.set_volume(0.4)
    else:
        win_sound = pygame.mixer.Sound("sounds/death_sound.wav")
        win_sound.set_volume(0.2)
    win_sound.play()
    while n < 1500:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        n += 1
        my_font_bigger = pygame.font.SysFont('fonts/kenvector_future.ttf', 80)
        text = my_font_bigger.render(winner, True, (0, 0, 0))
        screen.blit(text, (300, 300))
        pygame.display.flip()
    win_sound.fadeout(500)


