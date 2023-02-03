# TempConverter

# This program ask user to input tempearture in fahrenheit then convert's it into celsius.

inp = input('Enter Fahrenheit Temperature: ')  # ask for input
try:
    fahrenheit = float(inp)
    celsius = ((fahrenheit - 32)*5/9)  # convert's temperature.
    print(celsius)
except:
    print("Invalid input. Please enter a number")
