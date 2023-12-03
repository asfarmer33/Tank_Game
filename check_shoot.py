import pygame
import math

class check_shoot(pygame.sprite.Sprite): # class is used to check if the enemy would be able to see the player at any angle

    def __init__(self, screen, pos, player_tank, object_group):
        super().__init__()
        self.screen = screen
        self.pos = pos
        self.x, self.y = pos
        self.player = pygame.sprite.Group()
        self.image = pygame.image.load("images/green_bullet.png")
        self.player.add(player_tank)
        self.playerx = player_tank.x
        self.playery = player_tank.y
        self.rect = pygame.Rect(pos, (10, 10))
        self.rect.center = pos
        self.angle = self.player_angle()
        self.object_group = object_group
        self.face_player = 0
        self.check_for_hit = 1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self): # move the "bullet"
        self.x += 40 * math.cos(math.pi / 2 - self.angle * math.pi / 180) # it is fast
        self.y += 40 * math.sin(math.pi / 2 - self.angle * math.pi / 180)

        self.rect.centerx = self.x
        self.rect.centery = self.y

        if self.check_hit(): # check to see if it hit the player
            self.face_player = 1 # if it did tell the enemy to look at the player

    def player_angle(self): # calculate angle to player
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
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.93))
        if collided: # if it collides with an object do not check to see if it hits the player
            self.check_for_hit = 0
            return 0
        else:
            collided = pygame.sprite.spritecollide(self, self.player, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided: # if it does not collide with an object and hits the player send back that it hit the player
            return 1
        else:
            return 0