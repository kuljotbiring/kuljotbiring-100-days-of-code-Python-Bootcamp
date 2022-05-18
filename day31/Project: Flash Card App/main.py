from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"


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
canvas.create_text(400, 150, text="Title:", font=("Ariel", 40, "italic"))
canvas.create_text(400, 263, text="Word:", font=("Ariel", 60, "italic"))
canvas.grid(row=0, column=0, columnspan=2)

# create unknown button
x_image = PhotoImage(file="./images/wrong.png")
unknown_button = Button(image=x_image, highlightthickness=0)
unknown_button.grid(row=1, column=0)

# create known button
check_image = PhotoImage(file="./images/right.png")
known_button = Button(image=check_image, highlightthickness=0)
known_button.grid(row=1, column=1)

window.mainloop()
