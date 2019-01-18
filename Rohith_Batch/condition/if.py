# WAP print squre / find the sqre of a number when given number is even

def main():
    num = input("enter some data ")
    even = (num % 2 == 0)
    if(even ==True):
        sqre = num ** 2
        print " squre of a ",num ," is  : ",sqre
    print " if block over"

    
if(__name__ =="__main__"):
    main()  
