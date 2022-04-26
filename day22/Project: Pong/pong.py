from turtle import Turtle, Screen


# create the screen for the game
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

paddle = Turtle()
paddle.color("white")
paddle.shape("square")
paddle.shapesize(stretch_len=1, stretch_wid=5)
paddle.penup()
paddle.goto(350, 0)


# move the paddle up 20 places. then make it go to new x, y coordinate
def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)


# move the paddle down 20 places. then make it go to new x, y coordinate
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)


# make a key stroke listener
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

play_game = True

while play_game:
    screen.update()

screen.exitonclick()
