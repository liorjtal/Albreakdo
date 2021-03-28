from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import ScreenManager

class Control(Widget):
    """
    add docstring
    """
    player1 = ObjectProperty(None)

    def on_touch_move(self, touch):
        """
        add docstring
        """
        if touch.x < self.width / 2:
            self.player1.center_x = touch.x
        if touch.x > self.width - self.width / 2:
            self.player1.center_x = touch.x

class About(Widget):
    """
    add docstring
    """

class ElectroMagneticSpectrum(Widget):
    """
    add docstring
    """

class Sun(Widget):
    """
    add docstring
    """

class Albedo(Widget):
    """
    add docstring
    """

class Colors(Widget):
    """
    add docstring
    """

class Gasses(Widget):
    """
    add docstring
    """

class Manager(ScreenManager):
    """
    add docstring
    """
