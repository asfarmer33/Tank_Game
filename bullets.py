import pygame
import math

class Bullets(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, angle, enemy_group, object_group, player_group, bullet_group, enemy_bullet, tank):
        super().__init__()
        self.screen = screen
        self.x = x
        self.y = y
        self.angle = angle
        self.tank = tank
        if self.tank == 1:
            self.reg_image = pygame.image.load('images/blue_bullet.png')
        elif self.tank == 2:
            self.reg_image = pygame.image.load('images/green_bullet.png')
        elif self.tank == 3:
            self.reg_image = pygame.image.load('images/sand_bullet.png')
        self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
        self.bounce = 0
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.enemy_group = enemy_group
        self.object_group = object_group
        self.player_group = player_group
        self.bullet_group = bullet_group
        self.collision_radius = self.reg_image.get_height() * 2
        self.enemy_bullet = enemy_bullet
        self.time_alive = pygame.time.get_ticks()

        self.dis_exp_sound = pygame.mixer.Sound("sounds/dist_expl.mp3")
        self.exp_sound = pygame.mixer.Sound("sounds/expl.mp3")
        self.exp_sound.set_volume(0.1)
        self.bounce_sound = pygame.mixer.Sound("sounds/bounce.mp3")

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.enemy_bullet: # if bullet comes from a player it moves faster
            self.x += 8 * math.cos(math.pi/2 - self.angle*math.pi/180) # x direction
            self.y += 8 * math.sin(math.pi / 2 - self.angle * math.pi / 180) # y direction
        else:
            self.x += 5 * math.cos(math.pi / 2 - self.angle * math.pi / 180)  # x direction
            self.y += 5 * math.sin(math.pi / 2 - self.angle * math.pi / 180)  # y direction
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.bouncing() # check bounce
        self.hit_enemy() # check hit enemy


    def bouncing(self):
        if self.bounce >= 2: # if it bounced more than once kill it
            self.kill()
            self.dis_exp_sound.play()
        if self.bounce < 2: # allow it to bounce only once
            if self.x + self.image.get_width()/2 > self.screen.get_width() or self.x - self.image.get_width()/2 < 0: # check boundaries of screen
                self.angle *= -1 # swaps angle
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
                if self.bounce == 1:
                    self.bounce_sound.play()
            if self.y + self.image.get_height()/2 > self.screen.get_height() or self.y - self.image.get_height()/2 < 0:
                self.angle = self.angle * -1 + 180 # swaps angle and then flips it
                self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                self.bounce += 1
                if self.bounce == 1:
                    self.bounce_sound.play()


            for object in self.object_group: # checking all objects on the screen
                hit_factor = 0.95
                if self.rect.colliderect(object): # checking if the bullet collided with the object
                    if self.rect.centerx > object.rect.centerx + object.get_width()/2 * hit_factor or self.rect.centerx < object.rect.centerx - object.get_width()/2 * hit_factor: # checking to see if it hit the left or right of the box
                        self.angle *= -1
                        self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                        self.bounce += 1
                        if self.bounce == 1:
                            self.bounce_sound.play()
                    elif self.rect.centery > object.rect.centery + object.get_height()/2 * hit_factor or self.rect.centery < object.rect.centery - object.get_height()/2 * hit_factor: # else it hit the top of the box
                        self.angle = self.angle * -1 + 180  # swaps angle and then flips it
                        self.image = pygame.transform.rotate(self.reg_image, self.angle + 180)
                        self.bounce += 1
                        if self.bounce == 1:
                            self.bounce_sound.play()

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2

        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return (self.get_distance(coord1, coord2) < self.collision_radius)

    def hit_enemy(self):
        hit_enemy_list = pygame.sprite.spritecollide(self, self.enemy_group, False, collided=self.get_sprite_distance) # checks if bullet hit enemy
        if hit_enemy_list:
            if self.enemy_bullet == 1: # if it was shot by a player kill the enemy
                for enemy in hit_enemy_list:
                    enemy.kill()
                self.kill()
                self.exp_sound.play()

        hit_enemy_list = pygame.sprite.spritecollide(self, self.player_group, False, collided=self.get_sprite_distance) # checks if bullet hit player
        if pygame.time.get_ticks() - self.time_alive > 200:
            if hit_enemy_list:
                if self.enemy_bullet == 1: # if it was shot by a player kill the player
                    for player in hit_enemy_list:
                        player.kill()
                    self.kill()
                    self.exp_sound.play()

        hit_enemy_list = pygame.sprite.spritecollide(self, self.player_group, False, collided=self.get_sprite_distance) # checks if bullet hit player
        if hit_enemy_list:
            if self.enemy_bullet == 0:
                for player in hit_enemy_list: # if it was shot by an enemy kill the player
                    player.kill()
                self.kill()
                self.exp_sound.play()

        hit_enemy_list = pygame.sprite.spritecollide(self, self.bullet_group, False, pygame.sprite.collide_rect_ratio(0.7)) # checks if bullet hit object
        if hit_enemy_list:
            for bullet in hit_enemy_list:
                if bullet is not self:
                    bullet.kill()
                    self.kill()
                    self.dis_exp_sound.play()

