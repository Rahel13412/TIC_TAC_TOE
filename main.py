import tkinter
import random

choice = ['X', 'Y']


def button_function():
    pass


screen = tkinter.Tk()

canvas = tkinter.Canvas(width=500, height=500)

button_1 = tkinter.Button(width=3, background="powderblue", highlightthickness=0, command=button_function)
button_1.grid(row=0, column=0)

button_2 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_2.grid(row=0, column=1)

button_3 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_3.grid(row=0, column=2)

button_4 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_4.grid(row=1, column=0)

button_5 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_5.grid(row=1, column=1)

button_6 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_6.grid(row=1, column=2)

button_7 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_7.grid(row=2, column=0)

button_8 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_8.grid(row=2, column=1)

button_9 = tkinter.Button(width=3, background="powderblue", highlightthickness=0)
button_9.grid(row=2, column=2)
screen.mainloop()
