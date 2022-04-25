from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = ScoreBoard()

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
        # add a segment to the snake body
        snake.extend()
        score_board.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        # snake has hit wall and game over
        play_game = False
        score_board.game_over()

    # detect collision with tail
    for segment in snake.segments[1:]:
        # ignore the head piece
        if snake.head.distance(segment) < 10:
            # trigger game over
            play_game = False
            score_board.game_over()

screen.exitonclick()
