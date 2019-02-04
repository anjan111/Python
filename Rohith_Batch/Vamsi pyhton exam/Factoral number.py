def main():

    num = input ('Enter a number: ')
    count = 0;
    for i in range(2, num-1):
    	if num%i == 0:
    	    print(i);
    	    i += 1;
if (__name__ == "__main__"):
    main()
