from tkinter import filedialog
candy=list()

def loadFile(location):
    file= open(location, "r")
    candy.clear()
    for line in file:
        cLine= line.replace("\n", "")
        candy.append(cLine)
    file.close()
loadFile("hw3_2.txt")
def add(value):
    v2= value.replace("\n","")
    print("adding: ", v2)
    candy.append(v2)

def load():
    print("loading...")
    location= filedialog.askopenfilename(title="Open File...")
    loadFile(location)

    
def save():
    print ("saving...")
    location = filedialog.asksaveasfilename(title="Save File...")
    file = open (location, "w")
    for c in candy:
        file.write(c)
        file.write("\n")
    file.close()

def printList():
    print("printing...")
    for c in candy:
        print(c)
    print("***********")
