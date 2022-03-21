from turtle import Screen
import bar
import Ball
import time
import Scoreboard
import Middle_Bar

PLAYS = 5

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

paddle_right = bar.Pad("right")
paddle_left = bar.Pad("left")
ball = Ball.Ball()
scoreboard = Scoreboard.ScoreBoard()
middle_bar = Middle_Bar.MiddleBar()

screen.listen()
screen.onkey(paddle_right.up, "z")
screen.onkey(paddle_right.down, "s")

screen.onkey(paddle_left.up, "Up")
screen.onkey(paddle_left.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.02)
    ball.move()
    if (paddle_right.distance(ball) <= 61 or paddle_left.distance(ball) <= 61) and abs(ball.xcor()) > 330:
        ball.hit()
    elif ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.update_1()
    elif ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.update_2()
    if scoreboard.player_1 == PLAYS:
        game_is_on = False
        scoreboard.winner("1")
    if scoreboard.player_2 == PLAYS:
        game_is_on = False
        scoreboard.winner("1")

screen.exitonclick()
