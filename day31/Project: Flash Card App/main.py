from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    # get the data frame
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/french_words.csv")
    # convert the data frame to a dictionary
    to_learn = original_data.to_dict(orient="records")
else:
    # convert the data frame to a dictionary
    to_learn = data.to_dict(orient="records")


def next_card():
    # pick a random list element from the list
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    # change the title word to French
    canvas.itemconfig(card_title, text="French", fill="black")
    # change the current French word to the randomly selected word
    canvas.itemconfig(card_word, text=current_card["French"], fill="black")
    # change the card image to the front card
    canvas.itemconfig(card_background, image=front_card_img)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    # change the title word to English
    canvas.itemconfig(card_title, text="English", fill="white")
    # change the current English definition word
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    # change the card image to show back of the card
    canvas.itemconfig(card_background, image=back_card_img)


def is_known():
    # remove the current word from the list of words
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/words_to_learn.csv", index=False)
    # get the next card
    next_card()


# create window
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# create a canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
# get the image to use for the front of the card
front_card_img = PhotoImage(file="./images/card_front.png")
# get the image to use for the back of the card
back_card_img = PhotoImage(file="./images/card_back.png")
# add front card image to the canvas
card_background = canvas.create_image(400, 263, image=front_card_img)
card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# create unknown button
x_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1, column=0)

# create known button
check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1, column=1)

# start the card off with a random word
next_card()

window.mainloop()
