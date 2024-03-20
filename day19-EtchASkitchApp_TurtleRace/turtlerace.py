from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput("Make your bet", "which turtle you're choosing?")
race_on = False
turtles = ["red", "green", "yellow", "orange", "purple"]

angle = -150
all_turtle = []
for turtle in turtles:
    t = Turtle(shape="turtle")
    t.color(turtle)
    t.penup()
    angle += 50
    t.goto(-200, angle)
    all_turtle.append(t)
if bet:
    race_on = True

while race_on:
    randint = random.randint(0, 10)
    random_turtle = random.choice(all_turtle)
    random_turtle.fd(randint)
    if random_turtle.xcor() > 230:
        race_on = False
        win_turtle = random_turtle.pencolor()
        if bet.lower() == win_turtle:
            print(f"You Win :-)")
        else:
            print(f"You Lose :-(")
        print(f"{win_turtle} turtle is a winner!!")
screen.exitonclick()
