import time
import tkinter as tk
from tkinter import *


def wait():
    for i in range(10):
        print(i)
        time.sleep(1)


root = tk.Tk()


def start():
    graph_window = Toplevel()
    yes_label = Label(graph_window, text="window showed up")
    yes_label.pack()
    wait()

    #  the graph_window won't show up until the countdown to 10 is finished.


start = Button(text="start", command=start)
start.pack()


root.mainloop()