list1 = ["a", "b", "c"]
list2 = [0,1,2,3,4,5,6,7,8,9]
list3 = [10,11,12,13,14,15,16,17,18,19,20]
list4=list()
#1
def function1 (list1):
    for i in range(len(list1) -1, -1, -1):
        list4.append(list1[i])
    return list4
#2
def function2 (list2):
    value = int(input("Give me a value\n"))
    count = 0
    for i in range  (len(list2),1,-1):
        if value == i:
            count = count + 1
        else:
            count = count
    if count == 1:
        trueFalse= "True"
    else:
        trueFalse= "False"
    return trueFalse
#3
def function3 (list3):
    list4.clear()
    for i in range (0,len(list3),1):
        if (i % 2)!= 0:
            list4.append(list3[i])
    return list4
#4
def function4 (list3):
    list4.clear()
    for i in range (0,len(list3),1):
        if (list3[i] % 2)== 0:
            list4.append(list3[i])
    return list4
#5
def function5 (list2):
    summ= 0
    for i in range(0, len(list2), 1):
        summ = summ + list2[i]
    return summ
#6
def function6 (list2):
    summ=0
    count=0
    for i in range(0,len(list2), 1):
        summ= summ+ list2[i]
        average= summ/len(list2)
    return average
#7
def function7(number):
    lastTerm=0
    currentTerm=1
    result= list()
    for i in range (0, number):
        result.append(lastTerm)
        temp = currentTerm
        currentTerm=lastTerm+currentTerm
        lastTerm=temp
    return result
#8
def function8(list2, list3):
    result=list()
    for value in list2:
        result.append(value)
    for value in list3:
        result.append(value)
    return result
#9
def function9(l1,l2):
    result = list()
    for i in range (0,len(l1)):
        currentResult = l1[i]+l2[i]
        result.append(currentResult)
    return result
        
f = function1(list1)
print(f)

f2=function2(list2)
print(f2)

f3 = function3(list3)
print(f3)

f4= function4(list3)
print(f4)

f5= function5(list2)
print(f5)

f6= function6(list2)
print(f6)

number = int(input("How many terms: \n"))
f7 = function7(number)
print(f7)

print(function8(list2,list3))

print(function9(list2,list3))
