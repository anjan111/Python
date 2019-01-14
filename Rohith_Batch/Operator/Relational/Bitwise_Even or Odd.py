'''
Program         : Find the Given number is Even or Odd using bitwise operator

Programmer      : Rohit

'''

def main():
    a = input('Enter a value: ')
    if a&1==0:
        print "Number is Even"
    else:
        print "Number is Odd"

if (__name__=="__main__"):
    main()
