'''
Program             : To set the bit position to 1

Programmer      : Rohit

'''

def main():
    a = input('Enter a value: ')
    b = input('Enter the position of bit to set it to 1: ')
    c = a | (1 << b)
    print 'Binary representation of ', a, 'is: ', bin(a)
    print 'Value after setting the bit position to 1 is ', c
    print 'Binary representation of ', c, 'is: ', bin(c)
    
if (__name__=="__main__"):
    main()
