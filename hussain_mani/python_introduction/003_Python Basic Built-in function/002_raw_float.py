# this is file used for to understand raw_input with datatype  fucntion

def main():
    num = raw_input("enter float dataa ")
    # you can enter any data type the output type is str
    num =complex(num)
    print"num = ",num
    print" type =",type(num)
    print"id   = ",id(num)

if(__name__ =="__main__"):
    main()

# the above program modify  9 times with 9 different types
