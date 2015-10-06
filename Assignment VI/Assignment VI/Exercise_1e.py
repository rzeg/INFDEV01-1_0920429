import math

size = int(raw_input("Type radius as an integer number: "))
finalString = ""

for x in range(0,size):
        for y in range (0, size):
            distX = x - size / 2
            distY = y - size / 2
            dist = math.sqrt(distX * distX + distY * distY)
            if(dist < size / 2):
                finalString += "*"
            else:
                finalString += " "
        finalString += "\n"      
print(finalString)
