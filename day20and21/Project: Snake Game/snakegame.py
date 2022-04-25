from turtle import Screen
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()

# make a key stroke listener
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# make the snake body continuously move
play_game = True

while play_game:
    screen.update()
    time.sleep(.1)

    # get snake to move
    snake.move()

    # detect collision with food. if collision - make new food
    if snake.head.distance(food) < 15:
        food.refresh()


screen.exitonclick()