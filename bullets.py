import pygame
import math

class Bullets(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, angle, enemy_group):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.reg_image = pygame.image.load('images/blue_bullet.png')
        self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
        self.bounce = 0
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.enemy_group = enemy_group
        self.collision_radius = self.reg_image.get_height() * 2

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += 5 * math.cos(math.pi/2 - self.angle*math.pi/180)
        self.y += 5 * math.sin(math.pi / 2 - self.angle * math.pi / 180)
        self.rect.x = self.x
        self.rect.y = self.y
        self.bouncing()
        self.hit_enemy()


    def bouncing(self):
        if self.x + self.image.get_width() > self.screen.get_width() or self.x < 0: # check boundaries of screen
            if self.bounce < 1: # allows it to bounce 1 time
                self.angle *= -1 # swaps angle
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
            else:
                self.kill()
        if self.y + self.image.get_height() > self.screen.get_height() or self.y < 0:
            if self.bounce < 1:
                self.angle = self.angle * -1 + 180 # swaps angle and then flips it
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
            else:
                self.kill()


    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return (self.get_distance(coord1, coord2) < self.collision_radius)

    def hit_enemy(self):
        hit_enemy_list = pygame.sprite.spritecollide(self, self.enemy_group, False, collided=self.get_sprite_distance)
        if hit_enemy_list:
            for enemy in hit_enemy_list:
                enemy.kill()
            self.kill()

