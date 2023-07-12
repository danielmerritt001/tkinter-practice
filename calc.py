from tkinter import *

root = Tk()
root.title("Simple Calculator")

e = Entry(root, width=35, borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

def button_click(num):
  current = e.get()
  e.delete(0, END)
  e.insert(0, str(current) + str(num))

def button_delete():
  e.delete(0, END)

def button_addition():
  first_num = e.get()
  global f_num
  global operator
  operator = "addition"
  f_num = int(first_num)
  print(f_num)
  e.delete(0, END)
  
def button_minus():
  first_num = e.get()
  global f_num
  global operator
  operator = "subtraction"
  f_num = int(first_num)
  e.delete(0, END)

def button_mult():
  first_num = e.get()
  global f_num
  global operator
  operator = "multiplication"
  f_num = int(first_num)
  e.delete(0, END)

def button_div():
  first_num = e.get()
  global f_num
  global operator
  operator = "division"
  f_num = int(first_num)
  e.delete(0, END)

def button_equation():
  second_numb = e.get()
  e.delete(0, END)
  if operator == "addition":
    e.insert(0, f_num + int(second_numb))
  if operator == "subtraction":
    e.insert(0, f_num - int(second_numb))
  if operator == "multiplication":
    e.insert(0, f_num * int(second_numb))
  if operator == "division":
    e.insert(0, f_num / int(second_numb))


button_1= Button(root, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_1.grid(row=1,column=0)
button_2= Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_2.grid(row=1,column=1)
button_3= Button(root, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_3.grid(row=1,column=2)
button_4= Button(root, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_4.grid(row=2,column=0)
button_5= Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_5.grid(row=2,column=1)
button_6= Button(root, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_6.grid(row=2,column=2)
button_7= Button(root, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_7.grid(row=3,column=0)
button_8= Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_8.grid(row=3,column=1)
button_9= Button(root, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_9.grid(row=3,column=2)
button_0= Button(root, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_0.grid(row=4,column=0)
button_add= Button(root, text="+", padx=39, pady=20, command= button_addition)
button_add.grid(row=5,column=0)
button_equal= Button(root, text="=", padx=91, pady=20, command=button_equation)
button_equal.grid(row=4,column=1, columnspan=2)
button_clear= Button(root, text="Clear", padx=79, pady=20, command=button_delete)
button_clear.grid(row=5,column=1, columnspan=2)
button_subtract= Button(root, text="-", padx=40, pady=20, command=button_minus)
button_subtract.grid(row=6,column=0)
button_multiply= Button(root, text="*", padx=40, pady=20, command=button_mult)
button_multiply.grid(row=6,column=1)
button_divide= Button(root, text="/", padx=40, pady=20, command=button_div)
button_divide.grid(row=6,column=2)




root.mainloop()