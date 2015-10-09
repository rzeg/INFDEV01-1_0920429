while True:
    try:
        inputNumber = float(raw_input("Type the value you want an absolute number of: "))
        if(inputNumber < 0.0):
            inputNumber = -inputNumber
        print("The absolute value is %.2f " % inputNumber)
        break
    except ValueError:
        print("That is not a number, try again")