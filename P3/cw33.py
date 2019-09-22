from tkinter import*

window= Tk()
window.title("Class 33")
window.geometry("500x500+50+50")

l1 = Label(window, text= "label 1", bg="red", width=50)
l1.grid(row=0, column=0)

l2 = Label(window, text= "label 2", bg="blue")
l2.grid(row=0, column=1)


l3 = Label(window, text= "label 3", bg="yellow")
l3.grid(row=0, column=2)

l4 = Text(window, height=1, width=5)
l4.grid(row=1, column=1)

# option menu

options = ["A", "B", "C"]
choice= StringVar()
choice.set(options[0])

om =OptionMenu(window, choice, *options)
om.config(width=50)
om.grid(row=2, column=0, columnspan=2)

c= Canvas(window, height=400, width=400, bg="black")
c.grid(row=3, column=0, columnspan=3)
c.create_oval(10,10, 20,20, fill="red")
c.create_line(40,40,60,60, fill="green")
c.create_rectangle(100,100,150,150,fill="orange")
window.mainloop()
