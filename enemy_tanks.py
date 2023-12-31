import pygame
from bullets import Bullets
import math
from pathfinding import path
from check_shoot import check_shoot

class enemy_tank(pygame.sprite.Sprite):

    def __init__(self, screen, pos, player_tank, object_group, level, dif):
        super().__init__()
        self.screen = screen
        self.level = level
        self.x, self.y = pos
        self.reg_image = pygame.image.load('images/tank_sand.png')
        self.reg_image = pygame.transform.scale(self.reg_image, (40, 40))
        self.reg_shoot_image = pygame.image.load('images/tank_sand_shoot.png')
        self.reg_shoot_image = pygame.transform.scale(self.reg_shoot_image, (40, 40))
        self.reg_not_shoot_image = self.reg_image
        self.image = self.reg_image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.angle = 0
        self.speed = dif[0]
        self.turn_speed = dif[1]
        self.shoot_speed = dif[2]
        self.player_tank = player_tank
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player_tank)
        self.object_group = object_group
        self.time_shot = 0
        self.time_turn = 0
        self.make_bullet = 0
        self.time_calc = 0
        self.calc_angle = 0
        self.path = []
        self.last_player_pos = (0, 0)
        self.check_shoot_obj = 0
        self.check_shoot_time = 0
        self.face_player = 0
        self.get_new_path = 1
        self.show_fire = 0

    def draw(self):
        if self.show_fire:
            self.reg_image = self.reg_shoot_image
        else:
            self.reg_image = self.reg_not_shoot_image
        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.rect)

        '''
        try:
            if len(self.path) > 2:
                for x in self.path:
                    image = pygame.image.load("images/green_circle.png")
                    new_rect = image.get_rect()
                    new_rect.centerx = x[0] + 32
                    new_rect.centery = x[1] + 32
                    self.screen.blit(image, new_rect)
        except:
            print("error")
        '''


    def update(self):
        self.turn_path_bearing()
        self.check_shoot()
        self.check_distance_to_point()
        if self.face_player:
            self.turn()
        else:
            if abs(self.angle - self.calc_angle)%360 < 3 or abs(self.angle - self.calc_angle)%360 > 357:
                self.move()
            else:
                self.turn_path()

        if self.level < 12:
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed and self.face_player: # every 3 seconds the enemy tank can shoot
                if abs(self.angle - self.player_angle()) < 30 or abs(self.angle - self.player_angle()) > 330:
                    self.show_fire = 1
                    self.make_bullet = 1 # creates bullet that can hit the player
                    self.time_shot = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed: # every 3 seconds the enemy tank can shoot
                self.show_fire = 1
        else:
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed: # every 3 seconds the enemy tank can shoot
                self.show_fire = 1
                self.make_bullet = 1 # creates bullet that can hit the player
                self.time_shot = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed: # every 3 seconds the enemy tank can shoot
                self.show_fire = 1


    def create_bullet(self):
        if self.make_bullet == 1:
            self.make_bullet = 0
            self.show_fire = 0
            return 1
        else:
            return 0


    def player_angle(self):
        player_x = self.player_tank.x
        player_y = self.player_tank.y
        rel_x = player_x - self.x
        rel_y = player_y - self.y
        return -math.atan2(rel_y, rel_x) * 180 / math.pi + 90

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return self.get_distance(coord1, coord2)

    def move(self):
        self.x += self.speed * math.cos(math.pi / 2 - self.angle * math.pi / 180)
        self.y += self.speed * math.sin(math.pi / 2 - self.angle * math.pi / 180)
        self.rect.center = self.x, self.y


    def turn_path_bearing(self):
        if pygame.time.get_ticks() - self.time_calc > 500 and self.get_new_path or self.time_calc == 0:
            move_path = path(self.player_tank.rect.center, self.rect.center, self.level, self.last_player_pos, self.path)
            self.last_player_pos = self.player_tank.rect.center
            self.path = move_path[:]
            try:
                if len(self.path) > 0:
                    next_x = self.path[0][0] + 32
                    next_y = self.path[0][1] + 32
                    rel_x = next_x - self.x
                    rel_y = next_y - self.y
                    self.time_calc = pygame.time.get_ticks()
                    self.calc_angle = -math.atan2(rel_y, rel_x) * 180 / math.pi + 90
            except:
                print(move_path)


    def turn_path(self):
        self.turn_path_bearing()
        angle_diff = (self.calc_angle - self.angle + 180) % 360 - 180
        if angle_diff >= 0: # find if it needs to turn left or right
            direction = 1
        else:
            direction = -1
        self.angle += 3 * direction # change angle
        self.angle %= 360 # keeps it within 0-360
        self.time_shot -= 100


    def turn(self):
        angle_diff = (self.player_angle() - self.angle + 180) % 360 - 180 # find the angle to face the player
        if angle_diff >= 0: # find if it needs to turn left or right
            direction = 1
        else:
            direction = -1
        self.angle += self.turn_speed * direction # change angle
        self.angle %= 360 # keeps it within 0-360


    def check_collide(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.7))
        if collided:
            return 1
        else:
            return 0


    def check_shoot(self):
        if (pygame.time.get_ticks() - self.check_shoot_time) > 500 or self.check_shoot_time == 0:
            self.check_shoot_obj = check_shoot(self.screen, self.rect.center, self.player_tank, self.object_group)
            self.check_shoot_time = pygame.time.get_ticks()
        self.check_shoot_obj.update()
        if self.check_shoot_obj.check_for_hit == 1:
            if self.check_shoot_obj.check_hit() == 1:
                self.face_player = 1
        else:
            self.face_player = 0

    def check_distance_to_point(self):
        try:
            if self.get_distance((self.path[0][0] + 32, self.path[0][1] + 32), (self.x, self.y)) < 10:
                self.get_new_path = 1
            else:
                self.get_new_path = 0
        except:
            print("error check distance to point")

