from turtle import Turtle, Screen, colormode
import random

t = Turtle()
screen = Screen()
t.shape("turtle")
t.speed("fastest")
t.pensize(10)
t.ht()


def colours():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    tuple_colour = (red, green, blue)
    return tuple_colour


def shape(side):
    angle = 360 / side
    for _ in range(side):
        t.forward(50)
        t.right(angle)
    t.home()


def spirograph(angle):
    for i in range(int(360 / angle)):
        colormode(255)
        t.color(colours())
        t.circle(40)
        t.left(angle)


# print a 3 side triangle to 10 sided decagon in different color using turtle
# for i in range(3, 11):
#     colormode(255)
#     t.color(colours())
#     shape(i)


# random walk with color each time using turtle
# direction = [0, 90, 180, 270]
# for i in range(200):
#     colormode(255)
#     t.color(colours())
#     t.forward(20)
#     t.setheading(random.choice(direction))


# draw a circle in different color - spirograph
# spirograph(5)


# final project of reproducing hirst spot painting
"""import colorgram

colors = colorgram.extract('hirst_spot_painting.jpg', 30)
color_list = []
for colors in colors:
    red = colors.rgb.r
    green = colors.rgb.g
    blue = colors.rgb.b
    rgb = (red, green, blue)
    color_list.append(rgb)
print(color_list)"""

color_list = [(58, 106, 148), (224, 200, 109), (134, 84, 58), (223, 138, 62), (196, 145, 171),
              (234, 226, 204), (224, 234, 230), (141, 178, 204), (139, 82, 105), (209, 90, 69), (188, 80, 120),
              (68, 105, 90), (237, 225, 233), (134, 182, 136), (133, 133, 74), (63, 156, 92), (48, 156, 194),
              (183, 192, 201), (214, 177, 191), (19, 57, 93), (21, 68, 113), (112, 123, 149), (229, 174, 165),
              (172, 203, 182), (158, 205, 215), (69, 58, 47), (108, 47, 60), (53, 70, 65), (72, 64, 53)]
goto_angle = (-200, -150, -100, -50, 0, 50, 100, 150, 200, 250)

for i in goto_angle:
    t.penup()
    t.goto(-250, i)
    for _ in range(10):
        colormode(255)
        t.dot(20, random.choice(color_list))
        t.penup()
        t.fd(50)

screen.exitonclick()
