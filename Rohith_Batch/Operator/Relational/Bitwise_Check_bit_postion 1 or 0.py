'''
Program             : Check the bit position is 0 or 1

Programmer      : Rohit

'''

def main():
    a = input('Enter a value: ')
    b = input('Enter the position of bit to find if the value is 0 or 1: ')
    if (a & (1 << b) == 0):
        print b,"position is 0"
    else:
        print b,"position is 1"

if (__name__=="__main__"):
    main()
