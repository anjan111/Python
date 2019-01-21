'''
Program             : Find smallest number from the entered 3 numbers

Programmer      : Rohit
'''

def main():

    a = input('Enter a number: ')
    b = input('Enter a number: ')
    c = input('Enter a number: ')

    if (a < c and a < b):
        print 'Smallest number is ', a
    elif ( b < a and b < c):
        print 'Smallest number is ', b
    else:
        print 'Smallest number is ', c

if (__name__ == "__main__"):
    main()
