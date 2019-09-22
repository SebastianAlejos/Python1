from tkinter import *
from tkinter import filedialog
list1 = list()
index=0
file = open("EF.txt", "r")
for line in file:
    line2 = line.replace("\n","")
    cleanline = line2.split(",")
    d1 = {"Name":cleanline[0], "SalesS1" : cleanline[1], "SalesS2":cleanline[2]}
    list1.append(d1)        
file.close()
b=list1[index]
def loadFile (location,nameT,s1T,s2T):
    list1.clear()
    index=0
    file = open(location, "r")
    for line in file:
        line2 = line.replace("\n","")
        cleanline = line2.split(",")
        d1 = {"Name":cleanline[0], "SalesS1" : cleanline[1], "SalesS2":cleanline[2]}
        list1.append(d1)
    b=list1[index]
    canvas.create_rectangle(0,0,380,400,fill="white")
    canvas.create_rectangle(0,0,380/3,((400*int(b["SalesS1"]))/10000),fill="orange")
    canvas.create_rectangle(380/3,0,380/3*2,((400*int(b["SalesS2"]))/10000),fill="blue")
    canvas.create_rectangle(380/3*2,0,380/3*3,((400*(calculateAverage(list1))/10000)),fill="green")
    nameT.delete(1.0, END)
    nameT.insert(END, b["Name"])
    s1T.delete(1.0, END)
    s1T.insert(END, b["SalesS1"])
    s2T.delete(1.0, END)
    s2T.insert(END, b["SalesS2"])
    file.close()
def load():
    print("loading...")
    index=0
    location= filedialog.askopenfilename(title="Open File...")
    loadFile(location,nameT,s1T,s2T)
def calculateAverage (lista):
    global index
    s=lista[index]
    s1=int(s["SalesS1"])
    s2=int(s["SalesS2"])
    avg = (s1+s2)/2
    return avg
def nexts(lista,nameT,s1T,s2T):
    global index
    index=index+1
    b=list1[index]
    canvas.create_rectangle(0,0,380,400,fill="white")
    nameT.delete(1.0, END)
    nameT.insert(END, b["Name"])
    s1T.delete(1.0, END)
    s1T.insert(END, b["SalesS1"])
    s2T.delete(1.0, END)
    s2T.insert(END, b["SalesS2"])
    canvas.create_rectangle(0,0,380/3,((400*int(b["SalesS1"]))/10000),fill="orange")
    canvas.create_rectangle(380/3,0,380/3*2,((400*int(b["SalesS2"]))/10000),fill="blue")
    canvas.create_rectangle(380/3*2,0,380/3*3,((400*(calculateAverage(list1))/10000)),fill="green")
    return index
def prev(lista, nameT,s1T,s2T):
    global index
    index=index-1
    b=list1[index]
    canvas.create_rectangle(0,0,380,400,fill="white")
    nameT.delete(1.0, END)
    nameT.insert(END, b["Name"])
    s1T.delete(1.0, END)
    s1T.insert(END, b["SalesS1"])
    s2T.delete(1.0, END)
    s2T.insert(END, b["SalesS2"])
    canvas.create_rectangle(0,0,380/3,((400*int(b["SalesS1"]))/10000),fill="orange")
    canvas.create_rectangle(380/3,0,380/3*2,((400*int(b["SalesS2"]))/10000),fill="blue")
    canvas.create_rectangle(380/3*2,0,380/3*3,((400*(calculateAverage(list1))/10000)),fill="green")
    return index


window = Tk()
window.title("Final Exam")
window.geometry("380x520+100+100")

nameL = Label(window, text="Name:")
nameL.grid(row=0, column=0)

nameT = Text(window, width=20, height=1)
nameT.grid(row=0, column=1)

nameT.delete(1.0, END)
nameT.insert(END, b["Name"])

s1L = Label(window, text="Semester 1:")
s1L.grid(row=1, column=0)

s1T = Text(window, width=20, height=1)
s1T.grid(row=1, column=1)

s1T.delete(1.0, END)
s1T.insert(END, b["SalesS1"])

s2L = Label(window, text="Semester 2:")
s2L.grid(row=2, column=0)

s2T = Text(window, width=20, height=1)
s2T.grid(row=2, column=1)

s2T.delete(1.0, END)
s2T.insert(END, b["SalesS2"])

previous = Button(window, text="previous", width=20, command=lambda: prev(list1,nameT,s1T,s2T))
previous.grid(row=3, column=0)

nextB = Button(window, text="next", width=20, command=lambda: nexts(list1,nameT,s1T,s2T))
nextB.grid(row=3, column=1)

loadFile1 = Button(window, text="load file", width=44, command=lambda:load())
loadFile1.grid(row=4, column=0, columnspan=2)

canvas = Canvas(window, width=380, height=400, bg="white")
canvas.grid(row=5, column=0, columnspan=2)
canvas.create_rectangle(0,0,380/3,((400*int(b["SalesS1"]))/10000),fill="orange")
canvas.create_rectangle(380/3,0,380/3*2,((400*int(b["SalesS2"]))/10000),fill="blue")
canvas.create_rectangle(380/3*2,0,380/3*3,((400*(calculateAverage(list1))/10000)),fill="green")

window.mainloop()
