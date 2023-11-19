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
        self.path = []

    def draw(self):
        self.screen.blit(self.image, self.rect)
    def update(self):
        self.move()

        self.rect.centerx = self.x
        self.rect.centery = self.y

    def turn(self, turn):
        original_rect = self.rect
        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center = (self.x, self.y))
        self.angle %= 360
        collided = pygame.sprite.spritecollide(self, self.object_group, False)
        if collided:
            self.rect = original_rect
            self.angle -= turn

    def move(self):
        keys = pygame.key.get_pressed()  # list of pressed keys

        if keys[pygame.K_UP]:
            self.speed = 3
        elif keys[pygame.K_DOWN]:
            self.speed = -3
        else:
            self.speed = 0

        self.movex()
        self.movey()

        self.path.append(self.rect.center) # adds position to list
        self.path = self.path[-2:] # list of last two positions

        if self.check_collide():
            self.x, self.y = self.path[0] # if it collides with an object it goes back to its position two positions ago



    def movex(self):
        if (self.x - self.rect.width/2) > 0 and (self.x + self.rect.width/2) < self.screen.get_width():
            self.x += self.speed * math.cos(math.pi/2 - self.angle*math.pi/180)
        else:
            self.x, self.y = self.path[0]

    def movey(self):
        if (self.y - self.rect.height/2) > 0 and (self.y + self.rect.height/2) < self.screen.get_height():
            self.y += self.speed * math.sin(math.pi/2 - self.angle*math.pi/180)
        else:
            self.x, self.y = self.path[0]

    def check_collide(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided:
            return 1
        else:
            return 0

