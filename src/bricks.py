from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty
)

class CO2Brick(Widget):
    """
    Carbon Dioxide
    """

    speedRate = 2
    minSpeed = 6
    maxSpeed = 12

    brickR = NumericProperty(100)
    brickG = NumericProperty(150)
    brickB = NumericProperty(150)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def co2_collision(self, ball):
        """
        ball destroy brick based on color of ball.
        """
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            ball.velocity = vx, -vy

            #if brick is ghg
            if self.is_ghg():
                return "co2"

    def is_ghg(self):
        """
        add docstring
        """
        if(self.brickR == 100 and self.brickG == 100 and self.brickB == 100):
            return True
        return False

    def move(self, dt):
        """
        add docstring
        """
        self.speed_up(dt)
        self.pos = Vector(*self.velocity) + self.pos

    def apply_speed_rate(self, dt):
        self.velocity_x += self.speedRate * dt

    def speed_up(self, dt):
            #if we exceed the defined range then correct the sign of speedRate.
        if self.velocity_x < self.minSpeed:
            self.speedRate = abs(self.speedRate)
        elif self.velocity_x > self.maxSpeed:
            self.speedRate = -abs(self.speedRate)
        self.apply_speed_rate(dt)


class CH4Brick(Widget):
    """
    Carbon Dioxide
    """

    speedRate = 2
    minSpeed = 3
    maxSpeed = 15

    brickR = NumericProperty(100)
    brickG = NumericProperty(150)
    brickB = NumericProperty(150)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def ch4_collision(self, ball):
        """
        ball destroy brick based on color of ball.
        """
        if self.collide_widget(ball):
            vx, vy = ball.velocity
            ball.velocity = vx, -vy

            #if brick is ghg
            if self.is_ghg():
                return "ch4"

    def is_ghg(self):
        """
        add docstring
        """
        if(self.brickR == 100 and self.brickG == 100 and self.brickB == 100):
            return True
        return False

    def move(self, dt):
        """
        add docstring
        """
        self.speed_up(dt)
        self.pos = Vector(*self.velocity) + self.pos

    def apply_speed_rate(self, dt):
        self.velocity_x += self.speedRate * dt

    def speed_up(self, dt):
            #if we exceed the defined range then correct the sign of speedRate.
        if self.velocity_x < self.minSpeed:
            self.speedRate = abs(self.speedRate)
        elif self.velocity_x > self.maxSpeed:
            self.speedRate = -abs(self.speedRate)
        self.apply_speed_rate(dt)
