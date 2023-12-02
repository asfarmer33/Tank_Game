import pygame
import math
import random
from levels import *


def find_path(object_array, point_array, current_point, goal_point, last_point, path_length, all_paths):
    path = []
    points = point_array
    objects = object_array
    closest_distance = 0

    return_path = []
    new_path = []
    if current_point == goal_point: # if the player is on the enemy just return the current point as the path
        return_path.append(current_point)
        return return_path
    for y in range(0, 10): # go through all the position in the array
        for x in range(0, 14):
            dist = get_distance(current_point, points[y][x])
            if dist < 65 and dist > 0: # if the position is within 64 pixels of another position add
                if objects[y][x] == 0:
                    closest_distance = -100
    if closest_distance == 0:
        closest_distance = 20

    error = 0
    for y in range(0, 10): # go through all the position in the array
        for x in range(0, 14):
            dist = get_distance(current_point, points[y][x])
            if dist < 65 and dist > 0: # if the position is within 64 pixels of another position add
                if objects[y][x] == 1: # only add it if there is not an object there
                    if points[y][x] not in path: # if the points is not already recorded
                        if points[y][x] == goal_point: # if the point is the goal point return it
                            return goal_point
                        else:
                            if points[y][x] != last_point: # makes sure it is not the same as the last point so it does not go back and forth
                                if abs(get_distance(current_point, goal_point)) - abs(get_distance(points[y][x], goal_point)) > closest_distance: # if it is moving away don't let it
                                    path_length += get_distance(current_point, points[y][x])
                                    if path_length < 10000: # if the overall path length is too long do not use it
                                        if points[y][x] not in all_paths: # if the point is already in the path do not add it
                                            new_path.append(points[y][x])
                                            all_paths.append(points[y][x])


    for items in new_path: # copy the path over if it is not already in the recorded paths
        if items not in path:
            path.append(items)

    random.shuffle(path) # shuffle the points so we can get different paths in order to find the best

    for pos in path: # for all the new paths run the equation
        point = find_path(object_array, point_array, pos, goal_point, current_point, path_length, all_paths) # recursion
        if point == goal_point: # if the point is the goal point it needs to be returned a little differently
            return_path.append(pos)
            return_path.append(goal_point)
            return return_path
        if point:
            return_path.append(pos)
            for points in point:
                return_path.append(points)
            return return_path




def path(player, enemy, level, last_player_pos, last_path):
    # array of objects
    objects = get_object_level(level)

    # array of points for enemy to go to
    points = [
        [(0, 0), (64, 0), (128, 0), (192, 0), (256, 0), (320, 0), (384, 0), (448, 0), (512, 0), (576, 0), (640, 0), (704, 0), (768, 0), (832, 0)],
        [(0, 64), (64, 64), (128, 64), (192, 64), (256, 64), (320, 64), (384, 64), (448, 64), (512, 64), (576, 64), (640, 64), (704, 64), (768, 64), (832, 64)],
        [(0, 128), (64, 128), (128, 128), (192, 128), (256, 128), (320, 128), (384, 128), (448, 128), (512, 128), (576, 128), (640, 128), (704, 128), (768, 128), (832, 128)],
        [(0, 192), (64, 192), (128, 192), (192, 192), (256, 192), (320, 192), (384, 192), (448, 192), (512, 192), (576, 192), (640, 192), (704, 192), (768, 192), (832, 192)],
        [(0, 256), (64, 256), (128, 256), (192, 256), (256, 256), (320, 256), (384, 256), (448, 256), (512, 256), (576, 256), (640, 256), (704, 256), (768, 256), (832, 256)],
        [(0, 320), (64, 320), (128, 320), (192, 320), (256, 320), (320, 320), (384, 320), (448, 320), (512, 320), (576, 320), (640, 320), (704, 320), (768, 320), (832, 320)],
        [(0, 384), (64, 384), (128, 384), (192, 384), (256, 384), (320, 384), (384, 384), (448, 384), (512, 384), (576, 384), (640, 384), (704, 384), (768, 384), (832, 384)],
        [(0, 448), (64, 448), (128, 448), (192, 448), (256, 448), (320, 448), (384, 448), (448, 448), (512, 448), (576, 448), (640, 448), (704, 448), (768, 448), (832, 448)],
        [(0, 512), (64, 512), (128, 512), (192, 512), (256, 512), (320, 512), (384, 512), (448, 512), (512, 512), (576, 512), (640, 512), (704, 512), (768, 512), (832, 512)],
        [(0, 576), (64, 576), (128, 576), (192, 576), (256, 576), (320, 576), (384, 576), (448, 576), (512, 576), (576, 576), (640, 576), (704, 576), (768, 576), (832, 576)]
        ]

    player_x, player_y = player
    enemy_x, enemy_y = enemy
    last_player_x, last_player_y = last_player_pos

    player_x_array = int(player_x / 64) # find which the x and y indexes
    player_y_array = int(player_y / 64)


    enemy_x_array = int(enemy_x / 64)
    enemy_y_array = int(enemy_y / 64)

    last_x_array = int(last_player_x / 64)
    last_y_array = int(last_player_y / 64)

    enemy_coord = points[enemy_y_array][enemy_x_array] # find the general coordinate in the position array
    player_coord = points[player_y_array][player_x_array]

    #print(f"Enemy: {enemy_coord}, Player: {player_coord}")

    if last_x_array == player_x_array and last_y_array == player_y_array and len(last_path) > 1: # if the player is in the same square just return the same path, but one shroter
        return last_path[1:]

    all_paths = []
    depth = 15
    for x in range(depth): # caclulate 10 total paths and then find the shortest (can change the depth)
        final_path = find_path(objects, points, enemy_coord, player_coord, 0, 0, [])
        all_paths.append(final_path)
    try: # sometimes it has trouble finding, so just do not run it and return a blank path
        shortest_path = all_paths[0]
        for options in all_paths:
            if len(options) <= len(shortest_path):
                shortest_path = options[:]
    except Exception as e:
        print("error shortest path")
        print(e)
        shortest_path = [player_coord]

    print(f"This is the shortest path: {shortest_path}")
    return shortest_path



def get_distance(coord1, coord2):
    x1, y1 = coord1
    x2, y2 = coord2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_distance_to_point(path, en_x, en_y):
    try:
        if get_distance((path[0][0] + 32, path[0][1] + 32), (en_x, en_y)) < 10:
            return 1
        else:
            return 0
    except:
        print("error check distance to point")

player = pygame.Rect(64, 64, 20,20) # for testing
enemy = pygame.Rect(256, 448, 20, 20)

print(path(player.center, enemy.center, 99, (0,0), (0,0)))





