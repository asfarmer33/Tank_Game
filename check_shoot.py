import pygame
import math

class check_shoot(pygame.sprite.Sprite):

    def __init__(self, screen, pos, player_tank, object_group):
        super().__init__()
        self.screen = screen
        self.x, self.y = pos
        self.playerx = player_tank.x
        self.playery = player_tank.y
        self.rect = pygame.Rect(pos, (10, 10))
        self.rect.center = pos
        self.angle = self.player_angle()
        self.object_group = object_group
        self.face_player = 0

    def update(self):
        self.x += 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180)
        self.y += 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180)

        self.rect.centerx = self.x
        self.rect.centery = self.y

        if self.check_hit():
            self.face_player = 1

    def player_angle(self):
        player_x = self.playerx
        player_y = self.playery
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

    def check_hit(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided:
            return 1
        else:
            collided = pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided:
            return 1
        else:
            return 0