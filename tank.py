import arcade
import math
import constants

class Tank(arcade.Sprite):
    def __init__(self,window):
        super().__init__("green.png", 0.15)
        self.center_x = 500
        self.center_y = 300
        self.angle = 0  
        self.speed = 2
        self.health = 100
        self.rotation_speed = 2 
        self.moving_forward = False
        self.moving_backward = False
        self.rotating_left = False
        self.rotating_right = False
        self.window = window

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
        hit_list = arcade.check_for_collision_with_list(self,self.window.bullets)
        if hit_list:
            for bullet in hit_list:
                if bullet.is_friendly == False:
                    self.health -= bullet.damage
                    bullet.kill()
        if self.health <= 0:
            self.health = 0
            self.texture = arcade.load_texture("green_broken.png")
            self.speed = 0
            self.rotation_speed = 0

    def shoot(self):
        self.damage = 25
        bullet = Bullet(self.center_x, self.center_y, self.angle)
        return bullet
    
    def draw(self):
        super().draw()
        arcade.draw_text(f"HP: {self.health}", self.center_x - 35, self.center_y + 30, arcade.color.BLACK, 20)


class Enemy_tank(arcade.Sprite):
    def __init__(self,enemy_center_x,enemy_center_y,window):
        super().__init__("red.png",0.15)
        self.speed = 2
        self.angle = 180
        self.health = 100
        self.center_x = enemy_center_x
        self.center_y = enemy_center_y
        self.window = window
    def draw(self):
        super().draw()
        arcade.draw_text(f"HP: {self.health}", self.center_x - 35, self.center_y + 30, arcade.color.BLACK, 20)
    def update(self):
        hit_list = arcade.check_for_collision_with_list(self,self.window.bullets)
        if hit_list:
            for bullet in hit_list:
                if bullet.is_friendly == True:
                    self.health -= bullet.damage
                    bullet.kill()
                    print(self.health)
        if self.health <= 0:
            self.health = 0
            self.texture = arcade.load_texture("red_broken.png")

class Bullet(arcade.Sprite):
    def __init__(self, x, y, angle,is_friendly=True):
        super().__init__("green_bullet.png", 0.1)
        self.center_x = x
        self.center_y = y
        self.angle = angle
        self.speed = 5
        self.damage = 25
        self.is_friendly = is_friendly
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