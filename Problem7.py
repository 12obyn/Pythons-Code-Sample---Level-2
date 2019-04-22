#Maylene Garcia
#4/16/19
#This program will open a file and see if its found.


try:
    with open('file.log') as file:
        read_data = file.read()
except FileNotFoundError:
    print("File not found")
