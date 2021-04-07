from kivy.uix.widget import Widget
from kivy.properties import (
    NumericProperty, ReferenceListProperty
)
from kivy.vector import Vector

class Ball(Widget):
    """
    widget for ball containing color and velocity properties
    """

    ballR = NumericProperty(255)
    ballG = NumericProperty(0)
    ballB = NumericProperty(0)

    colors = [[255,0,0], [255,255,255], [210,180,140], [0,255,0], [0,0,255]]

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def move(self):
        """
        move ball through space based on velocity
        """
        self.pos = Vector(*self.velocity) + self.pos

    def is_colliding(self,target):
        """
        determine if ball is colliding with something and where
        """
        #check left edges in relation to one another
        if self.x > target.x + target.width or target.x > self.x + self.width:
            return False
        #check bottom edges in relation to one another
        if self.y > target.y + target.height or target.y > self.y + self.height:
            return False

        return True

    def is_white(self):
        """
        check if ball is white
        """
        if(self.ballR == 255 and self.ballG == 255 and self.ballB == 255):
            return True
        return False

    def is_tan(self):
        """
        check if ball is tan
        """
        if(self.ballR == 210 and self.ballG == 180 and self.ballB == 140):
            return True
        return False

    def is_green(self):
        """
        check if ball is green
        """
        if(self.ballR == 0 and self.ballG == 255 and self.ballB == 0):
            return True
        return False

    def is_blue(self):
        """
        check if ball is blue
        """
        if(self.ballR == 0 and self.ballG == 0 and self.ballB == 255):
            return True
        return False

    def is_red(self):
        """
        check if ball is red
        """
        if(self.ballR == 255 and self.ballG == 0 and self.ballB == 0):
            return True
        return False
