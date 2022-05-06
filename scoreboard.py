from turtle import Turtle
ALIGN = 'center'
FONT = ('Courier', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.pu()
        self.hideturtle()
        self.goto(0, 260)
        self.score = 0
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", move=False, align=ALIGN, font=FONT)

    def eat(self):
        self.score += 1
        self.clear()
        self.update()

    def over(self):
        self.goto(0, 0)
        self.color("red")
        self.write("GAME OVER", move=False, align=ALIGN, font=FONT)
