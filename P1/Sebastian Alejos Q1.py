import math
def volCylinder (radius, height):
    return float(math.pi * radius ** (2) * height)

def volPyramid (baseLength, baseWidth, height):
    return float((baseLength*baseWidth*height)/3)

def volSphere (radius):
    return float(4/3*math.pi*radius**3)

mainChoice = int(input("What geometric figure do you need the volume for: 1.Cylinder, 2.Pyramid or 3.Sphere?\n"))

if mainChoice == 1:
    radius = float(input ("What´s the radius of the base?\n"))
    height = float(input ("What´s the height of the cylinder?\n")) 
    result = float(volCylinder (radius, height))
    print ("The volume is: " + str(result))
elif mainChoice ==2:
    baseLength = float(input("What´s the base lenght of the pyramid?\n"))
    baseWidth = float(input("What´s the base width of the pyrmaid?\n"))
    height = float(input ("What´s the height of the pyramid?\n")) 
    result = float(volPyramid (baseLength, baseWidth, height))
    print ("The volume is: " + str(result))
elif mainChoice ==3:
     radius = float(input ("What´s the radius of the sphere?\n"))
     result= float(volSphere(radius))
     print ("The volume is: " + str(result))
    
