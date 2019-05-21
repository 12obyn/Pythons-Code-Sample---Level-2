#Maylene Garcia
#4/23/2019
#Problem 2, Module 3

xlist = [1, 2, 3, 4, 5]

def reverse(xlist):
    return [xlist[-1]] + reverse(xlist[:-1]) if xlist else []

print(reverse(xlist))


r=xlist[::-1]

print(r)
