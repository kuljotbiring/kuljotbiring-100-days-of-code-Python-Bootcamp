from turtle import Turtle, Screen

screen = Screen()
screen.title("U.S. States Game")
# use the gif image as screen
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

# prompt the user using screen
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?")

screen.exitonclick()