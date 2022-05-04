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


# make the window stay open
window.mainloop()
