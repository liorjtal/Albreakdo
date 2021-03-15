from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector


class Paddle(Widget):
    """
    add docstring
    """

#   I think you need to define an __init__ function here?
    def __init__(self):
        pass  # what do you want this Class to automatically do when it's initialized?

    score = NumericProperty(0)

    def bounce_ball(self, ball):
        """
        add docstring
        """
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            bounced = Vector(vx, vy * -1)
            vel = bounced * 1.5
            ball.velocity = vel.x, vel.y

    def change_color(self, button):
        """
        TODO: allow user to manually change paddle color by pressing a button
        """
#       see here for changing paddle color (https://stackoverflow.com/questions/12997545/how-do-i-change-the-color-of-my-widget-in-kivy-at-run-time)
#       I added a line in your `brickbreak.kv` file to start working with paddle color
#       r = NumericProperty(0)

    def paddle_shrink(self):
        """
        TODO: decrease paddle size as time of play or number of missed balls increases
        """


class Ball(Widget):
    """
    add docstring
    """
    def __init__(self):
        pass

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        add docstring
        """
        self.pos = Vector(*self.velocity) + self.pos
#       I think that this line of code can go within __init__ function instead


class Game(Widget):
    """
    add docstring
    """
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)

    #logic/assets inspired by https://github.com/Dirk-Sandberg/2DKivyGame.git
    cloud_texture = ObjectProperty(None)
    sun_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Create textures
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (
            Window.width / self.cloud_texture.width, -1
            )
        self.sun_texture = Image(source="sun.png").texture
        self.sun_texture.uvsize = (Window.width / self.sun_texture.width, -1)

    def on_size(self, *args):
        """
        add docstring
        """
        self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)

    def serve_ball(self, vel=(3, 3)):
        """
        add docstring
        """
        self.ball.center = self.center
        self.ball.velocity = vel

    def update(self, dt):
        """
        add docstring
        """

        # Update the uvpos of the texture
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] +
            dt/2.0) % Window.width, self.cloud_texture.uvpos[1])
        # Redraw the texture
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        self.ball.move()

        # bounce off paddles
        self.player1.bounce_ball(self.ball)

        # bounce ball off top
        if self.ball.top > self.top:
            self.ball.velocity_y *= -1

        # bounce off sides
        if self.ball.x < self.x:
            self.ball.velocity_x *= -1
        if self.ball.x > self.width:
            self.ball.velocity_x *= -1

        # went off bottom
        if self.ball.y < self.y:
            self.player1.score += 1
            self.serve_ball(vel=(3, 3))

    def on_touch_move(self, touch):
        """
        add docstring
        """
        if touch.x < self.width / 2:
            self.player1.center_x = touch.x
        if touch.x > self.width - self.width / 2:
            self.player1.center_x = touch.x


class BrickBreakApp(App):
    """
    add docstring
    """

    def __init__(self):
        pass  # do you need an __init__ function, or does the `build` function below serve the same purpose?

    def build(self):
        """
        add docstring
        """
        game = Game()
        game.serve_ball()
        Clock.schedule_interval(game.update, 1.0 / 60.0)
        return game


if __name__ == '__main__':
    BrickBreakApp().run()
