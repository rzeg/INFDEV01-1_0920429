height = int(raw_input("Type height as an integer number: "))
width = int(raw_input("Type width as an integer number: "))
finalString = ""

for x in range(0,height):
    for y in range (0, width):
        finalString += "x"
    finalString += "\n"
            
print(finalString)
