'''
Program             : Find if the entered year is leap year

Programmer      : Rohit
'''

def main():

    yr = input('Enter the year: ')
    if (yr%4==0):
        print ('Entered year is a Leap Year.')
    else:
        print ('Entered year is Not a Leap Year.')


if (__name__ == "__main__"):
    main()
