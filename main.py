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
start_active = False

window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Tomato canvas
tomato_img = PhotoImage(file="./tomato.png") #this step is needed to convert any picture to image
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
canvas.create_image(100,112,image=tomato_img)
timer_text = canvas.create_text(103,130,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row = 2,column=2)

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
   global reps
   global start_active
   window.after_cancel(timer)
   label.config(text="Timer",fg=GREEN)
   check_label.config(text="")
   canvas.itemconfig(timer_text, text="00:00")
   start_active = False
   reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
   global reps
   count_minutes = math.floor(count/60)
   if count_minutes < 10:
      count_minutes_text = f"0{count_minutes}"
   else:
      count_minutes_text = count_minutes
   count_seconds = int(count%60)
   if count_seconds < 10:
      count_seconds_text = f"0{count_seconds}"
   else:
      count_seconds_text = count_seconds

   count_text = f"{count_minutes_text}:{count_seconds_text}"
   canvas.itemconfig(timer_text, text=count_text)
   if count > 0:
      global timer
      timer = window.after(1000,count_down, count - 1)
   elif count == 0:
      start_timer()
      marks = ""
      work_sessions = math.floor(reps/2)
      for _ in range(work_sessions):
         marks += "✓"
      check_label.config(text=marks)

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
   global reps
   global start_active
   if start_active == False:
      start_active = True
      work_secs = WORK_MIN*60
      short_break_secs = SHORT_BREAK_MIN*60
      long_break_secs = LONG_BREAK_MIN*60

      reps += 1
      if reps %2 != 0:
         label.config(text="Work",fg=GREEN)
         count_down(work_secs)
      elif reps % 8 == 0:
         label.config(text="Break",fg=RED)
         count_down(long_break_secs)
      elif reps % 2 == 0:
         label.config(text="Break",fg=PINK)
         count_down(short_break_secs) 

# ---------------------------- UI SETUP ------------------------------- #


#Timer label
label = Label(text="Timer",font=(FONT_NAME,45,"normal"),bg=YELLOW,fg=GREEN)
label.grid(row = 0,column = 2)

#Button Start
start_button = Button(text="Start",command=start_timer,bg=YELLOW,highlightthickness=0)
start_button.grid(row = 3, column = 1)

#Button Stop
reset_button = Button(text="Reset",command=reset_timer,bg=YELLOW,highlightthickness=0)
reset_button.grid(row = 3, column = 3)

#check label
check_label = Label(text="",font=(FONT_NAME,35,"normal"),bg=YELLOW,fg=GREEN)
check_label.grid(row = 4, column = 2)

window.mainloop()