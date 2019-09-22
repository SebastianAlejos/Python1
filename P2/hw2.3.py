names = list()
def loadFile():
    names.clear()
    file= open ("hw2_3.txt", "r")
    for line in file:
        line2 = line.replace ("\n" , "")
        names.append(line2)
    file.close()
loadFile()
choice=0
while (choice != 7):
    print("Choose one of the following")
    print("1. Print names")
    print("2. Add a name")
    print("3. Delete a name")
    print("4. Sort name")
    print("5. Reload file")
    print("6. Save file")
    print("7. Exit")
    choice= int(input("Your choice: "))

    if choice == 1:
        for currentName in names:
            print(currentName)

    if choice== 2:
        name = input("Give me a name\n")
        names.append(name)

    if choice== 3:
        name = input("Give me a name to remove\n")
        names.remove(name)

    if choice==4:
        names.sort()

    if choice == 5:
        loadFile()

    if choice==6:
        file= open ("hw2_3.txt", "w")
        for i in names:
            file.write(i)
            file.write("\n")
        file.close()
    if choice==7:
        print("Bye")
        
        
        
        
        
        
