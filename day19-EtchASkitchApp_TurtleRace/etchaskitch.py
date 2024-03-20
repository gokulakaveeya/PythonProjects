from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
t.shape("turtle")


t.speed("fastest")
t.pensize(5)


def forward():
    t.forward(20)


def backward():
    t.backward(20)


def clockwise():
    new_heading = t.heading()+10
    t.setheading(new_heading)


def anticlockwise():
    new_heading = t.heading() - 10
    t.setheading(new_heading)


def clearscreen():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


screen.onkey(forward, "Right")
screen.onkey(backward, "Left")
screen.onkey(clockwise, "Up")
screen.onkey(anticlockwise, "Down")
screen.onkey(clearscreen, "c")
screen.listen()

screen.exitonclick()
