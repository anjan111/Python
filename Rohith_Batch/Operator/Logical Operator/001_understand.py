# this file is understand for logical operators

'''
Logical AND ---> and
---------------------

Defination :

-----------

if 1st input is false case then output is 1st input value
other wise 2nd input value is the output 

Logical OR---> or
---------------------

Defination :

-----------

if 1st input is false case then output is 2st input value
other wise 1st input value is the output 


Logicakl not ---> not
---------------------

Defination :

-----------

if 1st input is false case then output is True boolean data
other wise False boolean data as on output 



'''
def main():
    a = input("enter boolean data")  # True
    b = input("enter boolean daata")  # False

    print a ," logical and", b," is ", a and b

    print a , "logical or ",b, " is ", a or b

    print " logical not ", b ,"is " , not b

if(__name__ =="__main__"):
    main()
