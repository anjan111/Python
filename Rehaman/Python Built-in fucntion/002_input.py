# Basic Built in functions

#input()
'''
We can read any data type from keyboard , it can access that particular
data type 
'''

def main():
    num= input("enter some data ")
    print "num =",num
    print("type of ",num ,"is ",type(num))
    print "id of ",num,"is",id(num)


if(__name__=="__main__"):
    main()
# the above program execute 10 times  for each time  with different data type
