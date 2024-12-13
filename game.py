import arcade
import arcade.key
import constants
from tank import Tank  

class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("background.png")
        self.tank = Tank()
        self.bullets = arcade.SpriteList()

    def setup(self):
        pass

    def on_draw(self):
        self.clear((255, 255, 255))
        arcade.draw_texture_rectangle(
            constants.SCREEN_WIDTH / 2,
            constants.SCREEN_HEIGHT / 2,
            constants.SCREEN_WIDTH,
            constants.SCREEN_HEIGHT,
            self.bg,
        )
        self.tank.draw()
        self.bullets.draw()

    def update(self, delta_time):
        self.tank.update()
        self.bullets.update()

    def on_key_press(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.moving_forward = True
        if symbol == arcade.key.DOWN:
            self.tank.moving_backward = True
        if symbol == arcade.key.LEFT:
            self.tank.rotating_left = True
        if symbol == arcade.key.RIGHT:
            self.tank.rotating_right = True
        if symbol == arcade.key.SPACE:
            bullet = self.tank.shoot()
            if bullet:
                self.bullets.append(bullet)

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.UP:
            self.tank.moving_forward = False
        if symbol == arcade.key.DOWN:
            self.tank.moving_backward = False
        if symbol == arcade.key.LEFT:
            self.tank.rotating_left = False
        if symbol == arcade.key.RIGHT:
            self.tank.rotating_right = False



window = Game(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
window.setup()
arcade.run()
