burrito = 30
croissant = 50
moyetes = 45
panini = 60
check = 0
food = input("Welcome to Güich! Do you want something to eat? Type 1 for yes and 2 for no \n")
 
while food == "1":
   eat = input ("Type 1 for breakfast, and 2 for lunch \n")
   if eat == "1" :
       breakfast = input("If you want a burrito type 1 , or if you feel french today, type 2 for croissant \n")
       if breakfast == "1":
           print ("It will be $30 pesos")
           check = check + burrito
           food = input ("Do you want something else to eat? Type 1 for yes and 2 for no \n")
       else:
           print ("It will be $50 pesos")
           check = check + croissant
           food = input ("Do you want anything else? Type 1 for yes and 2 for no \n")
   else:
        
        lunch = input("If you want some very mexican molletes type 1, if you want a panini type 2 \n")
        if lunch == "1" :
            print ("It will be $45 pesos")
            check = check + molletes
            food = input ("Do you want something else to eat? Type 1 for yes and 2 for no \n")
        else :
            print (" It will be $60 pesos")
            check = check + panini
            food = input ("Do you want something else to eat? Type 1 for yes and 2 for no \n")


print ("Your total check is $", check," pesos thanks for buying at Güich")


    
            
        
