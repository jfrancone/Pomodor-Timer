from tkinter import *
import time
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
reps = 8
# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

speed_ms = 3

def count_down(count, rep):
    if rep == 0:
        title_label.config(text = "Work", font=(FONT_NAME, 50, "bold"))
    if rep == 1 or rep == 2:
        check_label.config(text ="reps: ✔")
    if rep == 3 or rep == 4:
        check_label.config(text ="reps: ✔✔")
    if rep == 5 or rep == 6:
        check_label.config(text ="reps: ✔✔✔")
    if rep == 7:
        check_label.config(text ="reps: ✔✔✔✔")

    # 300 seconds
    # 300 / 60 gives you num of minutes
    # what if I have 245 seconds remaining?
    # 245 / 60 rounded... equals 4 min
    # num of seconds would be 245 % 60
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # notice you are checking if it holds an int and then setting it to a string
    # this uses dynamic typing
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec:02}")
    # if it's the 1st/3rd/5th/7th rep, do 25 min
    # if it's 8th rep, count down uses long_break_sec
    # if 2/4/6 rep, it should count down to short break sec
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if count > 0:
        window.after(speed_ms, count_down, count - 1, rep)
    elif rep >=7:
        return
    else:
        rep += 1
        mod_rep = rep % 8
        new_count = 0
        if mod_rep in [0, 2, 4, 6]:
                title_label.config(text = "Work", font=(FONT_NAME, 50, "bold"), fg = GREEN)
                #title_label.grid(column=1, row=0)
                new_count = work_sec
        elif mod_rep in [1, 3, 5]:
                title_label.config(text = "Short Break", font=(FONT_NAME, 30, "bold"), fg = PINK)
                new_count = short_break_sec
        elif mod_rep in [7]:
                title_label.config(text = "Long Break", font=(FONT_NAME, 30, "bold"), fg = RED)
                new_count = long_break_sec
        print(f"new count: {new_count}")
        check_label.config(text ="✔")
        window.after(speed_ms, count_down, new_count - 1, rep)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)
# window.geometry("620x400")
# window.minsize(400, 400)

#window.after(1000,say_something, 3, 5, 8)
#text = "✔"
# fg=GREEN
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
# the numbers are # of pixels
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(
    100, 130, text="00:00", fill='black', font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


def start_button_click():
    work_sec = WORK_MIN * 60
    window.after(0, count_down, work_sec, 0)

    # IF IT'S THE 1/3/5/7 rep, do 25 minutes
    # if it's 8th rep, do long break secs
    # if 2/4/6 rep it should count down to short break seconds
    #count_down(5 * 60)
    # this way it counts down 5 minutes instead of 5 seconds


def reset_button_click():
    pass


start_button = Button(text='Start', command=start_button_click)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', command=reset_button_click)
reset_button.grid(column=2, row=2)
title_label = Label(text="Pomodoro Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 30, "bold"))
title_label.grid(column=1, row=0)
check_label = Label(text="reps: ", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)
window.mainloop()
