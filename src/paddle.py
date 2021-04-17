from kivy.uix.widget import Widget
from kivy.properties import NumericProperty
from kivy.vector import Vector
from screens import Manager

class Paddle(Widget):
    """
    Player's avatar. Contains color, timer, and radiation properties
    """

    duration = 100
    radiation = 10

    paddleR = NumericProperty(255)
    paddleG = NumericProperty(255)
    paddleB = NumericProperty(255)
    timer = NumericProperty(duration)
    radiation = NumericProperty(radiation)


    def is_white(self):
        """
        check if paddle is currently white
        """
        if(self.paddleR == 255 and self.paddleG == 255 and self.paddleB == 255):
            return True
        return False

    def is_tan(self):
        """
        check if paddle is currently tan
        """
        if(self.paddleR == 210 and self.paddleG == 180 and self.paddleB == 140):
            return True
        return False

    def is_green(self):
        """
        check if paddle is currently green
        """
        if(self.paddleR == 0 and self.paddleG == 255 and self.paddleB == 0):
            return True
        return False

    def is_blue(self):
        """
        check if paddle is currently blue
        """
        if(self.paddleR == 0 and self.paddleG == 0 and self.paddleB == 255):
            return True
        return False

    def on_touch_up(self, touch):
        """
        touch controls to change paddle color if touched paddle
        """
        if self.collide_point(touch.x, touch.y):
            #white to tan
            if self.is_white():
                self.paddleR = 210
                self.paddleG = 180
                self.paddleB = 140

            #tan to green
            elif self.is_tan():
                self.paddleR = 0
                self.paddleG = 255
                self.paddleB = 0

            #green to blue
            elif self.is_green():
                self.paddleR = 0
                self.paddleG = 0
                self.paddleB = 255

            #blue to white
            elif self.is_blue():
                self.paddleR = 255
                self.paddleG = 255
                self.paddleB = 255

    def bounce_ball(self, ball):
        """
        ball direction & velocity based on point of contact & color  of paddle.
        """
        if ball.is_colliding(self):
            vx, vy = ball.velocity

            #if paddle is white
            if (self.is_white() and (ball.is_white() or ball.is_red())):
                vx, vy = self.bounce_white(vx, vy, self.get_collision_point(ball))
                ball.ballR = self.paddleR
                ball.ballG = self.paddleG
                ball.ballB = self.paddleB
            #if paddle is tan
            elif (self.is_tan() and (ball.is_tan() or ball.is_red())):
                vx, vy = self.bounce_tan(vx, vy, self.get_collision_point(ball))
                ball.ballR = self.paddleR
                ball.ballG = self.paddleG
                ball.ballB = self.paddleB
            #if paddle is green
            elif (self.is_green() and (ball.is_green() or ball.is_red())):
                vx, vy = self.bounce_green(vx, vy, self.get_collision_point(ball))
                ball.ballR = self.paddleR
                ball.ballG = self.paddleG
                ball.ballB = self.paddleB
            #if paddle is blue
            elif (self.is_blue() and (ball.is_blue() or ball.is_red())):
                vx, vy = self.bounce_blue(vx, vy, self.get_collision_point(ball))
                ball.ballR = self.paddleR
                ball.ballG = self.paddleG
                ball.ballB = self.paddleB
            #change ball color and velocity to match paddle hit
            ball.velocity = vx, vy

    def get_collision_point(self, ball):
        """
        return ball touch position. left, middle, or right part of paddle
        """
        if ball.x < self.center_x - self.width/3:
            return "leftPaddle"
        elif ball.x > self.center_x + self.width/5:
            return "rightPaddle"
        else:
            return "middlePaddle"

    def bounce_white(self, velx, vely, direction):
        """
        reflect white ball based on paddle collision position
        """
        if direction == "leftPaddle":
            velx = -6
            vely = 18
        elif direction == "rightPaddle":
            velx = 6
            vely = 18
        elif direction == "middlePaddle":
            if velx > 0:
                velx = 6
                vely = 18
            else:
                velx = -6
                vely = 18
        return velx, vely

    def bounce_tan(self, velx, vely, direction):
        """
        reflect tan ball based on paddle collision position
        """
        if direction == "leftPaddle":
            velx = -4
            vely = 12
        elif direction == "rightPaddle":
            velx = 4
            vely = 12
        elif direction == "middlePaddle":
            if velx > 0:
                velx = 4
                vely = 12
            else:
                velx = -4
                vely = 12
        return velx, vely

    def bounce_green(self, velx, vely, direction):
        """
        reflect green ball based on paddle collision position
        """
        if direction == "leftPaddle":
            velx = -3
            vely = 9
        elif direction == "rightPaddle":
            velx = 3
            vely = 9
        elif direction == "middlePaddle":
            if velx > 0:
                velx = 3
                vely = 9
            else:
                velx = -3
                vely = 9
        return velx, vely

    def bounce_blue(self, velx, vely, direction):
        """
        reflect blue ball based on paddle collision position
        """
        if direction == "leftPaddle":
            velx = -2
            vely = 6
        elif direction == "rightPaddle":
            velx = 2
            vely = 6
        elif direction == "middlePaddle":
            if velx > 0:
                velx = 2
                vely = 6
            else:
                velx = -2
                vely = 6
        return velx, vely
