from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ReferenceListProperty, ObjectProperty
)
from kivy.vector import Vector
import operator

class Background(Widget):
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
        self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)

    def scroll_textures(self, time_passed):
        # Update the uvpos of the texture
        self.cloud_texture.uvpos = ( (self.cloud_texture.uvpos[0] +
            time_passed/2.0)%Window.width , self.cloud_texture.uvpos[1])
        # Redraw the texture
        texture = self.property('cloud_texture')
        texture.dispatch(self)

class BrickBreakApp(App):

    def next_frame(self, time_passed):
        ball = self.root.ids.ball
        paddle = self.root.ids.whitepaddle
        self.root.ids.background.scroll_textures(time_passed)
        ball.move()
        ball.check_ball_collision(paddle)

    def start_game(self):
        self.root.ids.score.text = "0"
        self.frames = Clock.schedule_interval(self.next_frame, 1/60.)

#         # bounce off paddles
#         self.whitepaddle.bounce_ball(self.ball)


class Ball(Image):
    """
    ball properties and movement
    """
    velocity_x = 0
    velocity_y = 3

    def move(self):
        self.pos = (self.pos[0] + self.velocity_x, self.pos[1] + self.velocity_y)

    def serve_ball(self, vel=(1,3)):
        self.pos = (0,0)
        self.velocity_x = vel[0]
        self.velocity_y = vel[1]

    def check_ball_collision(self, target):
        # bounce ball off sides
        if (self.pos[0] < -Window.size[0]/2) or (self.pos[0] > Window.size[0]/2):
            self.velocity_x = -self.velocity_x

       # bounce ball off top
        if self.pos[1] > Window.size[1]/2:
            self.velocity_y = -self.velocity_y

        # went off bottom
        if self.pos[1] < -Window.size[1]/2:
            self.serve_ball(vel=(1, 3))

        # hit paddle
        if self.colliding(target):
            self.velocity_x *= 1.5
            self.velocity_y = -self.velocity_y * 1.5

    def colliding(self, target):

        if ((self.pos[0] > target.pos[0] or target.pos[0] > self.pos[0]) and self.pos[1] != -400):
            return False

        return True

class WhitePaddle(Image):
    """
    white paddle properties - most reflective
    """

    def on_touch_move(self, touch):
        if touch.x < Window.width / 2:
            self.center_x = touch.x
        if touch.x > Window.width / 2:
            self.center_x = touch.x


if __name__ == '__main__':
    BrickBreakApp().run()