class st_enemy_tank(pygame.sprite.Sprite):

    def __init__(self, screen, pos, player_tank, object_group, level, dif):
        super().__init__()
        self.screen = screen
        self.level = level
        self.x, self.y = pos
        self.player_tank = player_tank
        self.object_group = object_group
        self.dif = dif
        self.angle = self.player_angle()
        self.speed = dif[0]
        self.turn_speed = dif[1]
        self.shoot_speed = dif[2]
        self.reg_image = pygame.image.load('images/tank_sand.png')
        self.reg_image = pygame.transform.scale(self.reg_image, (40, 40))
        self.reg_shoot_image = pygame.image.load('images/tank_sand_shoot.png')
        self.reg_shoot_image = pygame.transform.scale(self.reg_shoot_image, (40, 40))
        self.reg_not_shoot_image = self.reg_image
        self.image = self.reg_image
        self.rect = self.image.get_rect()
        self.rect.centerx = self.x
        self.rect.centery = self.y
        self.check_shoot_time = 0
        self.check_shoot_obj = 0
        self.shoot = 0
        self.make_bullet = 0
        self.show_fire = 0
        self.time_shot = 0

    def draw(self):
        if self.show_fire: # if it can fire put a red dot on it
            self.reg_image = self.reg_shoot_image
        else:
            self.reg_image = self.reg_not_shoot_image
        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.check_shoot() # check to see if the enemy is able to shoot
        if self.shoot: # if it can "see" the player then turn
            self.turn()

        if self.level < 12:
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed:  # see if enough time has passed to shoot
                if abs(self.angle - self.player_angle())%360 < 5 or abs(self.angle - self.player_angle())%360 > 355: # see if player is in FOV
                    if self.shoot: # if it can shoot
                        self.show_fire = 1
                        self.make_bullet = 1  # creates bullet that can hit the player
                        self.time_shot = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed:  # every 3 seconds the enemy tank can shoot
                self.show_fire = 1
        else: # if level 12, let the enemy shoot whenever
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed:  # every 3 seconds the enemy tank can shoot
                self.show_fire = 1
                self.make_bullet = 1  # creates bullet that can hit the player
                self.time_shot = pygame.time.get_ticks()
            if pygame.time.get_ticks() - self.time_shot > self.shoot_speed:  # every 3 seconds the enemy tank can shoot
                self.show_fire = 1

    def create_bullet(self): # to be called outside of class
        if self.make_bullet == 1:
            self.make_bullet = 0
            self.show_fire = 0
            return 1
        else:
            return 0

    def player_angle(self):
        player_x = self.player_tank.x
        player_y = self.player_tank.y
        rel_x = player_x - self.x
        rel_y = player_y - self.y
        return -math.atan2(rel_y, rel_x) * 180 / math.pi + 90

    def get_distance(self, coord1, coord2):
        x1, y1 = coord1
        x2, y2 = coord2
        return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

    def get_sprite_distance(self, sprite1, sprite2):
        coord1 = sprite1.rect.center
        coord2 = sprite2.rect.center
        return self.get_distance(coord1, coord2)


    def turn(self):
        angle_diff = (self.player_angle() - self.angle + 180) % 360 - 180  # find the angle to face the player
        if angle_diff >= 0:  # find if it needs to turn left or right
            direction = 1
        else:
            direction = -1
        self.angle += self.turn_speed * direction  # change angle
        self.angle %= 360  # keeps it within 0-360

    def check_shoot(self):
        if (pygame.time.get_ticks() - self.check_shoot_time) > 500 or self.check_shoot_time == 0: # every half a second send out an object to see if it can hit the player, if it can let the enemy turn and shoot
            self.check_shoot_obj = check_shoot(self.screen, self.rect.center, self.player_tank, self.object_group)
            self.check_shoot_time = pygame.time.get_ticks()
        self.check_shoot_obj.update()
        if self.check_shoot_obj.check_for_hit == 1:
            if self.check_shoot_obj.check_hit() == 1:
                self.shoot = 1
        else:
            self.shoot = 0




