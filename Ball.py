from turtle import Turtle
import random

PAS = 5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.color("red")
        self.penup()
        self.x_step = random.randint(1, 4)
        self.y_step = random.randint(1, 4)
        self.speeding = 1

    def move(self):
        x = self.xcor() + self.x_step*self.speeding
        y = self.ycor() + self.y_step*self.speeding
        self.goto(x, y)
        self.bounce()

    def bounce(self):
        if abs(self.ycor()) > 285:
            self.y_step *= -1

    def hit(self):
        self.speeding += 0.3
        self.x_step *= -1

    def hit_rev(self):
        self.x_step *= -1
        self.y_step *= -1

    def reset_pos(self):
        self.goto(0, 0)
        self.speeding = 1.5
        self.x_step *= -1
