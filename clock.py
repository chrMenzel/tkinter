from tkinter import *
import time

master = Tk()
clock = Label(master, font=("Arial", 30), bg = "black", fg = "yellow")
clock.pack(fill = BOTH)

def ticking():
    current_time = time.strftime("%H:%M:%S")
    clock.configure(text = current_time)
    clock.after(1000, ticking)

ticking()

master.mainloop()