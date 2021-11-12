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
REPS = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- #


def reset_timer():
    global REPS
    window.after_cancel(timer)
    REPS = 0
    label_check.config(text="✔")
    label_timer.config(text="Timer", bg=YELLOW, fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #


def start_timer():
    global REPS
    REPS += 1
    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    work_in_progress = True
    if REPS % 2 == 0 and REPS % 8 != 0:
        label_timer.config(text="Short break", fg=PINK)
        countdown(short_break_sec)
    elif REPS % 8 == 0:
        label_timer.config(text="Long break", fg=RED)
        countdown(long_break_sec)
    else:
        label_timer.config(text="Work", fg=GREEN)
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #


def countdown(count):
    global REPS
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count >= 0:
        global timer
        timer = window.after(1000, countdown, count-1)
        print(count)
    else:
        start_timer()
        check = ""
        n = math.floor(REPS/2)
        for _ in range(n):
            check += "✔"
            label_check.config(text=check)


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Pomodoro countdown")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 112, text="00:00", fill="white", font=(FONT_NAME, 24, "bold"))
canvas.grid(row=1, column=1)


label_timer = Label(text="Timer", font=(FONT_NAME, 36, "bold"), bg=YELLOW, fg=GREEN)
label_timer.grid(row=0, column=1)


label_check = Label(text="✔", bg=YELLOW, fg=GREEN)

label_check.grid(row=3, column=1)


button = Button(text="Start", command=start_timer, highlightthickness=0)
button.grid(row=2, column=0)


button = Button(text="Reset", command=reset_timer, highlightthickness=0)
button.grid(row=2, column=2)


window.mainloop()
