from tkinter import *

window = Tk()
window.geometry('760x670')
window.title("Calculator")

# Field

input_field = Entry(window,
                    width=40,
                    font=('large_font', 30))
input_field.grid(column=0, columnspan=4, row=0)

# Commands for buttons :-

def input_clr():
    input_field.delete(0, END)

def input_equals():
    global values
    values = str(input_field.get())
    result = str(eval(values))
    input_field.delete(0, END)
    input_field.insert(END, result)

def input_pad_1():
    input_field.insert(END, 1)
def input_pad_2():
    input_field.insert(END, 2)
def input_pad_3():
    input_field.insert(END, 3)

def input_pad_4():
    input_field.insert(END, 4)
def input_pad_5():
    input_field.insert(END, 5)
def input_pad_6():
    input_field.insert(END, 6)

def input_pad_7():
    input_field.insert(END, 7)
def input_pad_8():
    input_field.insert(END, 8)
def input_pad_9():
    input_field.insert(END, 9)

def input_pad_0():
    input_field.insert(END, 0)

def input_pad_add():
    input_field.insert(END, '+')
def input_pad_sub():
    input_field.insert(END, '-')
def input_pad_mul():
    input_field.insert(END, '*')

def input_pad_div():
    input_field.insert(END, '/')
def input_pad_mod():
    input_field.insert(END, '%')
def input_pad_dec():
    input_field.insert(END, ".")

# Buttons 0-9

pad_1 = Button(window, text="1", width=20, height=10, command=input_pad_1)
pad_2 = Button(window, text="2", width=20, height=10, command=input_pad_2)
pad_3 = Button(window, text="3", width=20, height=10, command=input_pad_3)

pad_4 = Button(window, text="4", width=20, height=10, command=input_pad_4)
pad_5 = Button(window, text="5", width=20, height=10, command=input_pad_5)
pad_6 = Button(window, text="6", width=20, height=10, command=input_pad_6)

pad_7 = Button(window, text="7", width=20, height=10, command=input_pad_7)
pad_8 = Button(window, text="8", width=20, height=10, command=input_pad_8)
pad_9 = Button(window, text="9", width=20, height=10, command=input_pad_9)

pad_0 = Button(window, text="0", width=20, height=10, command=input_pad_0)

# Buttons : Operators etc.

add_btn = Button(window, text="+", width=20, height=10, command=input_pad_add)
subtract_btn = Button(window, text="-", width=20, height=10, command=input_pad_sub)
divide_btn = Button(window, text="/", width=20, height=10, command=input_pad_div)
modulus_btn = Button(window, text="%", width=20, height=10, command=input_pad_mod)
multiply_btn = Button(window, text="X", width=20, height=10, command=input_pad_mul)
decimal_btn = Button(window, text=".", width=20, height=10, command=input_pad_dec)
equals_btn = Button(window, text="=", width=40, height=10, command=input_equals)
clear_btn = Button(window, text="C", width=20, height=10, command=input_clr)

# Placing the buttons in the grid :-

pad_1.grid(column=0, row=1)
pad_2.grid(column=1, row=1)
pad_3.grid(column=2, row=1)

pad_4.grid(column=0, row=2)
pad_5.grid(column=1, row=2)
pad_6.grid(column=2, row=2)

pad_7.grid(column=0, row=3)
pad_8.grid(column=1, row=3)
pad_9.grid(column=2, row=3)

pad_0.grid(column=1, row=4)

add_btn.grid(column=3, row=1)
subtract_btn.grid(column=3, row=2)
divide_btn.grid(column=3, row=3)
multiply_btn.grid(column=2, row=4)
decimal_btn.grid(column=0, row=4)
modulus_btn.grid(column=3, row=4)
equals_btn.grid(column=1, columnspan=2, row=5)
clear_btn.grid(column=0, row=5)

input_field.focus()

window.mainloop()