from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGN = 'Left'


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("Black")
        self.penup()
        self.ht()
        self.level = 1
        self.goto(-280, 270)
        self.update_score()

    def update_score(self):
        self.write(arg=f"Level: {self.level}", align=ALIGN, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.update_score()



    def gameover(self):
        self.goto(0, 0)
        self.write(arg="Game Over", align=ALIGN, font=FONT)

