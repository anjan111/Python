# write a program to find factorial of a number

def main():
    num =input("enter your target number")
    if(num < 0):
        print " factorial is not posible"
    elif( num == 0 or num == 1):
        print " factorial of ",num, " is 1 "
    else:
        fact =1
        for val in range(1,num+1):
            fact =fact*val
        print " factorial of ",num, " is  ",fact

if(__name__ == "__main__"):
    main()
