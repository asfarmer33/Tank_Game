import pygame
from bullets import Bullets
import math
from pathfinding import path

class enemy_tank(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, player_tank, object_group):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.reg_image = pygame.image.load('images/tank_sand.png')
        self.image = self.reg_image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.angle = 0
        self.turn_speed = 0.5
        self.player_tank = player_tank
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player_tank)
        self.object_group = object_group
        self.time_shot = 0
        self.time_turn = 0
        self.make_bullet = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.get_sprite_distance(self, self.player_tank) < 100:
            self.turn()
        else:
            self.move()

        if pygame.time.get_ticks() - self.time_shot > 3000 and abs(self.angle - self.player_angle()) < 50: # every 3 seconds the enemy tank can shoot and if it is looking at the player
            self.make_bullet = 1 # creates bullet that can hit the player
            self.time_shot = pygame.time.get_ticks()

    def create_bullet(self):
        if self.make_bullet == 1:
            self.make_bullet = 0
            return 1
        else:
            return 0


    def player_angle(self):
        player_x = self.player_tank.x
        player_y = self.player_tank.y
        rel_x = player_x - self.x
        rel_y = player_y - self.y
        return -math.atan2(rel_y, rel_x) * 180 / math.pi + 90

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return self.get_distance(coord1, coord2)

    def move(self):
        self.angle = self.turn_path()
        self.x += 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180)
        self.y += 1 * math.sin(math.pi / 2 - self.angle * math.pi / 180)

    def turn_path(self):
        print(self.player_tank.rect.center)
        move_path = path(self.player_tank.rect.center, self.rect.center, "test")
        next_x = move_path[0][0]
        next_y = move_path[0][1]
        rel_x = next_x - self.x
        rel_y = next_y - self.y
        return -math.atan2(rel_y, rel_x) * 180 / math.pi + 90


    def turn(self):
        original_rect = self.rect
        angle_diff = (self.player_angle() - self.angle + 180) % 360 - 180 # find the angle to face the player
        if angle_diff >= 0: # find if it needs to turn left or right
            direction = 1
        else:
            direction = -1
        self.angle += self.turn_speed * direction # change angle
        if self.check_collide(): # if it collides with an object while turning, do not turn
            self.angle -= self.turn_speed * direction
        self.angle %= 360 # keeps it within 0-360

        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def check_collide(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided:
            return 1
        else:
            return 0



