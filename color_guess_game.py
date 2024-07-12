from tkinter import *
FONT="#CCD3CA"
HUNT="#535C91"

import random

color_list=["yellow","green","orange","pink","red","purple","blue","black"]
score=0
time_left=60
def startgame(play):
    if time_left==60:
        count_down()
    changeColor()

def changeColor():
    global score
    global time_left
    if time_left>0:
        entry.focus_set()
        if entry.get().lower()==color_list[1].lower():
            score+=1
    entry.delete(0,END)
    random.shuffle(color_list)
    label.config(fg=str(color_list[1]),text=str(color_list[0]))
    actual_score.config(text="score:"+str(score))

def count_down():
    global time_left
    if time_left>0:
        time_left-=1
        time_left_label.config(text="Time left:"+str(time_left))
        time_left_label.after(1000,count_down)


windows=Tk()
windows.minsize(width=700,height=400)
windows.title("Color Guessing Game")
windows.config(bg=FONT)

heading_label=Label(text="Which color?",font=("Arial",20),bg=FONT,fg=HUNT)
heading_label.pack()

actual_score=Label(text="Press enter to start the game.",font=("Arial",12),bg=FONT,fg=HUNT)
actual_score.pack()

time_left_label=Label(text="Time left:"+str(time_left),font=("Arail",14),bg=FONT,fg=HUNT)
time_left_label.pack()

# actual_score=Label(text="0")
# actual_score.pack()

label=Label(font=("Arial",25),bg="white")
label.pack()

entry=Entry(width=25,font=(7),fg="#211951")
entry.bind('<Return>',startgame)
entry.focus_set()
entry.pack()


windows.mainloop()



















