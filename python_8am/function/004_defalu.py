# function with default arguments
'''
to send the data from function call to function defination
'''

def fun_arg( x=None ,y =None ,z =None):
    print "x = ",x
    print "y = ",y
    print "z = ",z

def main():
    #a = input("enter a : ")
    b = input("enter b : ")
    c = input("enter c : ")
    fun_arg(10,b,c*b) # actual argume
    fun_arg() # actual argume
if __name__ =="__main__":
    main()
