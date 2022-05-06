from tkinter import  *

# Creating a new window and configurations
window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=500, height=300)


# Label to hold the is equal to text
eq_label = Label()
eq_label.config(text="is equal to")
eq_label.grid(row=1, column=0)


# Text for user entering mileage to be converted
user_input = Text(height=1, width=10)
# Puts cursor in textbox.
user_input.focus()
# Adds some text to begin with.
user_input.insert(END, "0")
# place the user entry box on the grod
user_input.grid(row=0, column=1)

# Label for the Miles text placed on the grid
mi_label = Label()
mi_label.config(text="Miles")
mi_label.grid(row=0, column=2)

# Label to place the answer on the grid. Starts with value of 0
answer_label = Label()
answer_label.config(text="0")
answer_label.grid(row=1, column=1)

# Label for the Km text placed on the grid
km_label = Label()
km_label.config(text="Km")
km_label.grid(row=1, column=2)


# function gets the miles entered and gets the km conversion and places it on the grid
def action():
    # Gets current value in textbox at line 1, character 0
    miles_to_convert = float(user_input.get("1.0", END))
    # use the formula for mile conversion
    km = miles_to_convert * 1.609344
    # change the text in the answer label to the calculated km
    answer_label.config(text=km)


# calls action() when Calculate button is pressed
button = Button(text="Calculate", command=action)
button.grid(row=2, column=1)

window.mainloop()
