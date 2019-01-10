# Basic Built in functions

#raw_input()
'''
We can read any data type from keyboard , it can access str data type 
'''

def main():
    num1= raw_input("enter some data ")
    num1 = list(num1)
    num2= raw_input("enter some data ")
    num2 = list(num2)
    num =num1*2
    print "num =",num
    print("type of ",num ,"is ",type(num))
    print "id of ",num,"is",id(num)


if(__name__=="__main__"):
    main()
