# WAP given number of n bit clear
def main():
    num = input("enter a number ")
    print bin(num)
    n = input("which bit you wanna clear  it ")
    num =num & (~(1<<n))
    print bin(num)
    

if(__name__ == "__main__"):
    main()

#wap given number of n bit set it 
