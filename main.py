from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"

FONT_NAME = "Courier"
# WORK_MIN = 25
WORK_MIN = 1 # while testing make it 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timer = 0
# ---------------------------- TIMER RESET ------------------------------- # step 4
def reset_timer():
    window.after_cancel()


# ---------------------------- TIMER MECHANISM ------------------------------- # step 3
def start_timer():
    # countdown(5)
    global reps
    reps += 1

    word_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # if it's 8th rep'
    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Break", fg=RED)
    # if it's' 2nd/4th/6th rep
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Break", fg=PINK)
    # if it's 1st/3rd/5th/7th' rep:
    else:
        countdown(word_sec)
        timer_label.config(text="Work", fg=GREEN)

    # countdown(2*60)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # step 2
import time
import math
# learn about an tkinter widget after()
# and add it in window
# def say_something(thing):
#     print(thing)
# window.after(1000, say_something, "hello")

def countdown(count):
    # print(count)
    # add math lib
    count_min = math.floor(count/60)
    count_sec = count % 60 # using this only will give u 5:0 only if u want 5:00 use dynamic typing
    # In dynamic typing we have to assign count_sec "00" string data later it ll assigned int data
    # Python is only language that can do this
    # c, c++, java swift no one have this feature

    # if count_sec == 0:
    #     count_sec = "00"
    if count_sec < 10:
       count_sec = (f"0{count_sec}")

    # canvas.itemconfig(timer_text, text=count) # After making this call the countdown below canvas.grid
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}") # After making this call the countdown below canvas.grid
    if count > 0:
        window.after(1000, countdown, count - 1)
    else:
        start_timer()
        # After completing the break and work we need to add check mark after every two reps
        mark = ""
        work_sessions = math.floor(reps/2)
        for i in range(work_sessions):
            mark += "✔️"
        check_text.config(text=mark, fg=GREEN)
# Now assign the timer text to canvas where canvas is created a text 00:00


# ---------------------------- UI SETUP ------------------------------- # Step 1

window  = Tk()
window.title("Pomodoro")
window.config(padx=100 ,pady=50, bg=YELLOW) # do this after adding the image

# countdown(5) # It ll generate a timer clock


# Adding the label after canvas
timer_label = Label(text="Timer",bg=YELLOW, fg=GREEN ,font=(FONT_NAME, 50))
timer_label.grid(column=1, row=0)

# ---------Canvas-----------
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0) #If u want to find perfect size see the image details
# canvas.create_image(100,112, image=#here you can't directly put the name of image)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100,112, image=tomato_img)
# canvas.create_text(100,112, text="00:00")
# canvas.create_text(103,130, text="00:00", fill='white',font=(FONT_NAME, 35,"bold")) # Go to color hunt
# canvas.create_text(100,130, text="00:00", fill='white',font=(FONT_NAME, 35,"bold")) # Go to color hunt
timer_text = canvas.create_text(100,130, text="00:00", fill='white',font=(FONT_NAME, 35,"bold")) # Go to color hunt
# https://colorhunt.co/
# After adding the colors add bg and highlightthickness and make 103 to 100 on both place

# canvas.pack()
canvas.grid(column=1, row=1)
# countdown(5)

# Challenge--------------------

# add Timer
# add button
# add check mark



# Now we are adding the buttons after timer
# start_button = Button(text='Start', highlightthickness=0)
start_button = Button(text='Start', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text='Reset', highlightthickness=0)
reset_button.grid(column=2, row=2)

# Adding check mark
check_text = Label(text="", fg=GREEN, bg=YELLOW)
check_text.grid(column=1, row=3)


window.mainloop()