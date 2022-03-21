from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.player_1 = 0
        self.player_2 = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 210)
        self.color("white")
        self.write(f"{self.player_1}        {self.player_2}", False, "center", ("Courier", 50, "bold"))

    def update_1(self):
        self.player_1 += 1
        self.clear()
        self.write(f"{self.player_1}        {self.player_2}", False, "center", ("Courier", 50, "bold"))

    def update_2(self):
        self.player_2 += 1
        self.clear()
        self.write(f"{self.player_1}        {self.player_2}", False, "center", ("Courier", 50, "bold"))

    def winner(self, player):
        self.goto(0, 0)
        self.color("red")
        if player == "1":
            self.write(f"PLAYER 1 WON", False, "center", ("Courier", 50, "bold"))
        if player == "2":
            self.write(f"PLAYER 2 WON", False, "center", ("Courier", 50, "bold"))