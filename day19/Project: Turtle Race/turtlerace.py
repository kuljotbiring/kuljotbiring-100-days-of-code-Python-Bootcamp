import turtle
from turtle import Turtle, Screen
import random

is_race_on = False

screen = Screen()
# set screen size
screen.setup(width=550, height=400)
# make a popup screen with a prompt and save into a variable
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [-120, -75, -25, 25, 75, 125]
race_turtles = []

# create turtle object with different attributes using the above lists
for turtle_index in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(-230, y_position[turtle_index])
    race_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    # for each of the created turtles
    for turtle in race_turtles:
        # if any turtle has reached the end (turtles take up 20 x 20 space)
        if turtle.xcor() > 230:
            is_race_on = False
            # get the color of the turtle that finished
            winning_color = turtle.pencolor()
            # check if that is what user entered
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        # other-wise move the turtles at random intervals
        speed = random.randint(0, 10)
        turtle.forward(speed)

screen.exitonclick()

