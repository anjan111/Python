# WAP print squre / find the sqre of a number when given number is even
# print sqroot of number when number is not even 

def main():
    num = input("enter some data ")
    even = (num % 2 == 0)
    if(even ==True):
        sqre = num ** 2
        print " squre of a ",num ," is  : ",sqre
    else:
        sqrt = num ** 0.5
        print " squre root  of a ",num ," is  : ",sqrt
        
    print " if -else  block over"

    
if(__name__ =="__main__"):
    main()

# WAP given character is vowel or consonant  ----> in operator
# WAP given number is positive or negative 


