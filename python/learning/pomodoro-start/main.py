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
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text = "00:00")
    title_label.config(text = "Timer", fg=GREEN, bg=YELLOW)
    check_marks.config(text = "")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps, timer

    if timer:
        window.after_cancel(timer)
        timer = None
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED, bg=YELLOW)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK, bg=YELLOW)
        count_down(short_break_sec)
    else:
        title_label.config(text="Work", fg=GREEN, bg=YELLOW)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text = f"{count_min}:{count_sec}")

    global timer
    if count > 0:
        timer = window.after(1000, count_down, count - 1)
    else:
        if reps % 2 != 0:
            work_sessions = (reps + 1) // 2
            marks = "✔" * work_sessions
            check_marks.config(text=marks)

        timer = window.after(1000, start_timer)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx = 50, pady = 50, bg = YELLOW, highlightthickness = 0)


title_label = Label(text = "Timer", fg = GREEN, bg = YELLOW, font = (FONT_NAME, 50))
title_label.grid(column = 1, row = 0)

canvas = Canvas(width = 200, height = 235, bg = YELLOW, highlightthickness = 0)
tomato_img = PhotoImage(file = "tomato.png")
canvas.create_image(100, 120, image = tomato_img)
timer_text = canvas.create_text(100, 137, text = "00:00", fill = "white", font = (FONT_NAME, 35, "bold"))
canvas.grid(column = 1, row = 1)

start_button = Button(text = "Start", fg = RED, font = (FONT_NAME, 15),
                      highlightthickness = 0, command = start_timer)
start_button.grid(column = 0, row = 2)

reset_button = Button(text = "Reset", fg = RED, font = (FONT_NAME, 15),
                      highlightthickness = 0, command = reset_timer)
reset_button.grid(column = 2, row = 2)

check_marks = Label(fg = GREEN, bg = YELLOW, font = (FONT_NAME, 15))
check_marks.grid(column = 1, row = 3)

window.mainloop()