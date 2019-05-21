#Maylene Garcia
#4/23/2019
#Problem 6, Module 3


textD = {}

f = open("testText.txt", "r")

def buildTextD(words):
    for x in words:
        if x not in textD:
            textD[x] = 1
        else:
            textD[x] = textD[x] + 1

for line in f:
    w = line.split()
    buildTextD(w)

print(textD)

f.close()

