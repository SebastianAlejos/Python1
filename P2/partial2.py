nameList=list()
lastnames= list()
salaryList=list()
list3=list()
file = open ("partial2.txt", "r")
for line in file:
    line2 = line.replace ("\n" , "")
    lineList = line2.split(",")
    nameList.append(lineList[0])
    lastnames.append(lineList[1])
    salaryList.append(int(lineList[2]))
file.close()
def findSalary (nameList, salaryList, name):
    index=0
    for i in range (0, len(nameList)):
        if name == nameList[i]:
            index = i
    return salaryList[index]

def average (salaryList):
    summ= 0
    count=0
    for i in range(0,len(salaryList)):
        count= count+1
        summ= summ + salaryList[i]
        avg= summ/count
    return avg

def lowestSalary (salaryList):
    lowest= salaryList[0]
    for currentSalary in salaryList:
        if (currentSalary < lowest):
            lowest= currentSalary
    return lowest

choice= 0
while choice !=8:
    print("Choose one of the following")
    print("1. Print records")
    print("2. Add rcord")
    print("3. Save record")
    print("4. Reverse list")
    print("5. Find record")
    print("6. Average")
    print("7. Lowest salary")
    print("8. Exit")
    choice= int(input("Your choice: "))

    if choice == 1:
        for i in range (0, len(nameList)):
            print(nameList[i], lastnames[i], salaryList[i])

    elif choice ==2:
        name1 = input("Give me the name")
        lastname1 = input("Give me the last name")
        salary = input("Give me the salary")
        nameList.append(name1)
        lastnames.append(lastname1)
        salaryList.append(salary)

    elif choice==3:
        file = open ("partial2.txt", "w")
        for i in nameList:
            file.write(i)
            file.write(",")
        for i in lastnames:
            file.write(i)
            file.write(",")
        for i in salaryList:
            file.write(str(i))
            file.write("\n")

    elif choice ==4:
        reverseName=list()
        reverseLastName=list()
        reverseSalary= list()
        for i in range (len(nameList)-1,-1,-1):
            reverseName.append(names[i])
            reverseLastName.append(lastnames[i])
            reverseSalary.append(salaryList[i])
        nameList=reverseName
        lastnames= reverseLastName
        salaryList=reverseSalay
    elif choice==5:
        name=input("Give me a name")
        record =findSalary(nameList, salaryList, name)
        print(record)
    elif choice==6:
        prom= average(salaryList)
        print(prom)
    elif choice==7:
        low= lowestSalary(salaryList)
        print(low)
        
