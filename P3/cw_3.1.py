#GUI
#GRAPHIC USER INTERFACE
#TKINTER

from tkinter import*
from c1 import*
window= Tk()
window.title("Salu2")

#widget
l1 = Label(window, text= "Hey guys whatsup")
l1.pack()                       

t1= Text(window, height=2)
t1.pack()

b2 = Button(window, text= "load", command =load)
b2.pack()

b2 = Button(window, text= "save", command= lambda:save(t1.get("1.0",END)))
b2.pack()



window.mainloop()#detectar interacción



