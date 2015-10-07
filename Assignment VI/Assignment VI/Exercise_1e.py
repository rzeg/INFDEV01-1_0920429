import math

size = int(raw_input("Type radius as an integer number: "))
finalString = ""
center = size / 2

for y in range(0,size):
        for x in range (0, size):
            distanceX = x - center
            distanceY = y - center
            distance = math.sqrt(distanceX ** 2 + distanceY ** 2)
            if(distance < center):
                finalString += "*"
            else:
                finalString += " "
        finalString += "\n"      
print(finalString)
