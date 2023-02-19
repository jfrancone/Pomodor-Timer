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
                new_count = work_sec
        elif mod_rep in [1, 3, 5]:
                new_count = short_break_sec
        elif mod_rep in [7]:
                new_count = long_break_sec
        print(f"new count: {new_count}")
        window.after(speed_ms, count_down, new_count - 1, rep)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

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

# count_down(5)
# def rep_tracker(rep):
#     rep += 1
#     print(f"rep = {rep}")
#     return rep

# def recursive_timer():


def start_button_click():
    work_sec = WORK_MIN * 60
    #count = 300

    #window.after(1000,count_down, count - 1)
    #  START HERE while rep < 8:
    #     cumulative_millisecs = 1000
    #     rep += 1
    #     if (rep % 8 == 0 and cumulative_millisecs >= ) :
    #         window.after(cumulative_millisecs,count_down, long_break_sec, rep)
    #     elif (rep % 2 == 0):
    #         window.after(cumulative_millisecs,count_down, short_break_sec, rep)
    #         cumulative_millisecs += 1000 * short_break_sec
    #     else:
    window.after(0, count_down, work_sec, 0)
    #cumulative_millisecs += 1000 * work_sec

    # while ((reps % 2) == 1):
    # count_down(60)
    #window.after(60, rep_tracker, reps)

    # all these reps are happening right away before countdown is over

    # count_down(10)
    #reps += 1

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
title_label = Label(text="Timer", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 50, "bold"))
title_label.grid(column=1, row=0)
check_label = Label(text="✔", bg=YELLOW, fg=GREEN,
                    font=(FONT_NAME, 20, "bold"))
check_label.grid(column=1, row=3)
window.mainloop()
