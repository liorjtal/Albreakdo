from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.screenmanager import WipeTransition
from buttons import AboutButton
from paddle import Paddle
from ball import Ball
from screens import (
    Manager, Control, About, ElectroMagneticSpectrum, Sun, Albedo, Colors, Gasses
)

class Game(Widget):
    """
    add docstring
    """
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    canvasOpacity = NumericProperty(0)

    #logic/assets inspired by https://github.com/Dirk-Sandberg/2DKivyGame.git
    cloud_texture = ObjectProperty(None)
    sun_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Game,self).__init__(**kwargs)

        # Create textures
        self.cloud_texture = Image(source="cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (
            Window.width / self.cloud_texture.width, -1
            )
        self.sun_texture = Image(source="sun.png").texture
        self.sun_texture.uvsize = (Window.width / self.sun_texture.width, -1)

        button_size = (Window.width/5, Window.height/8)
        self.restart_button = Button(
            pos = (Window.width*0.4, self.center_y + self.height * 2.5),
            size = button_size, text='Try Again',
            on_release=self.restart
        )
        self.menu_button = Button(
            pos = (Window.width*0.4, self.center_y + self.height * 1.5),
            size = button_size, text='Back to Main Menu',
            on_release=self.change_screen
        )

    def on_touch_move(self, touch):
        """
        add docstring
        """
        if touch.x < self.width / 2:
            self.player1.center_x = touch.x
        if touch.x > self.width - self.width / 2:
            self.player1.center_x = touch.x

    def on_size(self, *args):
        """
        add docstring
        """
        self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)

    def serve_ball(self, vel=(2, -5)):
        """
        add docstring
        """
        #make ball (ray) come from sun's position
        self.ball.center = (0.25 * self.center_x, self.center_y + self.center_y/2) 
        self.ball.velocity = vel
        self.ball.ballR = 255
        self.ball.ballG = 0
        self.ball.ballB = 0

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

        #make timer slower or faster based on time left
        #activate a canvas on the screen which makes it redder at each mark
        if(self.player1.timer >= 80):
            self.canvasOpacity = 0
            self.player1.timer -= 2 * 0.01
        elif(self.player1.timer >= 50 and self.player1.timer < 80):
            self.player1.timer -= 4 * 0.01
            self.canvasOpacity = 0.2
        elif(self.player1.timer >= 20 and self.player1.timer < 50):
            self.player1.timer -= 6 * 0.01
            self.canvasOpacity = 0.4
        elif(self.player1.timer > 0 and self.player1.timer < 20):
            if self.player1.timer < 6 * 0.01:
                self.player1.timer = 0
                self.game_over()
            else:
                self.player1.timer -= 6 * 0.01
                self.canvasOpacity = 0.6
        elif(self.player1.timer <= 0):
            self.canvasOpacity = 1
            self.player1.timer = 0
            self.game_over()

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
            self.serve_ball()

    def play(self):
        self.reset()
        self.serve_ball()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def game_over(self):
        self.remove_widget(self.restart_button)
        self.remove_widget(self.menu_button)
        self.add_widget(self.restart_button)
        self.add_widget(self.menu_button)

    def restart(self, instance):
        self.reset()
        self.play()

    def change_screen(self, instance):
        sm = self.parent.parent
        sm.current = 'home'

    def reset(self):
        self.remove_widget(self.restart_button)
        self.remove_widget(self.menu_button)
        Clock.unschedule(self.update)
        self.player1.timer = self.player1.DURATION

class BrickBreakApp(App):
    """
    add docstring
    """

    def build(self):
        """
        add docstring
        """
        return Manager(transition=WipeTransition())

if __name__ == '__main__':
    BrickBreakApp().run()
