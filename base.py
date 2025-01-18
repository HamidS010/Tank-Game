import arcade
class Base(arcade.Sprite):
    def __init__(self,image,scale,center_x,center_y,health):
        super().__init__(image,scale, center_x= center_x,center_y=center_y)
        self.health = health
    def draw(self):
        super().draw()
        arcade.draw_text(f"HP: {self.health}", self.center_x - 35, self.center_y + 130, arcade.color.BLACK, 20)

