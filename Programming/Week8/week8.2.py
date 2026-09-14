import tkinter as tk
from tkinter import ttk

from week8 import *

root = tk.Tk()
name_box = ttk.Entry(root)
name_box.pack()

def onBook():
    name = name_box.get()
    print(name) 