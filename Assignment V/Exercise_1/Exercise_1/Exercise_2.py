inputPassword = raw_input("Put in your password for checking ")

passwordStrength = 0
strengthString = ""

for symbol in inputPassword:
    if(symbol.isdigit):
        passwordStrength += 1
    elif(symbol.isupper):
        passwordStrength += 1
    elif(symbol.islower):
        passwordStrength += 1
    elif(symbol.isspace):
        passwordStrength += 5

if(len(inputPassword) > 15):
    passwordStrength += 3


if(passwordStrength < 5):
    strengthString = "Weak"
elif(passwordStrength < 15):
    strengthString = "Medium"
elif(passwordStrength > 20):
    strengthString = "Strong"

print(strengthString)