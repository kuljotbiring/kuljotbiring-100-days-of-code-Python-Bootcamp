from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
tim.color("green")

# make a square using turtle and its methods
# for move in range(4):
#     tim.forward(100)
#     tim.left(90)
#     tim.forward(100)

# make a dotted line
# for move in range(50):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()

colors = ["red", "green", "blue", "purple", "orange", "magenta", "black", "deep sky blue", "dim gray"]

tim.speed("fastest")
# draw shapes
def draw_shape(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)


for shape_side_n in range(3, 11):
    tim.color(random.choice(colors))
    draw_shape(shape_side_n)


# generate random walk
directions = [0, 90, 180, 270]
tim.pensize(15)
for _ in range(200):
    tim.color(random.choice(colors))
    tim.forward(30)
    tim.setheading(random.choice(directions))






# only lets the screen close when clicked
screen = Screen()
screen.exitonclick()