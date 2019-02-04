# addition of two integers 
def main():
    num1 = raw_input("enter some data ")
    num1 =int(num1)
    num2 = raw_input("enter some data ")
    num2 = int(num2)
    num =num1 + num2
    # you can enter any data type the output type is str 
    print "num = ",num
    print" type =",type(num)
    print"id   = ",id(num)

if(__name__ =="__main__"):
    main()
