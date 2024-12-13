import arcade
import math
import constants

class Tank(arcade.Sprite):
    def __init__(self):
        super().__init__("green.png", 0.15)
        self.center_x = 500
        self.center_y = 300
        self.angle = 0  
        self.speed = 2 
        self.rotation_speed = 2 
        self.moving_forward = False
        self.moving_backward = False
        self.rotating_left = False
        self.rotating_right = False

    def update(self):
        if self.rotating_left:
            self.angle += self.rotation_speed
        if self.rotating_right:
            self.angle -= self.rotation_speed
        radians = math.radians(self.angle)
        if self.moving_forward:
            self.center_x += math.cos(radians) * self.speed
            self.center_y += math.sin(radians) * self.speed
        if self.moving_backward:
            self.center_x -= math.cos(radians) * self.speed
            self.center_y -= math.sin(radians) * self.speed

    def shoot(self):
        bullet = Bullet(self.center_x, self.center_y, self.angle)
        return bullet


class Bullet(arcade.Sprite):
    def __init__(self, x, y, angle):
        super().__init__("green_bullet.png", 0.1)
        self.center_x = x
        self.center_y = y
        self.angle = angle
        self.speed = 5
        radians = math.radians(self.angle)
        self.change_x = math.cos(radians) * self.speed
        self.change_y = math.sin(radians) * self.speed

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y
        if (
            self.center_x < 0
            or self.center_x > constants.SCREEN_WIDTH
            or self.center_y < 0
            or self.center_y > constants.SCREEN_HEIGHT
        ):
            self.kill()