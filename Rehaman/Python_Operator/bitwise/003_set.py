#wap given number of n bit set it

def main():
    num = input("enter a number ")
    print bin(num)
    n = input("which bit you wanna clear  it ")
    num =num | (1<<n)
    print bin(num)
    

if(__name__ == "__main__"):
    main()

# wap toggle n bit of given number
# wap given is power 2 or not
# wap clear from 2bit to 5bit  of any number
# wap set from 2bit to 5bit of any number
# wap toggle from 2 bit 5bit of any numbers 
