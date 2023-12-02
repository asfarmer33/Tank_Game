import pygame
from bullets import Bullets

def run_game(screen, player_group, enemy_group, bullet_group, object_group, background, FPS):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            for tanks in player_group:
                if tanks.player == 1:
                    if event.key == pygame.K_SPACE:
                        bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group, 1, 1))
                if tanks.player == 2:
                    if event.key == pygame.K_LSHIFT:
                        bullet_group.add(Bullets(screen, tanks.x, tanks.y, tanks.angle, enemy_group, object_group, player_group , 1, 2))

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



def run_start_menu(screen, background, FPS, level):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    if pygame.mouse.get_pressed()[0]:
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
            if mouse_y < (screen.get_height() / 2 + 49) and mouse_y > (screen.get_height() / 2):
                print("test")
                level[0] = 1
        if mouse_x > (screen.get_width() / 2 - 190/2) and mouse_x < (screen.get_width() / 2 + 190/2):
            if mouse_y < (screen.get_height() / 2 + 49*3) and mouse_y > (screen.get_height() / 2 + 49*2):
                print("test2")


    screen.blit(background, (0, 0))

    pygame.display.flip()
    pygame.display.set_caption(f"Tank Game | FPS:{FPS.get_fps():3.2f}")
    FPS.tick(60)

