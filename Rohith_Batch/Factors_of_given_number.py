'''
Program             : Find the number of factors for given number and find if it is prime

Programmer      : Rohit
'''

def main():

    num = input ('Enter a number: ')
    count = 0;
    for i in range(2, num-1):
    	if num%i == 0:
    	    print(i);
    	    i += 1;
    	    count += 1;
    if count==0:
        print(num,"is a prime number.");
    print 'Total factors of given number are: ', count+2

if (__name__ == "__main__"):
    main()
