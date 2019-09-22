file = open("Cw_2_2.txt", "r")
for line in file:
    cleanLine = line.replace("\n" , "")
    print(cleanLine)
file.close()

file= open ("Cw_2_2.txt", "r")
lines = file.readlines()
print(lines)
file.close()

file = open ("Cw_2_2.txt", "w")
file.write("A\n")
file.write("B\n")
file.write("C")
file.close()

file = open("Cw_2_2.txt", "a")
file.write("\nD")
file.close()

x= "A,b,c"
y = x.split(",")
print(y)

    
