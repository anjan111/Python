'''
Program         : Convert Fahrenheit to Celsius

Programmer      : Rohit
'''

def main():
    import math
    fahren = input("Please enter the temperature in Fahrenheit ")
    celsius = (fahren-32)*5/9
    print ('The temperature in celsius is ', round(celsius, 2))
    

if (__name__ == "__main__"):
    main()
