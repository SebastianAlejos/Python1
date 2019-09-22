item= float (input ("What item do you want? Soda, Chocolate, or Peanuts. For soda press 1, for chocolate 2 and for peanuts 3\n"))
if  item== 1:
    price = 12
    print("the price is: $" + str(price))
elif item== 2 :
    price= 9
    print("the price is: $" + str(price))
elif item== 3 :
    price= 3
    print("the price is: $" + str(price))       
m10 =float (input ("How many $10 coins are you inserting?\n"))
m5 =float (input ("How many $5 coins are you inserting?\n"))
m1 =float (input ("How many $1 coins are you inserting?\n"))
money= float(m10*10+ float(m5*5) +float(m1))
change= int(float(money)-float(price))
print("your change is: "+str(change))
cambio10= int(float(change)//10)
remainder1= int(float(change)%10)
cambio5= int(float(remainder1)//5)
remainder2=int(float(remainder1)%5)
cambio1=int(remainder2)
print("Your change is: " +str(cambio10) +" coins of $10, " +str(cambio5)+ " coins of $5, and "+str(cambio1)+ " coins of $1")
