# wap if given number even then find square of number

def main():
    num = input(" enter a number")
    if (num % 2 == 0):
        sqr = num * num
        print " sqr  of  ",num , " is ",  sqr
    print " my main function is over"

if (__name__ == "__main__"):
    main()
