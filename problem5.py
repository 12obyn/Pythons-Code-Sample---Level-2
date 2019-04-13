#Maylene Garcia
#4/9/19
#Problem 5. This program print a new list of  8 elements.

oldList = [1,3,3,3,6,2,3,5]
newList = []

for x in oldList:
    if x not in newList:
        newList.append(x)
print(newList)
