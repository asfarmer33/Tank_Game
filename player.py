import pygame
import math

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, image, x = 0, y = 0):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.rot_image = self.image
        self.x = x
        self.y = y
        self.rotate = 0
        self.speed = 0
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def draw(self):
        self.screen.blit(self.rot_image, self.rect)
    def update(self):
        if (self.x - self.rect.width/2) > 0 and (self.x + self.rect.width/2) < self.screen.get_width():
            self.x += self.speed * math.cos(math.pi/2 - self.angle*math.pi/180)
        if (self.y - self.rect.height/2) > 0 and (self.y + self.rect.height/2) < self.screen.get_height():
            self.y += self.speed * math.sin(math.pi/2 - self.angle*math.pi/180)
        self.rect.centerx = self.x
        self.rect.centery = self.y

    def turn(self):
        self.rot_image = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.rot_image.get_rect(center = (self.x, self.y))

