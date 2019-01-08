'''
Program         : Convert miles to kilometers

Programmer      : Rohit
'''

def main():
    import math
    mile = input("Please enter the number in miles ")
    kilo = mile*1.60934
    print ('The number in kilometers is ', round(kilo, 2))
    

if (__name__ == "__main__"):
    main()
