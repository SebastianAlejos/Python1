grades= list()
grades.clear()
file= open ("hw2_4.txt", "r")
for line in file:
    line2 = line.split (",")
    for grade in line2:
        grades.append(float(grade))
file.close()

def average(grades):
    count=0
    sums=0
    for currentGrade in grades:
        count=count+1
        sums= sums+ currentGrade
        average= sums/count
    return average

def getBest(grades):
    best = grades[0]
    for currentGrade in grades:
        if (currentGrade > best):
            best = currentGrade
    return best

def getWorst(grades):
    worst = grades[0]
    for currentGrade in grades:
        if (currentGrade < worst):
            worst = currentGrade
    return worst

def studFail(grades):
    count=0
    for currentGrade in grades:
        if (currentGrade < 70):
            count= count+1
    return count

def studPass(grades):
    count=0
    for currentGrade in grades:
        if (currentGrade >= 70):
            count= count+1
    return count
            
choice=0
while choice!=7:
    print("Choose one of the following")
    print("1. Print grades")
    print("2. Calculate average")
    print("3. Get best")
    print("4. Get worst")
    print("5. Students who failed")
    print("6. Students who passed")
    print("7. Exit")
    choice= int(input("Your choice: "))

    if choice==1:
        print(grades)

    if choice==2:
        avg = average(grades)
        print("The average is: ", avg)

    if choice==3:
        grades = grades
        bestGrade = getBest(grades)
        print("The best grade is: ", bestGrade)

    if choice==4:
        grades = grades
        worstGrade = getWorst(grades)
        print("The worst grade is: ", worstGrade)

    if choice==5:
        grades=grades
        fail= studFail(grades)
        print("The number of student who failed is: ", fail)

    if choice==6:
        grades=grades
        passed = studPass(grades)
        print("The number of student who failed is: ", passed)

    if choice == 7:
        print("Bye")
