import pygame

class Can(pygame.sprite.Sprite):

    def __init__(self, screen, x, y):
        super().__init__()
        self.screen = screen
        self.image = pygame.image.load('images/sandbagBrown.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def get_height(self):
        return self.rect.height

    def get_width(self):
        return self.rect.width
