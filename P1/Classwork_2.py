#1
print("Factorial")
num = int(input("Enter a number: \n"))
factorial= 1
for i in range(1,num + 1):
    factorial = factorial*i
print("The factorial of",num,"is",factorial,"\n")

#2
print("Summation")
sums=0
lowRange = int(input("Give me the lower number: \n"))
upRange = int(input("Give me the higher number: \n"))
for i in range(lowRange, upRange+1, 1):
    sums= sums + i 
print ("The summation of the range is: ", sums,"\n")

#3
print("Even numbers")
lowRange = int(input("Give me the lower number: \n"))
upRange = int(input("Give me the higher number: \n"))
for i in range(lowRange, upRange+1, 1):
    if (i % 2)== 0:
        print (i)
print("\n")

#4
print("Sum of odd numbers")
sums=0
lowRange = int(input("Give me the lower number: \n"))
upRange = int(input("Give me the higher number: \n"))
for i in range(lowRange, upRange+1, 1):
    if (i % 2)== 1:
        sums= sums + i 
print ("The summation of the range is: ", sums,"\n")

#5
print("Sum of even numbers")
sums=0
lowRange = int(input("Give me the lower number: \n"))
upRange = int(input("Give me the higher number: \n"))
for i in range(lowRange, upRange+1, 1):
    if (i % 2)== 0:
        sums= sums + i 
print ("The summation of the range is: ", sums,"\n")

#6
print("100-1")
for i in range(100, 0,-1):
    print(i)
print("\n")

#7
print("Power of a number")
num = int(input("Give me the number: \n"))
power = int(input("Give me the power: \n"))
result= 1
for i in range(1, power+1, 1):
    result= (result*num)
print("The result is: ", result,"\n")

#8
print("Prime numbers")
number = int(input("Give me a number: \n"))
track=0
for i in range (2, number):
    if (number % i ==0):
        track = track +1
if (track > 0):
    print("Not prime")
else:
    print("Prime")
#9
print("Fibonacci sequence")
number = int(input("How many terms: \n"))
lastTerm=0
currentTerm=1
for i in range (0, number):
    print (lastTerm)
    temp = currentTerm
    currentTerm=lastTerm+currentTerm
    lastTerm=temp
#10
number = int (input("Give me a number: \n"))
for i in range (1, number) :
    current = 1/i
    print(current)


    

