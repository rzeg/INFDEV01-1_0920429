while True:
    try:
        celsiusTemp = raw_input("Type the Celsius value to convert to Kelvin: ")
        celsiusTemp = float(celsiusTemp)
        conversion = celsiusTemp + 273.15
        if conversion <= 0:
            print("You have reached absolute zero!")
            break
        print("%.2f Kelvin" % conversion)
        break
    except ValueError:
        print("That's not a number!")