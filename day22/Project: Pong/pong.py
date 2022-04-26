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

# exit the screen on click
screen.exitonclick()
