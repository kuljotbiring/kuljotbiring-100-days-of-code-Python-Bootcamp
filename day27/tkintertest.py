import tkinter

# have tkinter create a window
window = tkinter.Tk()

# change the title of the window
window.title("My First GUI Program")

# size the window
window.minsize(width=500, height=300)

# components for inside window ie labels
# create a label
my_label = tkinter.Label(text="I am a label", font=("Arial", 24, "bold"))
# place the label and center it on the screen
my_label.pack()
my_label["text"] = "New Text!"
# or you can change text in lae this way
my_label.config(text="New Text")

# Entry component - makes a field for entry
entry = tkinter.Entry(width=10)
entry.pack()


# get button to work using event listener
def button_clicked():
    # change text in label by getting the value entered
    my_label.config(text=entry.get())


# create a button
button = tkinter.Button(text="Click Me", command=button_clicked)
button.pack()


# make the window stay open
window.mainloop()
