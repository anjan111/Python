# its module creation
'''
Every python file is a module
module used for reusability of the code
we can reduce the code size

'''
import package
def main():
    num1 = input("enter a some number")
    num2 = input("enter a some number")
    res =package.add(num1,num2)
    print "res of add ",res
    res =package.sub(num1,num2)
    print "res of sub ",res
    res =package.mul(num1,num2)
    print "res of mul ",res
if (__name__ =="__main__"):
    main()






    
