from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector

class Brick(Widget):
    """
    Carbon Dioxide/ Methane
    """

    brickR = NumericProperty(100)
    brickG = NumericProperty(100)
    brickB = NumericProperty(100)

    def check_collision(self, ball):
        """
        ball destroy brick based on color of ball.
        """
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            ball.velocity = vx, -vy
            #if brick is white
            if self.is_white() and ball.is_white():
                return "w"
            #if brick is tan
            elif self.is_tan() and ball.is_tan():
                return "t"
            #if brick is green
            elif self.is_green() and ball.is_green():
                return "g"
            #if brick is blue
            elif self.is_blue() and ball.is_blue():
                return "b"
            #if brick is ghg
            elif self.is_ghg():
                return "ghg"

    def is_white(self):
        """
        add docstring
        """
        if(self.brickR == 255 and self.brickG == 255 and self.brickB == 255):
            return True
        return False

    def is_tan(self):
        """
        add docstring
        """
        if(self.brickR == 210 and self.brickG == 180 and self.brickB == 140):
            return True
        return False

    def is_green(self):
        """
        add docstring
        """
        if(self.brickR == 0 and self.brickG == 255 and self.brickB == 0):
            return True
        return False

    def is_blue(self):
        """
        add docstring
        """
        if(self.brickR == 0 and self.brickG == 0 and self.brickB == 255):
            return True
        return False

    def is_ghg(self):
        """
        add docstring
        """
        if(self.brickR == 100 and self.brickG == 100 and self.brickB == 100):
            return True
        return False
