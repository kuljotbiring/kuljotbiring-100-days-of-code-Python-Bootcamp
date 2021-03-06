from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
               'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
               'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # use list comprehension to make list with the give number of letters, symbols and numbers
    password_letters = [choice(letters) for char in range(randint(8, 10))]
    password_symbols = [choice(symbols) for symbol in range(randint(2, 4))]
    password_numbers = [choice(numbers) for number in range(randint(2,4))]
    # combine the lists into one list
    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    # make the password list into one string
    password = "".join(password_list)
    # fill the password field with the generated password
    password_input.insert(0, password)
    # copy the created password into the clipboard
    pyperclip.copy(password)

# ---------------------------- SEARCH JSON ------------------------------- #


def find_password():
    # grab the data from the website field
    website = website_input.get()
    if website == "":
        messagebox.showerror(title="Error", message="You must enter a website to search for.")
    else:
        try:
            # open the file and insert the fields formatted
            with open("data.json", "r") as file:
                # read the old data
                data = json.load(file)
        except FileNotFoundError:
            messagebox.showinfo(title="Error", message="No Data File Found.")
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]
                messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
            else:
                messagebox.showerror(title="Error", message=f"You do not have account info for {website} saved.")
# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    # grab the data from the fields entered
    website = website_input.get()
    email_username = mail_user_input.get()
    password = password_input.get()
    new_data = {
        website: {
            "email": email_username,
            "password": password,
        }
    }

    # make sure any of the fields are not empty - if so show an error warning box
    if len(website) == 0 or len(email_username) == 0 or len(password) == 0:
        messagebox.showerror(title="ERROR!", message="Please don't leave any fields empty!")
    else:
        try:
            # open the file and insert the fields formatted
            with open("data.json", "r") as file:
                # read the old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            # updating old data with new data
            data.update(new_data)

            with open("data.json", "w") as file:
                # save/dumps the data we want into the file we specify and indented
                json.dump(data, file, indent=4)
        finally:
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
website_input = Entry(width=19)
# Puts cursor in textbox.
website_input.focus()
# place the user entry box on the grid
website_input.grid(row=1, column=1)

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

# create button for searching
search_button = Button(width=14, command=find_password)
search_button.config(text="Search", highlightthickness=10)
search_button.grid(row=1, column=2)

# create button for password generator
password_button = Button(command=generate_password)
password_button.config(text="Generate Password", highlightthickness=10)
password_button.grid(row=3, column=2)

# create button for adding password
add_button = Button(width=36, command=save)
add_button.config(text="Add", highlightthickness=10)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
