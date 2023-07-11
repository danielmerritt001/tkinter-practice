from tkinter import *

root = Tk()

# ---------- display text with grid ----------
# myLabel = Label(root, text="Hello World!")
# myLabel.grid(row=0, column=0)

# myLabelGrid = Label(root, text="I don't have a name")
# myLabelGrid.grid(row=1, column=0)


e = Entry(root, width=50, bg="black", fg="white")
e.pack()
e.insert(0, "Enter Your Name")

def myClick():
    hello = "Hello " + e.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()

myButton = Button(root, text="Enter Your Name", command=myClick)
myButton.pack()

root.mainloop()