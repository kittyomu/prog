from tkinter import *
from tkinter import ttk

root = Tk()
root.title('Frame Test')

framel = ttk.Frame(
  root,
  height=200,
  width=300,
  relief='sunken',
  borderwidth=5
)
framel.grid()

root.mainloop()