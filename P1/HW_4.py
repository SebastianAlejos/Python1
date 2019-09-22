numStudents = int(input("How many students do you have\n"))
grades=0
for i in range(0, numStudents, 1):
    grade=float(input("What´s the grade?\n"))
    grades= grades + grade
    avg= grades / (i+1)
print("Your average is: ", avg)
    
