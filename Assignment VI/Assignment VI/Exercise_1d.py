﻿size = int(raw_input("Type size as an integer number: "))
finalString = ""

for x in range(0,size):
    if(x % 2 == 0):
        for y in range (-size, -x):
            finalString += " "
        for z in range (0, x + 1):
            finalString += " *"
        finalString += "\n"      
print(finalString)
