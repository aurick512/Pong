from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

ball = Ball()

left_paddle = Paddle((-350, 0))
left_paddle.color("Red")
right_paddle = Paddle((350, 0))
right_paddle.color("Blue")
scoreboard = ScoreBoard()
screen.listen()

game_is_on = True
while game_is_on:
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.update()
    time.sleep(ball.move_speed)
    ball.ball_move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    # Detect collision with right_paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()

    # When left player scores
    if ball.xcor() > 380:
        ball.reset()
        scoreboard.left_point()
    # When right player scores
    if ball.xcor() < -380:
        scoreboard.right_point()
        ball.reset()

screen.exitonclick()
