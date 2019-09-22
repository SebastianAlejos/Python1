list2=list()
file=open("h3_1.txt","r")
for line in file:
    clean=line.split(",")
    d1 = {"name": clean[0] , "lastName": clean[1], "invoiceId": clean[2], "invoiceTotal":clean[3]}
    list2.append(d1)
file.close()

#initials
def printInitials (list2):
    for current in list2:
        var1 = current["name"]
        var2 = current["lastName"]
        print = (var1, var2)

#save file
def saveFile (list2):
    file = open("h3_1.txt", "w")
    for current in list2:
        file.write(current["name"])
        file.write(",")
        file.write(current["lastName"])
        file.write(",")
        file.write(current["invoiceId"])
        file.write(",")
        file.write(current["invoiceTotal"])
        file.write("\n")
    file.close()

def firstThree(list2):
    result = list3[0:3]
    return result

menu = """Select one of the following choices:
1. print
2. save
3. first three
5. exit"""

choice = 0
while choiice != 4:
    print(menu)
    choice int (input ("your choice:"))

if choice==1:
    printInitials(list2)
if choice==:
    saveFile(list2)
if choice == 3:
    result= firstThree(list2)
    print(result)
    
