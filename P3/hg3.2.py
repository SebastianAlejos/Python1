from tkinter import*
from hw32 import*
window = Tk()
window.title("Homework 3.2")

t= Text(window, width=50, height= 1)
t.pack()

bAdd= Button(window, text= "ADD", width =45, command=lambda: add(t.get("1.0",END)))
bAdd.pack()

bLoad= Button(window, text= "LOAD", width =45, command=lambda: load())
bLoad.pack()

bSave= Button(window, text= "SAVE", width =45, command=lambda: save())
bSave.pack()

bPrint=Button(window, text= "PRINT", width =45, command=lambda: printList())
bPrint.pack()


window.mainloop()
