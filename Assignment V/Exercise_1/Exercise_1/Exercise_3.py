stringToShift = raw_input("Put in a string to encode" )
numberToShiftBy = int(raw_input("Put in an integer number to shift by "))

for letter in stringToShift:
    letter + numberToShiftBy
    print(letter)