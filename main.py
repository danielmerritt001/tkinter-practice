from tkinter import *

root = Tk()

myLabel = Label(root, text="Hello World!")
myLabel.grid(row=0, column=0)

myLabelGrid = Label(root, text="I don't have a name")
myLabelGrid.grid(row=1, column=0)

root.mainloop()