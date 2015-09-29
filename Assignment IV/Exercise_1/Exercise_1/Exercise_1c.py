while True:
    try:
        inputNumber = raw_input("Type the value you want an absolute number of: ")
        conversion = abs(float(inputNumber))
        print("The absolute value is %.2f " % conversion)
        break
    except ValueError:
        print("That is not a number, try again")