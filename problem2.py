#Maylene Garcia
#4/9/19
#Problem 2. This program will print the start week day and finish week day after a certain length.


start = int(input("What is the starting day?"))
length = int(input("How long will you be gone?"))
finish = (start + length) % 7



if finish == 0:
    print("Sunday")

if finish == 1:
    print("Monday")

if finish == 2:
    print("Tuesday")

if finish == 3:
    print("Wednesday")

if finish == 4:
    print("Thursday")

if finish == 5:
    print("Friday")

if finish == 6:
    print("Saturday")


