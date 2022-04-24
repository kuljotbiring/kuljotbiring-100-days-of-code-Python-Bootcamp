from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# make snake objects using a for loop. make 3 in a row

# get the starting positions as tuples
starting_position = [(0, 0), (-20, 0), (-40, 0)]

# make the pieces of the snake object
for position in starting_position:
    snake = Turtle()
    snake.color("white")
    snake.shape("square")
    snake.goto(position)


screen.exitonclick()