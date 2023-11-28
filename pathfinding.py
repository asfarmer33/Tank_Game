import pygame


object_array = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        ]
def get_array(object_array, player_x, player_y, enemy_x, enemy_y):
    player_x_array = int(player_x / 64)
    player_y_array = int(player_y / 64)

    enemy_x_array = int(enemy_x / 64)
    enemy_y_array = int(enemy_y / 64)

    object_array[player_y_array][player_x_array] = 2
    object_array[enemy_y_array][enemy_x_array] = 3

    for y in range(0,10):
        for x in range(0,12):
            print(object_array[x][y])

player_x = 20
player_y = 20
enemy_x = 300
enemy_y = 300

get_array(object_array, player_x, player_y, enemy_x, enemy_y)