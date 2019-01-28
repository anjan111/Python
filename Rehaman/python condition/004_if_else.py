# if given number is even then find square else find square root of number
def main():
    num = input("enter a number ")
    if (num % 2 == 0):
        print " square of ",num ," is ",num*num
    else:
        print " square root of ",num ," is ",num ** 0.5
if(__name__ =="__main__"):
    main()
