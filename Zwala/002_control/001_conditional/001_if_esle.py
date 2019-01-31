# wap find square of a number when given even or find sqrt of a number

def main():
    num = input("enter some data ")
    if(num % 2 == 0):
        sqr =num ** 2
        print "square of a ",num ," is ",sqr
    else:
        sqrt =num ** 0.5
        print "square root of  a ",num ," is ",sqrt
if(__name__ =="__main__"):
    main()
        
