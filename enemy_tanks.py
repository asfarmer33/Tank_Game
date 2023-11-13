import pygame
from bullets import Bullets
import math

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
        self.bullet_group = pygame.sprite.Group()
        self.object_group = object_group
        self.time_shot = 0
        self.time_turn = 0

    def draw(self):
        [bullet.draw() for bullet in self.bullet_group]
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()
        self.turn()
        if pygame.time.get_ticks() - self.time_shot > 3000 and abs(self.angle - self.player_angle()) < 50: # every 3 seconds the enemy tank can shoot and if it is looking at the player
            self.bullet_group.add(Bullets(self.screen, self.x, self.y, self.angle, self.player_group, self.object_group))  # creates bullet that can hit the player
            self.time_shot = pygame.time.get_ticks()
        [bullet.update() for bullet in self.bullet_group]

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
        if self.get_sprite_distance(self, self.player_tank) < 600 and self.get_sprite_distance(self, self.player_tank) > 200 or abs(self.player_angle() - self.angle) == 0:
            self.x += 1 * math.cos(math.pi/2 - self.angle*math.pi/180)
            self.y += 1 * math.sin(math.pi/2 - self.angle*math.pi/180)
            self.turn_speed = 1.4
        else:
            self.turn_speed = 0.5

    def turn(self):
        angle_diff = (self.player_angle() - self.angle + 180) % 360 - 180
        if angle_diff >= 0:
            direction = 1
        else:
            direction = -1
        self.angle += self.turn_speed * direction
        self.angle %= 360 # keeps it within 0-360

        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))




