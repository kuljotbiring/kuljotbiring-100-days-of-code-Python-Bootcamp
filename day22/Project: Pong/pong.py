from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# create the screen for the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

# create paddle objects with parameters for location and color
r_paddle = Paddle((350, 0), "dodger blue")
l_paddle = Paddle((-350, 0), "red")

# create the ball object
ball = Ball()


# make a key stroke listener
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

play_game = True

while play_game:
    # pause game to slow down ball movement
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect ball collision with top and bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # ball needs to bounce
        ball.bounce_y()

    # detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # detect if right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()

    # detect if left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()

# exit the screen on click
screen.exitonclick()
