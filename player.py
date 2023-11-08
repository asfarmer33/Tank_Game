import pygame

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, image, x = 0, y = 0):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.x = x
        self.y = y
        self.speed = 1

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))
    def update(self):
        self.x += self.speed
        self.y += self.speed

