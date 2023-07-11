from tkinter import *

root = Tk()

# ---------- display text with grid ----------
# myLabel = Label(root, text="Hello World!")
# myLabel.grid(row=0, column=0)

# myLabelGrid = Label(root, text="I don't have a name")
# myLabelGrid.grid(row=1, column=0)

myButton = Button(root, text="Click Me!")
myButton.pack()

root.mainloop()