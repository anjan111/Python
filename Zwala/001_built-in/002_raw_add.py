# addition of two number using raw_input
def main():
    num1 = raw_input("enter  some int  ")
    num1 =int(num1)
    num2 = raw_input("enter some int ")
    num2 =int(num2)
    num =num1 + num2  # concatnation 
    print("num is ", num)
    print "type  ", type(num)
    print "id    ", id(num)

if (__name__ == "__main__"):
    main()
    
