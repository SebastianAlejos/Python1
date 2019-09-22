#Multiplication Table
choice = "yes"
while choice == "yes": 
    number = int(input("Give me a number\n"))
    for i in range (1, 10+1 ,1):
        result= int( number * i)
        print(result)
    choice= input("Do you want to repeat process\n")
#2
else:
    for i in range (0,5):
        print("*****")
#3
x=5
for i in range(0,5):
    currentLine = ""
    for j in range(0, x):
        currentLine = currentLine + "*"
    x= x - 1
    print(currentLine);
#4
currentLine = ""
for j in range(5, 0, -1):
        currentLine = currentLine + "*"
        print(currentLine);
#5
list1 = list()
while (choice != 5):
    choice = int(input("What do you want to do: 1. Add name to list, 2. Remove a name, 3. Sort names, 4. Print names, 5. Exit\n"))
    if choice == 1:
        newName = input("What name do you want to add?\n")
        list1.append(newName)
    elif choice== 2:
        noName= input("What name do you want to remove?\n")
        list1.remove(noName)
    elif choice == 3:
        list1.sort()
        print("Sorting list...")
    elif choice == 4:
        print (list1)
        for currentElement in list1:
            print(currentElement)
        for i in range (0, len(list1)):
            print(list1[i])



        

    
    


 

        
        
        
