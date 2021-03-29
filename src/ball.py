from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty
)
from kivy.vector import Vector

class Ball(Widget):
    """
    add docstring
    """

    ballR = NumericProperty(255)
    ballG = NumericProperty(0)
    ballB = NumericProperty(0)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        add docstring
        """
        self.pos = Vector(*self.velocity) + self.pos

    def is_white(self):
        """
        add docstring
        """
        if(self.ballR == 255 and self.ballG == 255 and self.ballB == 255):
            return True
        return False

    def is_tan(self):
        """
        add docstring
        """
        if(self.ballR == 210 and self.ballG == 180 and self.ballB == 140):
            return True
        return False

    def is_green(self):
        """
        add docstring
        """
        if(self.ballR == 0 and self.ballG == 255 and self.ballB == 0):
            return True
        return False

    def is_blue(self):
        """
        add docstring
        """
        if(self.ballR == 0 and self.ballG == 0 and self.ballB == 255):
            return True
        return False