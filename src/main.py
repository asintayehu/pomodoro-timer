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

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    if reps % 2 == 0 and reps != 8:
        countdown(short_break_sec)
    elif reps == 8:
        countdown(long_break_sec)
    else:
        countdown(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds == 0:
        seconds = "00"
    elif seconds < 10:
        seconds = f"0{seconds}"
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        window.after(1000, countdown, count-1)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.minsize(width=200, height=224)
window.config(padx=100, pady=50, bg=YELLOW)
fg = GREEN
# 🗸🗸🗸🗸🗸
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_picture = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_picture)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)


welcome_txt = Label()
welcome_txt.grid(row=0, column=1)
welcome_txt.config(text="TIMER", bg=YELLOW,  fg=GREEN, font=(FONT_NAME, 50))

btn_start = Button()
btn_start.config(text="Start", width=8, command=start_timer)
btn_start.grid(row=2, column=0)

btn_reset = Button()
btn_reset.config(text="Reset", width=8)
btn_reset.grid(row=2, column=2)

check_label = Label()
check_label.config(text="🗸", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 25))
check_label.grid(row=3, column=1)

window.mainloop()
