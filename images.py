from tkinter import *
from PIL import ImageTk, Image


root = Tk()

root.title('Image tkinter training')
root.iconbitmap('c:/Users/danielmerritt/code/sei/sandbox/tkinter-practice/icon.ico')

button_quit = Button(root, text="Exit Program", command=root.quit)
button_quit.pack()

root.mainloop()