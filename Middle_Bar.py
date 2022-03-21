from turtle import Turtle


class MiddleBar(Turtle):
    def __init__(self):
        super().__init__()
        for i in range(-6, 7):
            segment = Turtle()
            segment.penup()
            segment.shape("square")
            segment.shapesize(stretch_len=0.5, stretch_wid=2)
            segment.color("white")
            segment.goto(0, i * 60)
