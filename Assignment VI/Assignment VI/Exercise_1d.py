size = int(raw_input("Type height as an integer number: "))
finalString = ""

for x in range(0,size):
    # Man sometimes I think too hard
    for y in range (0, x + 1):
        finalString += "x"
    
    finalString += "\n"
            
print(finalString)
