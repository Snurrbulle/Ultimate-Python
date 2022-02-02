import sys
import time
import datetime

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

def say(it):
    print(it)
