def kmToMiles():
    km=int(input("Enter the Kms: "))
    miles=km * (0.621371)
    print "The miles are: ",miles
    
def ctoF_temp():
    celsius=int(input("Enter the temperaturs in Celsius: "))
    fahr=(celsius * (1.8))+32
    print "Temperature in Fahrenheit: ",fahr
    
def isPrime():
    num=int(input("Enter the number: "))
    for i in range(2,num):
        if num%i==0:
            print "The number is NOT a Prime Number."
            break
    else:
        print "The number is a Prime Number."
        
def prime_list():
    interval=int(input("Enter the range of PrimeNumbers needed: "))
    print "Prime Numbers are: ",
    for num in range(2,interval):
        for i in range(2,num):
            if num%i==0:
                break
        else:
            print num,
            
def getFactorial():
    num=int(input("Enter the number:"))
    prod=1
    print "The Factorial is: ",
    for i in range(2,num+1):
        prod*=i
    print prod

    
def multiplication_table():
    num=int(input("Which Multiplication Table: "))
    for i in range(1,21):
        print num,"X",i,"=", (num*i)
    
def fibonacci():
    num=int(input("Enter the range for Fibonacci sequence: "))
    first=0
    second=1
    third=first+second
    print first,second,
    while third<=num:
        print third,
        first=second
        second=third
        third=first+second

def isArmstrong():
    num=int(input("Enter the number to check w/Armstrong number: "))
    n=num
    sum=0
    L=[]
    while n>0:
        L.append(n%10)
        n=n//10
    print L
    for i in range(len(L)):
        sum+=(L[i])**3
    print sum
    if sum == num:
        print "The number is an Armstrong number"
    else:
        print "The number is NOT an Armstrong number."
        
def get_factors():
    number=int(input("Enter the number: "))
    print "The Factors are:",
    for i in range(1,number+1):
        if number%i==0:
            print i,    

def getGCD():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    small=min(a,b)
    big=max(a,b)
    gcd=0
    print "The HCF or GCD is: ",
    for i in range(1,small+1):
        if small%i==0 and big%i==0:
            gcd=i
    print gcd

def getLCM():
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    big=max(a,b)
    lcm=0
    print "The LCM is: ",
    while True:
        if big%a==0 and big%b==0:
            lcm=big
            break
        big+=1
    print lcm
            

if (__name__=="__main__"):
    #kmToMiles()
    #ctoF_temp()
    #isPrime()
    #prime_list()
    #check_factorial()
    #multiplication_table()
    #fibonacci()
    #isArmstrong()
    #get_factors()
    #getGCD()
    getLCM()