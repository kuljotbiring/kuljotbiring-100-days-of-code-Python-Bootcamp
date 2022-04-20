from turtle import Turtle, Screen

tim = Turtle()


screen = Screen()


# moves the turtle 10 spaces
def move_forwards():
    tim.forward(10)


# listen for keyboard input
screen.listen()
# use space bar as the skey to track and call move_forwards function
screen.onkey(key="space", fun=move_forwards)

# exit the pop-up screen when clicking
screen.exitonclick()
