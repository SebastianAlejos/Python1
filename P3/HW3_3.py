from tkinter import *

from HW333CODE import *
window =Tk()
window.title("HW33")
window.geometry("500x500+50+100")

testX0 = Text(window, width=25, height=1)
textX0.grid(row=0, column = 1)

testY0 = Text(window, width=25, height=1)
textY0.grid(row=0, column = 1)

testX1 = Text(window, width=25, height=1)
textX1.grid(row=0, column = 1)

testY1 = Text(window, width=25, height=1)
textY1.grid(row=0, column = 1)

options= ["line", "rectangle", "oval"]
choice = StringVar()
choice.set(options[0])
manu = OptionMenu(window, choice, *options)
menu.config(width=50)
menu.grid(row=2, colum=0, columspan=2)

b = Button(window, text="draw", width =50, command=lambda:draw(textX0, textY0, textX1, textY1, choice, c))
b.grid(row=3, column=0, columnspan=2)

c =Canvas(window, height=370, width=420, bg="grey")
c.grid(row=4, column=0, columnspan=2)

window.mainloop()
