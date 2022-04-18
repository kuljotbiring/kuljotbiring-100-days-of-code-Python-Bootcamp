from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("green")

# make a square using turtle and its methods
for move in range(4):
    tim.forward(100)
    tim.left(90)
    tim.forward(100)

# make a dotted line
for move in range(50):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()












# only lets the screen close when clicked
screen = Screen()
screen.exitonclick()