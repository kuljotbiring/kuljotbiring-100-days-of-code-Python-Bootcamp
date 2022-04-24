from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()

# make the snake body continuously move
play_game = True

while play_game:
    screen.update()
    time.sleep(.1)

    # get snake to move
    snake.move()


screen.exitonclick()