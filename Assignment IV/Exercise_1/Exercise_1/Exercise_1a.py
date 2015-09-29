while True:
    try:
        fahrenheitTemp = raw_input("Type the Fahrenheit value to convert to Celsius: ")
        fahrenheitTemp = float(fahrenheitTemp)
        conversion = (fahrenheitTemp - 32.0) * 5.0/9.0
        print("%.2f Celsius" % conversion)
        break
    except ValueError:
        print("That is not a number, try again")