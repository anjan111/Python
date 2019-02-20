# wap find the factorial
# 5 ----> 5*4*3*2*1--->
def main():
    num =input("enter number")
    if(num <0):
       print "factorial is not posible"
    elif(num ==0 or num ==1):
        print "factorial =1"
    else:
        fact=1
        temp =num
        while(num >=2):
            fact=fact*num
            num =num-1
    
        print"factorial of ",temp," is ",fact
if(__name__ =="__main__"):
    main()
# given number is prime number or not
# wap find sum of digits in a number
# wap find reverse of a number 123 --->321
