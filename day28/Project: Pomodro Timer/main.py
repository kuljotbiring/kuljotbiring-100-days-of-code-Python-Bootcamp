from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start_timer():
    count_down(5 * 60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def count_down(count):
    count_minute = math.floor(count / 60)
    count_seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{count_minute}:{count_seconds}")
    if count > 0:
        window.after(1000, count_down, count - 1)

# ---------------------------- UI SETUP ------------------------------- #


# create window
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# create a canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# get the image to use
tomato_img = PhotoImage(file="tomato.png")
# add image to the canvas
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

label = Label()
label.config(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 50, "normal"))
label.grid(row=0, column=1)

start_button = Button()
start_button.config(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button()
reset_button.config(text="Reset", highlightthickness=0)
reset_button.grid(row=2, column=2)

check_label = Label()
check_label.config(text="✔", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 20, "normal"))
check_label.grid(row=3, column=1)


window.mainloop()
