from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


# inherit from the Turtle super class and start the turtle at starting position
# set its attributes and have turtle facing north
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    # function that is called when UP key is pressed moving the turtle forward 10 spaces
    def move_up(self):
        self.forward(MOVE_DISTANCE)

    # check if turtle has safely crossed the street
    def has_crossed(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            self.setheading(90)
            print("YOU MADE IT ACROSS THE STREET")
            return True

