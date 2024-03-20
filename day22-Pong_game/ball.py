from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1, 1)
        self.color("White")
        self.penup()
        self.goto(0, 0)
        self.move_x = 10
        self.move_y = 10
        self.moving_speed = 0.1

    def move_ball(self):
        new_xcor = self.xcor() + self.move_x
        new_ycor = self.ycor() + self.move_y
        self.goto(new_xcor, new_ycor)

    def bounce_ball_y(self):
        self.move_y *= -1

    def bounce_ball_x(self):
        self.move_x *= -1
        self.moving_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        # to make the ball to go in opposite direction when the paddle misses.
        self.bounce_ball_x()
        self.moving_speed = 0.1






