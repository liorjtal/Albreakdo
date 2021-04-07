from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector
from kivy.properties import (
    NumericProperty, ReferenceListProperty
)

class CO2(Widget):
    """
    Carbon Dioxide object with its own speed
    """

    gasR = NumericProperty(100)
    gasG = NumericProperty(150)
    gasB = NumericProperty(150)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def co2_collision(self, ball):
        """
        reverse ball y velocity and return if collided with ghg
        """
        if ball.is_colliding(self):
            ball.y = ball.y - ball.height
            vx, vy = ball.velocity
            if self.is_ghg():
                vx, vy = self.bounce_ball(vx, vy, self.get_collision_point(ball))
                ball.velocity = vx, vy
                return "co2"

    def get_collision_point(self, ball):
        """
        return ball collision position. left, middle, or right
        """
        if ball.x < self.center_x - self.width/3:
            return "left"
        elif ball.x > self.center_x + self.width/5:
            return "right"
        else:
            return "middle"

    def bounce_ball(self, velx, vely, direction):
        """
        reflect ball based on brick collision position
        """
        if direction == "left":
            if velx > 0:
                velx = -velx
                vely = -vely
            else:
                velx = velx
                vely = -vely
        elif direction == "right":
            velx = abs(velx)
            vely = -vely
        elif direction == "middle":
            velx = velx
            vely = -vely
        return velx, vely

    def is_ghg(self):
        """
        check if ball is ghg
        """
        if(self.gasR == 100 and self.gasG == 150 and self.gasB == 150):
            return True
        return False

    def move(self, dt):
        """
        move ghg brick
        """
        self.pos = Vector(*self.velocity) + self.pos

class CH4(Widget):
    """
    Methane object with its own speed
    """

    speedRate = 2
    minSpeed = 3
    maxSpeed = 15

    gasR = NumericProperty(100)
    gasG = NumericProperty(150)
    gasB = NumericProperty(150)

    velocity_x = NumericProperty(0)
    velocity_y = NumericProperty(0)
    velocity = ReferenceListProperty(velocity_x, velocity_y)

    def ch4_collision(self, ball):
        """
        reverse ball y velocity and return if collided with ghg
        """
        if ball.is_colliding(self):
            ball.y = ball.y - ball.height
            vx, vy = ball.velocity
            if self.is_ghg():
                vx, vy = self.bounce_ball(vx, vy, self.get_collision_point(ball))
                ball.velocity = vx, vy
                return "ch4"

    def get_collision_point(self, ball):
        """
        return ball collision position. left, middle, or right of object
        """
        if ball.x < self.center_x - self.width/3:
            return "left"
        elif ball.x > self.center_x + self.width/5:
            return "right"
        else:
            return "middle"

    def bounce_ball(self, velx, vely, direction):
        """
        reflect ball based on brick collision position
        """
        if direction == "left":
            if velx > 0:
                velx = -velx
                vely = -vely
            else:
                velx = velx
                vely = -vely
        elif direction == "right":
            velx = abs(velx)
            vely = -vely
        elif direction == "middle":
            velx = velx
            vely = -vely
        return velx, vely

    def is_ghg(self):
        """
        check if brick is ghg
        """
        if(self.gasR == 100 and self.gasG == 150 and self.gasB == 150):
            return True
        return False

    def move(self, dt):
        """
        move ghg brick
        """
        self.speed_up(dt)
        self.pos = Vector(*self.velocity) + self.pos

    def apply_speed_rate(self, dt):
        """
        speed rate for moving ghg brick
        """
        self.velocity_x += self.speedRate * dt

    def speed_up(self, dt):
        """
        speed up ghg brick movement
        """
        #if we exceed the defined range then correct the sign of speedRate.
        if self.velocity_x < self.minSpeed:
            self.speedRate = abs(self.speedRate)
        elif self.velocity_x > self.maxSpeed:
            self.speedRate = -abs(self.speedRate)
        self.apply_speed_rate(dt)
