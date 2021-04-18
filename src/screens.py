from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

class Control(Widget):
    """
    control screen
    """
    player1 = ObjectProperty(None)

    def on_touch_move(self, touch):
        """
        move paddle
        """
        if touch.x < self.width / 2:
            self.player1.center_x = touch.x
        if touch.x > self.width - self.width / 2:
            self.player1.center_x = touch.x

class About(Widget):
    """
    about screen
    """

class ElectroMagneticSpectrum(Widget):
    """
    em screen
    """

class Sun(Widget):
    """
    sun screen
    """

class Albedo(Widget):
    """
    albedo screen
    """

class Colors(Widget):
    """
    colors screen
    """

class Gasses(Widget):
    """
    gasses screen
    """

class Manager(ScreenManager):
    """
    screen manager
    """
