import pygame
from bullets import Bullets
import math

class enemy_tank(pygame.sprite.Sprite):

    def __init__(self, screen, x, y, player_tank, object_group):
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
        self.turn_speed = 0.5
        self.player_tank = player_tank
        self.player_group = pygame.sprite.Group()
        self.player_group.add(player_tank)
        self.object_group = object_group
        self.time_shot = 0
        self.time_turn = 0
        self.path = []
        self.make_bullet = 0
        self.collided_count = 0
        self.count_move_collide = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.collided_count <= 20:
            self.move()
            self.turn()
        else:
            self.move_collide()

        if pygame.time.get_ticks() - self.time_shot > 3000 and abs(self.angle - self.player_angle()) < 50: # every 3 seconds the enemy tank can shoot and if it is looking at the player
            self.make_bullet = 1 # creates bullet that can hit the player
            self.time_shot = pygame.time.get_ticks()

    def create_bullet(self):
        if self.make_bullet == 1:
            self.make_bullet = 0
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
        if self.get_sprite_distance(self, self.player_tank) < 600 and self.get_sprite_distance(self, self.player_tank) > 200 or abs(self.player_angle() - self.angle) <= 1 or abs(self.player_angle() - self.angle) >= 359:
            self.x += 1 * math.cos(math.pi/2 - self.angle*math.pi/180)
            self.y += 1 * math.sin(math.pi/2 - self.angle*math.pi/180)
            self.turn_speed = 1.4
        else:
            self.turn_speed = 0.5

        self.path.append(self.rect.center)  # adds position to list
        self.path = self.path[-2:]  # list of last two positions
        if self.check_collide():
            self.x, self.y = self.path[0] # move back to position two times ago

    def turn(self):
        original_rect = self.rect
        angle_diff = (self.player_angle() - self.angle + 180) % 360 - 180 # find the angle to face the player
        if angle_diff >= 0: # find if it needs to turn left or right
            direction = 1
        else:
            direction = -1
        self.angle += self.turn_speed * direction # change angle
        if self.check_collide(): # if it collides with an object while turning, do not turn
            self.angle -= self.turn_speed * direction
        self.angle %= 360 # keeps it within 0-360

        self.image = pygame.transform.rotate(self.reg_image, self.angle)
        self.rect = self.image.get_rect(center=(self.x, self.y))

    def move_collide(self):
        print(self.count_move_collide)

        if self.count_move_collide < 30:
            self.x -= 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180) # if collided move back
            self.y -= 1 * math.sin(math.pi / 2 - self.angle * math.pi / 180)

            self.path.append(self.rect.center)  # adds position to list
            self.path = self.path[-2:]  # list of last two positions
            if self.check_collide() and self.count_move_collide > 10:
                self.x, self.y = self.path[0]  # move back to position two times ago

            self.rect.center = self.x, self.y
            self.angle += self.turn_speed # turn left while moving back

            if self.check_collide(): # if it turns into an object don't turn
                self.angle -= self.turn_speed

            self.rect.center = self.x, self.y
            self.angle %= 360

            self.image = pygame.transform.rotate(self.reg_image, self.angle) # redraw image
            self.rect = self.image.get_rect(center=(self.x, self.y))
            self.count_move_collide += 1
            self.collided_count = 40
        elif self.count_move_collide < 100: # move forward a little after turning and moving back
            self.x += 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180)
            self.y += 1 * math.sin(math.pi / 2 - self.angle * math.pi / 180)
            self.path.append(self.rect.center)  # adds position to list
            self.path = self.path[-2:]  # list of last two positions
            if self.check_collide():
                self.x, self.y = self.path[0]  # move back to position two times ago
                self.collided_count = 100
            self.rect.center = self.x, self.y
            self.count_move_collide += 1
            self.collided_count = 40
        else:
            self.count_move_collide = 0
            self.collided_count = 0


    def check_collide(self):
        collided = pygame.sprite.spritecollide(self, self.object_group, False, pygame.sprite.collide_rect_ratio(0.9))
        if collided:
            self.collided_count += 1
            return 1

        check_boundaries = 0
        if (self.x - self.rect.width / 2) > 0 and (self.x + self.rect.width / 2) < self.screen.get_width():
            check_boundaries = 0
        else:
            self.turn_360()
            return 1

        if (self.y - self.rect.height / 2) > 0 and (self.y + self.rect.height / 2) < self.screen.get_height():
            check_boundaries = 0
        else:

            self.turn_360()
            return 1

        return 0

    def turn_360(self):
        self.x += 1 * math.cos(math.pi / 2 - self.angle * math.pi / 180)
        self.y += 1 * math.sin(math.pi / 2 - self.angle * math.pi / 180)
        self.angle += self.turn_speed  # change angle
        if self.check_collide():  # if it collides with an object while turning, do not turn
            self.angle -= self.turn_speed
        self.angle %= 360  # keeps it within 0-360



