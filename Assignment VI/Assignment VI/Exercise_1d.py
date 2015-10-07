size = int(raw_input("Type size as an integer number: "))
finalString = ""

for x in range (0, size):
    for y in range(0, size - x):
        finalString += " "
    for z in range(0, x * 2 + 1):
        finalString += "x"
    finalString += "\n"
print(finalString)
