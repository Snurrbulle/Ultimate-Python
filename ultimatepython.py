import sys
import time
import datetime
import tkinter

class WError(Exception):
    def __init__(self, errno, msg):
        super().__init__(f"[Errno {errno}]: {msg}")

def hello_world():
    print("Hello world!")

def exit():
    sys.exit()

def time(time):
    if time == "now" or time == 0:
        return datetime.datetime.now()
    else:
        raise WError(1, "[That is actually a bad time.")
def pause(time):
    time.sleep(time)

def say(it, time=0):
    print(it)
    pause(time)

def open_window(title="My window", width1=100, height1=100, ):
    window = tkinter.Tk(title)
    window.configure(width=width1, height=height1)
    window.configure(bg=background)
    window.mainloop()

def ask(it, time=0):
    say(it, time)
    answear = input(" ")
    return answear
