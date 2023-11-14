import pygame
import math

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, image, x, y, object_group):
        super().__init__()
        self.screen = screen
        self.reg_image = pygame.image.load(image)
        self.image = self.reg_image
        self.x = x
        self.y = y
        self.rotate = 0
        self.speed = 0
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.object_group = object_group

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        old_x = self.x
        old_y = self.y

        self.move()
        collided = pygame.sprite.spritecollide(self, self.object_group, False)
        if collided:
            self.x = old_x
            self.y = old_y

        self.rect.centerx = self.x
        self.rect.centery = self.y
    def turn(self):
        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.angle %= 360

    def check_collide(self, x, y):
        for object in self.object_group:
            if self.rect.colliderect(object):
                self.x = x
                self.y = y

    def move(self):
        self.movex()
        self.movey()

    def movex(self):
        if (self.x - self.rect.width/2) > 0 and (self.x + self.rect.width/2) < self.screen.get_width():
            self.x += self.speed * math.cos(math.pi/2 - self.angle*math.pi/180)
        else:
            self.x += self.speed * math.cos(math.pi / 2 - self.angle * math.pi / 180) * 0.02

    def movey(self):
        if (self.y - self.rect.height/2) > 0 and (self.y + self.rect.height/2) < self.screen.get_height():
            self.y += self.speed * math.sin(math.pi/2 - self.angle*math.pi/180)
        else:
            self.y += self.speed * math.sin(math.pi / 2 - self.angle * math.pi / 180) * 0.02
