import arcade
from random import  randint
from math import sin, cos, radians

SCREEN_WIDTH = 1920
SCREEN_HEIGHT = 1080





img_space_suttle = arcade.load_texture('img/rokets.png')

def get_distanse(ob1, ob2):
    dx = ob2.x - ob1.x
    dy = ob2.y - ob1.y

    return (dx ** 2 + dy ** 2) ** 0.5

class Apple:
    def __init__(self):
        self.size = randint(5,30)
        self.x = randint(self.size, SCREEN_WIDTH - self.size)
        self.y = randint(self.size, SCREEN_HEIGHT - self.size)
        self.color = arcade.color.BLUE

    def draw(self):
        arcade.draw_circle_filled(self.x, self.y, self.size, self.color)

    def is_collision(self, hero):
        r = get_distanse(self, hero)
        r2 = self.size / 2 + hero.size
        return r2 >= r



class Hero:
    def __init__(self):
        self.x = 1850
        self.y = 950
        self.dir = 0
        self.speed = 2
        self.speed_rotation = 0
        self.size = 60

        self.color = arcade.color.HEART_GOLD

    def draw(self):
        arcade.draw_texture_rectangle(self.x, self.y,
                                      self.size * 0.8, self.size * 1.5,
                                      img_space_suttle, - self.dir)
        # dx = 80 * sin(radians(self.dir))
        # dy = 80 * cos(radians(self.dir))
        # arcade.draw_circle_filled(self.x, self.y, self.size, self.color)
        # arcade.draw_line(self.x, self.y, self.x + 0.3 * dx, self.y + 0.3 * dy, [255, 255, 255], 4)

    def speed_up(self):
        if self.speed < 3:
            self.speed += 1

    def rotation_left(self):
        self.speed_rotation = -3

    def rotation_right(self):
        self.speed_rotation = 3

    def rotation_stop(self):
        self.speed_rotation = 0

    def speed_down(self):
        if self.speed > -3:
            self.speed -= 1

    def turn_left(self):
        self.dir -= 10

    def turn_right(self):
        self.dir += 10

    def move(self):
        self.dir += self.speed_rotation
        dx = self.speed * sin(radians(self.dir))
        dy = self.speed * cos(radians(self.dir))
        self.x += dx
        self.y += dy



pass


class MyGame(arcade.Window):
    """ Главный класс приложения. """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.BLACK)


    def setup(self):
        # Настроить игру здесь
        self.hero = Hero()
        self.apple_list = []
        self.state = 'run'
        for i in range(randint(20, 20)):
            self.apple_list.append(Apple())
        pass

    def on_draw(self):
        """ Отрендерить этот экран. """
        arcade.start_render()
        # Здесь код рисунка
        if self.state == 'run':
            self.hero.draw()
            for apple in self.apple_list:
                apple.draw()
        elif self.state == 'pause':
            pass
        elif self.state == 'game_over':
            self.hero.draw()
            for apple in self.apple_list:
                apple.draw()
            arcade.draw_text('Иди учись в АЭРО!!!', 500, 500, [200, 200, 200], 100)

    def update(self, delta_time):
        """ Здесь вся игровая логика и логика перемещения."""
        if self.state == 'run':
            self.hero.move('')
            for apple in self.apple_list:
                if apple.is_collision(self.hero):
                    self.state = 'game_over'

                # arcade.draw_text('Иди в АЭРО!!!', 122, 400, [200, 200, 200], 25, 300)

        pass

    def on_key_press(self, symbol: int, modifiers: int):
        if self.state == 'run':
            if symbol == arcade.key.LEFT:
                self.hero.move()
                self.hero.rotation_left()
            elif symbol == arcade.key.RIGHT:
                self.hero.rotation_right()
                self.hero.move()
            elif symbol == arcade.key.UP:
                self.hero.speed_up()
            elif symbol == arcade.key.DOWN:
                self.hero.speed_down()

    def on_key_release(self, symbol: int, modifiers: int):
        if self.state == 'run':
            if symbol == arcade.key.LEFT:
                self.hero.rotation_stop()
            elif symbol == arcade.key.RIGHT:
                self.hero.rotation_stop()

def main():
    global IN_GAME
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    game.setup()
    arcade.run()
    #arcade.schedule(on_draw, 1 / 80)


if __name__ == "__main__":
    main()





