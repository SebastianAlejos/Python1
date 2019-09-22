#function
from tkinter import filedialog
#undetermined arguments

def ejemplo (x,**d):
    print(x)
    print(d)
def save(TextToSave):
    print("saving..." , TextToSave)
    location=filedialog.asksaveasfilename(title="Save File...")
    print(location)
def load():
    print("loading...")
    location=filedialog.askopenfilename(title="Open File...")
    print(location)

#ejemplo("hola")
