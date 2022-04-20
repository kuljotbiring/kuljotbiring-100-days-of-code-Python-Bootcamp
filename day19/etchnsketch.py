from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def move_counter_clockwise():
    tim.left(10)


def move_clockwise():
    tim.right(10)


def clear_drawing():
    tim.clear()
    tim.penup()
    tim.home()


# listen for keyboard input
screen.listen()
# use space bar as the skey to track and call move_forwards function
screen.onkey(key="w", fun=move_forwards)
# use space bar as the skey to track and call move_backwards function
screen.onkey(key="s", fun=move_backwards)
# use space bar as the skey to track and call move_counter_clockwise function
screen.onkey(key="a", fun=move_counter_clockwise)
# use space bar as the skey to track and call move_clockwise function
screen.onkey(key="d", fun=move_clockwise)
# use space bar as the skey to track and call clear_drawing function
screen.onkey(key="c", fun=clear_drawing)


# exit the pop-up screen when clicking
screen.exitonclick()
