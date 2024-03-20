from turtle import Turtle, Screen

ALIGN = "Center"
FONT = ("courier", 50, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.penup()
        self.ht()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.goto(-100, 200)
        self.write(self.l_score, align=ALIGN, font=FONT)
        self.goto(100, 200)
        self.write(self.r_score, align=ALIGN, font=FONT)

    def add_l_score(self):
        self.l_score = + 1
        self.clear()
        self.update_score()

    def add_r_score(self):
        self.r_score = + 1
        self.clear()
        self.update_score()
