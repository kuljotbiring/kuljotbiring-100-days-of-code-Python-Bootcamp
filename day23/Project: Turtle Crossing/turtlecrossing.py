import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# make a screen that is 600x600 and move the animation immediately
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# create the player turtle
player = Player()

# make a car object
car_manager = CarManager()

# listen for keyboard UP key pressed
screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # check if turtle has been hit by cars
    for car in car_manager.car_fleet:
        if car.distance(player) < 20:
            print("TURTLE WAS SQUASHED BY A CAR!")
            game_is_on = False




screen.exitonclick()
