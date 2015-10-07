import math

size = int(raw_input("Type radius as an integer number: "))
rimWidth = 1
finalString = ""
center = size / 2

for y in range(0,size):
        for x in range (0, size):
            distanceX = x - center
            distanceY = y - center

            distance = math.sqrt(distanceX ** 2 + distanceY ** 2)
            if(distance < center and distance > center - rimWidth):
                finalString += "*"
            elif((x == center - 2 or x == center + 2) and y == center - 2):
                finalString += "#"
            elif((x > center - 2 and x < center + 2) and y == center + 2):
                finalString += "-"
            else:
                finalString += " "
        finalString += "\n"      
print(finalString)
