from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.clock import Clock
from kivy.properties import (
    NumericProperty, ObjectProperty
)
from kivy.uix.screenmanager import WipeTransition
from kivy.core.audio import SoundLoader
from buttons import AboutButton
from paddle import Paddle
from ball import Ball
from screens import (
    Manager, Control, About, ElectroMagneticSpectrum, Sun, Albedo, Colors, Gasses
)
from bricks import CO2, CH4
import random

class Game(Widget):
    """
    Main game code containing bricks, player paddle, ball, background
    textures, and update function for logic.
    """
    ball = ObjectProperty(None)
    player1 = ObjectProperty(None)
    co2 = ObjectProperty(None)
    ch4 = ObjectProperty(None)
    paused = False

    canvasOpacity = NumericProperty(0)

    #logic/assets inspired by https://github.com/Dirk-Sandberg/2DKivyGame.git
    cloud_texture = ObjectProperty(None)
    sun_texture = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(Game,self).__init__(**kwargs)

        # Create textures
        self.cloud_texture = Image(source="art/cloud.png").texture
        self.cloud_texture.wrap = 'repeat'
        self.cloud_texture.uvsize = (
            Window.width / self.cloud_texture.width, -1
            )
        self.sun_texture = Image(source="art/sun.png").texture
        self.sun_texture.uvsize = (Window.width / self.sun_texture.width, -1)

        button_size = (275, 50)
        self.restart_button = Button(
            pos = (Window.width*0.7, self.center_y + self.height * 4),
            size = button_size, text='Try Again',
            on_release=self.restart
        )
        self.menu_button = Button(
            pos = (Window.width*0.4, self.center_y + self.height * 4),
            size = button_size, text='Back to Main Menu',
            on_release=self.change_screen
        )
        self.resume_button = Button(
            pos = (Window.width*0.1, self.center_y + self.height * 4),
            size = button_size, text='Resume',
            on_release=self.resume
        )

    def on_touch_move(self, touch):
        """
        touch controls for paddle position
        """
        if touch.x < self.width / 2:
            self.player1.center_x = touch.x
        if touch.x > self.width - self.width / 2:
            self.player1.center_x = touch.x

    def on_size(self, *args):
        """
        make clouds approrpiate size for screen
        """
        self.cloud_texture.uvsize = (self.width / self.cloud_texture.width, -1)

    def serve_ball(self, vel=(2, -5)):
        """
        serve ball from sun's location at velocity set by parameter vel
        ball color is random every serve
        """
        #serve a random colored ball from sun's position
        self.ball.center = (0.25 * self.center_x, self.center_y + self.center_y/2)
        self.ball.velocity = vel
        col = random.randint(0, 4)
        self.ball.ballR = self.ball.colors[col][0]
        self.ball.ballG = self.ball.colors[col][1]
        self.ball.ballB = self.ball.colors[col][2]

    def move_co2(self, vel=(4, 0)):
        """
        move co2 brick at velocity set by parameter vel
        """
        self.co2.velocity = vel

    def move_ch4(self, vel=(8, 0)):
        """
        move ch4 brick at velocity set by parameter vel
        """
        self.ch4.velocity = vel

    def update(self, dt):
        """
        update function providing game logic at dt FPS
        """

        # Update the uvpos of the texture
        self.cloud_texture.uvpos = ((self.cloud_texture.uvpos[0] +
            dt/2.0) % Window.width, self.cloud_texture.uvpos[1])
        # Redraw the texture
        texture = self.property('cloud_texture')
        texture.dispatch(self)

        #move ball and bricks
        self.ball.move()
        self.co2.move(dt)
        self.ch4.move(dt)

        #make timer slower or faster based on time left
        #activate a canvas on the screen which makes it redder at each mark
        if self.player1.timer >= 80:
            self.canvasOpacity = 0
            self.player1.timer -= 2 * 0.01
        elif self.player1.timer >= 50 and self.player1.timer < 80:
            self.player1.timer -= 4 * 0.01
            self.canvasOpacity = 0.2
        elif self.player1.timer >= 20 and self.player1.timer < 50:
            self.player1.timer -= 6 * 0.01
            self.canvasOpacity = 0.4
        elif self.player1.timer > 0 and self.player1.timer < 20:
            if self.player1.timer < 6 * 0.01:
                self.player1.timer = 0
                self.game_over()
            else:
                self.player1.timer -= 6 * 0.01
                self.canvasOpacity = 0.6

        if self.player1.radiation <= 0:
            self.win_game()

        # bounce off paddles
        self.player1.bounce_ball(self.ball)

        #bounce off bricks. each collision with ghg removes 5 seconds
        if self.co2.co2_collision(self.ball) == "co2" and self.player1.timer >= 5:
            self.player1.timer -= 5
        if self.ch4.ch4_collision(self.ball) == "ch4" and self.player1.timer >= 5:
            self.player1.timer -= 5

        # remove ball off top. each successfully reflected ball adds 5 seconds
        if self.ball.top > self.top and self.player1.timer > 0:
            self.player1.radiation -= 1
            self.player1.timer += 5
            self.serve_ball()

        # bounce off sides
        if self.ball.x < self.x:
            self.ball.velocity_x *= -1
        if self.ball.x > self.width:
            self.ball.velocity_x *= -1

        #gradually increase brick speed while moving back and forth
        if self.co2.x < self.x:
            self.co2.velocity_x *= -1 * 1.05

        if self.co2.x > self.width:
            self.co2.velocity_x *= -1 * 1.05

        if self.ch4.x < self.x:
            self.ch4.velocity_x *= -1 * 1.05

        if self.ch4.x > self.width:
            self.ch4.velocity_x *= -1 * 1.05

        # went off bottom. each missed ball removes 5 seconds
        if self.ball.y < self.y and self.player1.timer >= 5:
            self.player1.timer -= 5
            self.serve_ball()

    def play(self):
        """
        begins the game and starts update function
        """
        self.reset()
        self.serve_ball()
        self.move_co2()
        self.move_ch4()
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def pause(self):
        """
        stops the update function and brings up menu
        """
        if not self.paused:
            self.paused = True
            Clock.unschedule(self.update)
            self.add_widget(self.resume_button)
            self.add_widget(self.restart_button)
            self.add_widget(self.menu_button)

    def resume(self, instance):
        """
        resumes the update function and removes menu
        """
        self.paused = False
        Clock.schedule_interval(self.update, 1.0 / 60.0)
        self.remove_widget(self.resume_button)
        self.remove_widget(self.restart_button)
        self.remove_widget(self.menu_button)

    def game_over(self):
        """
        stops the update function and brings up menu
        """
        Clock.unschedule(self.update)
        self.remove_widget(self.restart_button)
        self.remove_widget(self.menu_button)
        self.add_widget(self.restart_button)
        self.add_widget(self.menu_button)

    def win_game(self):
        """
        stops the update function and brings up menu
        """
        Clock.unschedule(self.update)
        self.add_widget(self.restart_button)
        self.add_widget(self.menu_button)

    def restart(self, instance):
        """
        resets the update function and plays game
        """
        self.reset()
        self.play()

    def change_screen(self, instance):
        """
        back to main menu
        """
        sm = self.parent.parent
        sm.current = 'home'

    def reset(self):
        """
        resets the update function and removes menu
        """
        self.paused = False
        self.remove_widget(self.resume_button)
        self.remove_widget(self.restart_button)
        self.remove_widget(self.menu_button)
        Clock.unschedule(self.update)
        self.player1.timer = self.player1.DURATION
        self.player1.radiation = self.player1.RAD

class BrickBreakApp(App):
    """
    main app with build function
    """

    def build(self):
        """
        builds the app
        """
        music = SoundLoader.load("sound/PatakasWorld.wav")
        music.loop = True
        music.volume = 0.03
        if music:
            music.play()
        return Manager(transition=WipeTransition())

if __name__ == '__main__':
    BrickBreakApp().run()
