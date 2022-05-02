from turtle import Turtle, Screen
import pandas

TOTAL_STATES = 50
FONT = ('Arial', 10, 'normal')
x_cords = []
y_cords = []

correct_guess = []


# removes extraneous information from data needed
def format_data(data_item):
    return data_item.to_string(index=False)


# adds the state to the map as a name turtle
def update_map(x, y):
    state_turtle = Turtle()
    state_turtle.color("black")
    state_turtle.penup()
    state_turtle.hideturtle()
    state_turtle.goto(x, y)
    state_turtle.write(state, font=FONT, align="center")


screen = Screen()
screen.title("U.S. States Game")
# use the gif image as screen
image = "blank_states_img.gif"
screen.addshape(image)

turtle = Turtle()
turtle.shape(image)

# get a hold of the csv data
data = pandas.read_csv("50_states.csv")

run_game = True

while run_game:
    # prompt the user using screen
    answer_state = screen.textinput(title=f"{len(correct_guess)}/{TOTAL_STATES} States Correct",
                                    prompt="What's another state's name?")

    # convert the guess to title case
    answer_state = answer_state.title()

    if answer_state == "Quit":
        run_game = False
        break

    if answer_state is None:
        continue

    # check if user entry exist in the csv file
    state_info = data[data["state"] == answer_state]

    if state_info.empty:
        pass
    else:
        state = state_info.state
        state = format_data(state)
        # if the state is already not guessed correctly
        if state not in correct_guess:
            # add state to the list
            correct_guess.append(state)
            # get the x and y coordinates and format them
            x_val = state_info.x
            x_val = format_data(x_val)
            x_val = int(x_val)
            y_val = state_info.y
            y_val = format_data(y_val)
            y_val = int(y_val)
            # function to place state name on the map
            update_map(x_val, y_val)
        else:
            continue


screen.exitonclick()
