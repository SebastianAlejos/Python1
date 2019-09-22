names = list()
ages = list()
majors = list()
p1s = list()
p2s = list()
finals = list()

def calculateGrade (p1, p2, fe):
    finalGrade = (p1*.3) + (p2*.3) + (finalExam*.4)
    return finalGrade

def findMajor (nameList, mayorList, name):
    for i in range (0, len(nameList)):
        if (nameList[i]== name):
            return majorList[i]
    return "not found"        
#file modes
#r- read
#w- write
#a- append
file = open("hw2_2.txt", "r")

for line in file:
    line2 = line.replace ("\n" , "")
    lineList = line2.split(",")
    names.append(lineList[0])
    ages.append(int(lineList[1]))
    majors.append(lineList[2])
    p1s.append(float(lineList[3]))
    p2s.append(float(lineList[4]))
    finals.append(float(lineList[5]))
file.close()

choice=0
while choice!=10:
    print("Choose one of the following")
    print("1. Add student")
    print("2. Delete student")
    print("3. Calculate grade")
    print("4. Find student major")
    print("5.Get best final exam")
    print("6. Get worst final exam")
    print("7. Print students")
    print("Reload file")
    print("Save file")
    print("Exit")
    choice= int(input("Your choice: "))

    if (choice == 1):
        name = input("Give me a name")
        age = input(int("Give me an age"))
        major = input("Give me a major")
        p1 = float(input("Give me p1: "))
        p2 = float(input("Give me p2: "))
        final = float(input("Give me final: "))

        names.append(name)
        ages.append(age)
        majors.append(major)
        p1s.append(p1)
        p2s.append(p2)
        finals.append(final)

    if (choice == 2):
        location = int(input("Give me a location:"))
        del(names[location])
        del(ages[location])
        del(majors[location])
        del(p1s[location])
        del(p2s[location])
        del(finals[location])

    if (choice == 3):
        location = int(input("Give me a location:"))

        grade = calculateGrade(p1s[location], p2s[location], finals[location])
        print ("The grade is: ", finalGrade)

    if (choice == 4):
        name= input("Give me a name")
        major = findMajor(names, majors, name)
        print("The major is: ")

    if (choice == 5):
        best = finals[0]

        for currentGrade in finals:
            if (currentGrade > best):
                best = currentGrade
        print("The best exam is: ", best)
            

    if (choice == 7) :
        for i in range(0, len(names)):
            print(names[i], ages[i], majors[i], p1s[i], p2s[i], finals[i])
        
         
                       
                   
        
