# wap find n bit  of number is 0 or 1
def main():
    num = input("enter a number ")
    n = input("which bit you wanna check it ")
    res =num & (1 << n)
    print res != 0
    

if(__name__ == "__main__"):
    main()

# WAP given number is even or not
# wap given number is odd or not 
