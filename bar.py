from turtle import Turtle


class Pad(Turtle):
    def __init__(self, position):
        super().__init__()
        if position == "right":
            x = 350
        else:
            x = -350
        self.penup()
        self.speed("fastest")
        self.goto(x, 0)
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)

    def up(self):
        if self.ycor() < 240:
            y = self.ycor() + 40
            self.goto(self.xcor(), y)

    def down(self):
        if self.ycor() > -240:
            y = self.ycor() - 40
            self.goto(self.xcor(), y)
