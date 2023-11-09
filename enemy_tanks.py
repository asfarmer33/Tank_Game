import pygame
from bullets import Bullets
import math

class enemy_tank(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, player_tank):
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
        self.player_tank = player_tank
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player_tank)
        self.bullet_group = pygame.sprite.Group()
        self.time_shot = 0

    def draw(self):
        [bullet.draw() for bullet in self.bullet_group]
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.y += 0
        if pygame.time.get_ticks() - self.time_shot > 3000: # every 3 seconds the enemy tank can shoot
            self.bullet_group.add(Bullets(self.screen, self.x, self.y, self.player_angle(), self.player_group))  # creates bullet that can hit the player
            self.time_shot = pygame.time.get_ticks()
        [bullet.update() for bullet in self.bullet_group]
        self.turn()
        self.rect.centerx = self.x
        self.rect.centery = self.y


    def player_angle(self):
        player_x = self.player_tank.x
        player_y = self.player_tank.y
        rel_x = player_x - self.x
        rel_y = player_y - self.y
        return -math.atan2(rel_y, rel_x) * 180 / math.pi - 270

    def turn(self):
        self.image = pygame.transform.rotate(self.reg_image, self.player_angle())
        self.rect = self.image.get_rect(center=(self.x, self.y))


