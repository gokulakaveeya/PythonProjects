from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, cords):
        super().__init__()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("White")
        self.penup()
        self.goto(cords)

    def move_up(self):
        ycor = self.ycor()+20
        self.goto(self.xcor(), ycor)

    def move_down(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)

    def w(self):
        ycor = self.ycor() + 20
        self.goto(self.xcor(), ycor)

    def s(self):
        ycor = self.ycor() - 20
        self.goto(self.xcor(), ycor)

