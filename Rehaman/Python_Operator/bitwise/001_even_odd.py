# wap find given number is even or not  and odd or not

def main():
    num = input("enter a number ")
    
    res = num & (1 << 0)
    print num ," is even ",res ==0
    print num , "is odd ", res ==1
    

if(__name__ == "__main__"):
    main()
# WAP given number of n bit clear
