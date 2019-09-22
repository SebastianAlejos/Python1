import math
#1
    #a
def cylinderVol (radius, height):
    cVol = math.pi *radius**2* height
    return cVol
    #b
def sphereVol (radius):
    sVol= 4/3*math.pi*radius**3
    return sVol
    #C
def prismVol (side1, side2, height):
    pVol= side1*side2*height
    return pVol
#2
    #a
repeat= "yes"
count = 0
while repeat=="yes":
    count= count+1
    figure = int(input("Choose one of the following figures: 1. Cylinder, 2. Sphere, 3. Rectangular prism\n"))
    if figure == 1:
        radius = float(input("What's the radius of the cylinder\n"))
        height = float(input("What's the height of the cylinder\n"))
        result = cylinderVol (radius, height)
        print("The volume is: ", result)
    elif figure == 2:
        radius = float(input("What's the radius of the sphere\n"))
        result = sphereVol (radius)
        print("The volume is:", result)
    elif figure== 3:
        side1 = float(input("What's the lenght of the first side of the prism?\n"))
        side2 = float(input("What's the lenght of the second side of the prism?\n"))
        height = float(input("What's the height of the prism?\n"))
        result = prismVol (side1, side2, height)
        print("The volume is:", result)
    else:
        print ("Error, number not supported")
        repeat = "no"
    repeat= input("Do you want to repeat the process?\n")
oddOrEven = count % 2
if oddOrEven == 0:
    print("You requested a volume an even amount of times")
else:
     print("You requested a volume an odd amount of times")
            
        
     
