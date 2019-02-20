# with default arguments with return
# wap find given number is prime or not

def isprime(num =12):
    count_fact =0
    for i in range(1,num+1):
        if(num % i ==0):
            count_fact+=1
    if(count_fact == 2):
        return True,num
    else:
        return False,num
    
      
def main():
    num = input("enter any number")
    res=isprime(num)
    print "Given ",res[1]," is prime",res[0]
if(__name__ =="__main__"):
    main()
