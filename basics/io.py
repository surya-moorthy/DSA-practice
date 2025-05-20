import os

openinput = print("open file")
getinput = input("Enter your input:")

if getinput == "":
   print("how can't you provide")
else:
   print("Your input:",getinput)

fileName = input("Enter your file name:")

enterText = input("Enter text that you want to write:")

if fileName :
    with open(fileName,"w") as file:
        file.write(enterText)
    with open(fileName,"r") as file:
        print(file.read())
else:
    print("file does not exist")
