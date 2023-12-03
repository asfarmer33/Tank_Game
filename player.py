import pygame
import math

class Player(pygame.sprite.Sprite):

    def __init__(self, screen, image, pos, object_group, player):
        super().__init__()
        self.screen = screen
        self.image_player = image
        self.reg_image = pygame.image.load(image)
        self.reg_image = pygame.transform.scale(self.reg_image, (40, 40))
        if image == "images/tank_blue.png":
            self.reg_shoot_img = pygame.image.load("images/tank_blue_shoot.png")
            self.reg_shoot_img = pygame.transform.scale(self.reg_shoot_img, (40, 40))
        else:
            self.reg_shoot_img = pygame.image.load("images/tank_green_shoot.png")
            self.reg_shoot_img = pygame.transform.scale(self.reg_shoot_img, (40, 40))
        self.reg_not_shoot_img = self.reg_image
        self.image = self.reg_image
        self.x, self.y = pos
        self.rotate = 0
        self.speed = 0
        self.angle = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.object_group = object_group
        self.path = []
        self.player = player
        self.time_shot = 0
        self.make_bullet = 0
        self.show_fire = 0

        self.reload_sound = pygame.mixer.Sound("sounds/reload.mp3")
        self.reload_sound.set_volume(0.2)

    def draw(self):
        if self.show_fire:
            self.reg_image = self.reg_shoot_img
        else:
            self.reg_image = self.reg_not_shoot_img
        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.move()

        keys = pygame.key.get_pressed()  # list of pressed keys
        if self.player == 1:
            if keys[pygame.K_LEFT]:
                self.angle += 1.4
                self.turn(1.4)
            elif keys[pygame.K_RIGHT]:
                self.angle -= 1.4
                self.turn(-1.4)
        else:
            if keys[pygame.K_a]:
                self.angle += 1.4
                self.turn(1.4)
            elif keys[pygame.K_d]:
                self.angle -= 1.4
                self.turn(-1.4)

        self.rect.centerx = self.x
        self.rect.centery = self.y

        if pygame.time.get_ticks() - self.time_shot > 3000 and self.make_bullet == 0: # every 3 seconds the enemy tank can shoot
            self.show_fire = 1
            self.reload_sound.play()
            self.make_bullet = 1 # creates bullet that can hit the player


    def turn(self, turn):
        original_rect = self.rect
        self.angle %= 360
        collided = pygame.sprite.spritecollide(self, self.object_group, False)
        if collided:
            self.rect = original_rect
            self.angle -= turn

    def move(self):
        keys = pygame.key.get_pressed()  # list of pressed keys
        if self.player == 1:
            if keys[pygame.K_UP]:
                self.speed = 3
            elif keys[pygame.K_DOWN]:
                self.speed = -3
            else:
                self.speed = 0
        else:
            if keys[pygame.K_w]:
                self.speed = 3
            elif keys[pygame.K_s]:
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

    def create_bullet(self):
        if self.make_bullet == 1:
            self.make_bullet = 0
            self.show_fire = 0
            self.time_shot = pygame.time.get_ticks()
            return 1
        else:
            return 0

    def check_collide(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.8))
        if collided:
            return 1
        else:
            return 0


