'''
Program             : To unset the bit position to 0

Programmer      : Rohit

'''

def main():
    a = input('Enter a value: ')
    b = input('Enter the position of bit to unset it to 0: ')
    c = a & ~(1 << b)
    print 'Binary representation of ', a, 'is: ', bin(a)
    print 'Value after unsetting the bit position to 0 is ', c
    print 'Binary representation of ', c, 'is: ', bin(c)
    
if (__name__=="__main__"):
    main()
