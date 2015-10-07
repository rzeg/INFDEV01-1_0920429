stringToShift = raw_input("Put in a string to encode " )
numberToShiftBy = int(raw_input("Put in an integer number to shift by "))
finalString = ""

for letter in stringToShift:
    if(str.isupper(letter)):
        asciiNumber = ord(letter) - 65
        asciiNumber += numberToShiftBy
        asciiNumber %= 26
        asciiNumber += 65      
        convertedLetter = chr(asciiNumber)
    elif(str.islower(letter)):
        asciiNumber = ord(letter) - 97
        asciiNumber += numberToShiftBy
        asciiNumber %= 26
        asciiNumber += 97    
        convertedLetter = chr(asciiNumber)
    else:
        convertedLetter = letter
    finalString += convertedLetter
print(finalString)