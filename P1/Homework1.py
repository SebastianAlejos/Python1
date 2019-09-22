import math
#1
userName = input("What is your name?\n")
userLastName = input ("What is your last name?\n")
print ("Hello "+ str(userName) + " " + str(userLastName))
#2
userInput= input ("Give me one of the sides of the rectangle\n")
userInput2= input ("Give me the other side of the rectangle\n")
area= float(userInput)*float(userInput2)
print("The area of the rectangle is: " + str(area))
#3
userInput= input ("Give me the base of the triangle\n")
userInput2= input ("Give me the height of the triangle\n")
area= ((float(userInput)*float(userInput2))/2)
print("The area of the triangle is: "+str(area))
#4
userInput= input ("Give me the radius of the cirle\n")
area= (math.pi*(float(userInput))**(2))
print("The area of the circle is: "+str(area))
#5
userInput= input ("Give me the radius of the cirle\n")
perimeter= (float(userInput)*(2)*(math.pi))
print("The perimeter of the circle is: "+str(perimeter))
#6
userInput= input ("Give me the price of the car\n")
userInput2= input ("Give me the monthly interest rate\n")
userInput3= input ("Give me the number of months\n")
price= float(userInput)*float(userInput2)*float(userInput3)
print("The price is: " +str(price))
#7
userInput= input ("Give me the angle in radians\n")
userInput2= input ("Give me the lenght of the adjacent leg\n")
adjLeg= math.cos(float(userInput))*float(userInput2)
print( "The size of the opposite leg is: " +str (adjLeg))
#8
userInput= input ("Give me the mass of the object\n")
force= float(userInput)*9.81
print( "The gravitational force applied to that object is: " +str (force))

