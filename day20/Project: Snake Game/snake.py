from turtle import Turtle
# get the starting positions as tuples
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        # make snake objects using a for loop. make 3 in a row
        # make the pieces of the snake object
        for position in STARTING_POSITIONS:
            snake = Turtle()
            snake.color("white")
            snake.shape("square")
            snake.penup()
            snake.goto(position)
            self.segments.append(snake)

    def move(self):
        # make each of the segments move in reverse order so they move to the piece ahead of them position
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            # get a hold of the last segment and move it where the second to last segment is
            self.segments[segment_num].goto(new_x, new_y)

        # get the first segment and move it 20 paces
        self.segments[0].forward(MOVE_DISTANCE)
