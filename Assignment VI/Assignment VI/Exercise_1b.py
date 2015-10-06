height = int(raw_input("Type height as an integer number: "))
width = int(raw_input("Type width as an integer number: "))
finalString = ""

for x in range(0,height):
    for y in range (0, width):
        if(y > 0 and y < width - 1 and x > 0 and x < height - 1):
            finalString += " "
        else:
            finalString += "*"
    finalString += "\n"
            
print(finalString)
