from turtle import Turtle, Screen
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# make snake objects using a for loop. make 3 in a row

# get the starting positions as tuples
starting_position = [(0, 0), (-20, 0), (-40, 0)]

# make a list to hold the snake segments
segments = []

# make the pieces of the snake object
for position in starting_position:
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.penup()
    snake.goto(position)
    segments.append(snake)


# make the snake body continuously move
play_game = True

while play_game:
    screen.update()
    time.sleep(.1)
    # make each of the segments move in reverse order so they move to the piece ahead of them position
    for segment_num in range(len(segments) - 1, 0, -1):
        new_x = segments[segment_num - 1].xcor()
        new_y = segments[segment_num - 1].ycor()
        # get a hold of the last segment and move it where the second to last segment is
        segments[segment_num].goto(new_x, new_y)

    # get the first segment and move it 20 paces
    segments[0].forward(20)

screen.exitonclick()