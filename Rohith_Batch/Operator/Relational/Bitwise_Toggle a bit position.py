'''
Program             : To toggle the bit position to 0 or 1

Programmer      : Rohit

'''

def main():
    a = input('Enter a value: ')
    b = input('Enter the position of bit to Toggle it: ')
    c = a ^ (1 << b)
    print 'Binary representation of ', a, 'is: ', bin(a)
    print 'Value after Toggling the bit position is ', c
    print 'Binary representation of ', c, 'is: ', bin(c)
    
if (__name__=="__main__"):
    main()
