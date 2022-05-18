from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

# get the data frame
data = pandas.read_csv("./data/french_words.csv")
# convert the data frame to a dictionary
to_learn = data.to_dict(orient="records")


def next_card():
    # pick a random list element from the list
    current_card = random.choice(to_learn)
    # change the title word to french
    canvas.itemconfig(card_title, text="French")
    # change the current French word to the randomly selected word
    canvas.itemconfig(card_word, text=current_card["French"])


# create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# create a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# get the image to use
card_img = PhotoImage(file="./images/card_front.png")
# add image to the canvas
canvas.create_image(400, 263, image=card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# create unknown button
x_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# create known button
check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(row=1, column=1)

# start the card off with a random word
next_card()

window.mainloop()
