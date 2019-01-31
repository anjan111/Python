# wap to find the square of a number when given number is even
def main():
    num = input("enter some data")
    if(num % 2 ==0):
        sqr = num ** 2
        print "square of a ",num," is ",sqr
        
if(__name__ =="__main__"):
    main()

