from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #

# create window
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

# create a canvas
canvas = Canvas(width=200, height=200)
# get the image to use
lock_img = PhotoImage(file="logo.png")
# add image to the canvas
canvas.create_image(100, 100, image=lock_img)
canvas.pack()

window.mainloop()