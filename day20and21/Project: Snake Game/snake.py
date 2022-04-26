from turtle import Turtle
# get the starting positions as tuples
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        # make snake objects using a for loop. make 3 in a row
        # make the pieces of the snake object
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle()
        snake.color("dark olive green")
        snake.shape("square")
        snake.penup()
        snake.goto(position)
        self.segments.append(snake)

    # adds a segment to the last position using index slicing
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        # make each of the segments move in reverse order so they move to the piece ahead of them position
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            # get a hold of the last segment and move it where the second to last segment is
            self.segments[segment_num].goto(new_x, new_y)

        # get the first segment and move it 20 paces
        self.head.forward(MOVE_DISTANCE)

# each of below methods moves when corresponding key is pressed
# prevents the snake from going back on itself
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
