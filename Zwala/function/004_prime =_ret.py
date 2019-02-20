# with arguments with return
# wap find given number is prime or not

def isprime(num):
    count_fact =0
    for i in range(1,num+1):
        if(num % i ==0):
            count_fact+=1
    if(count_fact == 2):
        return True
    else:
        return False
    
      
def main():
    num = input("enter any number")
    print "Given ",num," is prime",isprime(num)
if(__name__ =="__main__"):
    main()
