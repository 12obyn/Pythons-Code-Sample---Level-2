#Maylene Garcia
#4/9/19
#Problem 6. This program print a random list of 100 elements from range (1,1000) and give the average of the given list.

import random

print (random.randrange(1,1000))
List = []
for x in range (100):
    List.append(random.randrange(1,1000))
    
average = random.randrange(1,1000)/100
print(average)
