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