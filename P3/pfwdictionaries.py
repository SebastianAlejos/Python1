
#Ivonne Medina
#Sebastian Alejos 

animalitoslist = list()
dictanimalitos = list()
fileanimalitos = open("pf.txt", "r")
for line in fileanimalitos:
    lineanimalitos = line.replace("\n","")
    cleananimalitos = lineanimalitos.split(",")
    print(cleananimalitos)
    diccomplete = {"Nombre comun":cleananimalitos[0], "Nombre cientifico" : cleananimalitos[1], "Reino":cleananimalitos[2], "Filo": cleananimalitos[3], "Clase": cleananimalitos[4], "Orden": cleananimalitos[5], "Familia":cleananimalitos[6]}
    animalitoslist.append(diccomplete)
    
def load (location):
    animalitoslist.clear()
    file = open (location, "r")
    for line in file:
        lineanimalitos = line.replace("\n","")
        cleananimalitos = lineanimalitos.split(",")
        diccomplete = {"Nombre comun":cleananimalitos[0], "Nombre cientifico" : cleananimalitos[1], "Reino":cleananimalitos[2], "Filo": cleananimalitos[3], "Clase": cleananimalitos[4], "Orden": cleananimalitos[5], "Familia":cleananimalitos[6]}
        animalitoslist.append(diccomplete)
    file.close()

def findcientifico(animalitoslist, comunName):
    for name in animalitoslist:
        animalitoR = name["Nombre cientifico"]
        if(comunName == name["Nombre comun"]):
            return animalitoR
    else:
        return "not found"

def eliminar (index):
    del(animalitoslist[index])
    return print("deleting...")

def newName(common, cientific, reino, filo, clase, order, family):
    dictnewanimal = {"Nombre comun": common, "Nombre cientifico": cientific, "Reino": reino, "Filo": filo, "Clase": clase, "Orden": order, "Familia": family} 
    animalitoslist.append(dictnewanimal)
    return("adding...")

def saveFile (list1):
    file = open("pf.txt", "w")
    for current in list1:
        file.write(current["Nombre comun"])
        file.write(",")
        file.write(current["Nombre cientifico"])
        file.write(",")
        file.write(current["Reino"])
        file.write(",")
        file.write(current["Filo"])
        file.write(",")
        file.write(current["Clase"])
        file.write(",")
        file.write(current["Orden"])
        file.write(",")
        file.write(current["Familia"])
        file.write("\n")
    file.close()

        
choice=0
while choice!=7:
    print(""" Choose one of the following:
1. print names
2. find scientific name
3. delete record
4. add record
5. load file
6. save file
7. exit""")
    choice= int(input("Your choice:"))
    if choice ==1:
        for current in animalitoslist:
            var1=current["Nombre comun"]
            var2=current["Nombre cientifico"]
            var3=current["Reino"]
            var4=current["Filo"]
            var5=current["Clase"]
            var6=current["Orden"]
            var7=current["Familia"]
            print(var1,",",var2,",",var3,",",var4,",",var5,",",var6,",",var7)
            
    if choice==2:
        name= input("Give me a common name \n")
        y=findcientifico(animalitoslist,  name)
        print(y)

    if choice==3:
        index= int(input("Give me an index:"))
        y= eliminar(index)
        print(y)
    if choice==4:
        a=input("Give me the common name:")
        b=input("Give me the scientific name:")
        c=input("Gime me the reign name")
        d=input("Give me the filo name:")
        e=input("Give me the class name:")
        f=input("Give me the order name:")
        g=input("Give me the family name:")
        y= newName(a, b, c, d ,e ,f, g)
        print(y)
    if choice==5:
        load("pf.txt")
    if choice==6:
        saveFile(animalitoslist)


                  
