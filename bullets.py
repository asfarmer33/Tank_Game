import pygame
import math

class Bullets(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, angle):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.reg_image = pygame.image.load('images/blue_bullet.png')
        self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
        self.bounce = 0

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y))

    def update(self):
        self.x += 5 * math.cos(math.pi/2 - self.angle*math.pi/180)
        self.y += 5 * math.sin(math.pi / 2 - self.angle * math.pi / 180)
        self.bounce()


    def bounce(self):
        if self.x + self.image.get_width() > self.screen.get_width() or self.x < 0: # check boundaries of screen
            if self.bounce < 3: # allows it to bounce 3 times
                self.angle *= -1 # swaps angle
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
            else:
                self.kill()
        if self.y + self.image.get_height() > self.screen.get_height() or self.y < 0:
            if self.bounce < 3:
                self.angle = self.angle * -1 + 180 # swaps angle and then flips it
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
            else:
                self.kill()

