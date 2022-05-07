from tkinter import *

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # grab the data from the fields entered
    website = website_input.get()
    email_username = mail_user_input.get()
    password = password_input.get()

    # open the file and insert the fields formatted
    with open("data.txt", "a") as file:
        file.write(f"{website} | {email_username} | {password}\n")

        # delete the items in the website and password field
        website_input.delete(0, END)
        password_input.delete(0, END)
# ---------------------------- UI SETUP ------------------------------- #


# create window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# create a canvas
canvas = Canvas(width=200, height=200)
# get the image to use
lock_img = PhotoImage(file="logo.png")
# add image to the canvas
canvas.create_image(100, 100, image=lock_img)
canvas.grid(row=0, column=1)

# create a label for the Website
web_label = Label()
web_label.config(text="Website:", font="bold")
web_label.grid(row=1, column=0)

# create a label for the Email/Username:
mail_user_label = Label()
mail_user_label.config(text="Email/Username:", font="bold")
mail_user_label.grid(row=2, column=0)

# create a label for the Password
password_label = Label()
password_label.config(text="Password:", font="bold")
password_label.grid(row=3, column=0)

# create entry field for the website
website_input = Entry(width=35)
# Puts cursor in textbox.
website_input.focus()
# place the user entry box on the grid
website_input.grid(row=1, column=1, columnspan=2)

# create entry field for the Email/Username
mail_user_input = Entry(width=35)
# Adds some text to begin with.
mail_user_input.insert(END, "youremail@email.com")
# place the user entry box on the grid
mail_user_input.grid(row=2, column=1, columnspan=2)

# create entry field for the Password
password_input = Entry(width=19)
# place the user entry box on the grid
password_input.grid(row=3, column=1)

# create button for password generator
password_button = Button()
password_button.config(text="Generate Password", highlightthickness=10)
password_button.grid(row=3, column=2)

# create button for adding password
add_button = Button(width=36, command=save)
add_button.config(text="Add", highlightthickness=10)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
