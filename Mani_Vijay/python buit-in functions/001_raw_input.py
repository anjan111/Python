# wap to understand raw_input function
'''
in python we don't have any main function
the execution starts from 1st statements 
'''
def main( ):
    var = raw_input("enter some data")
    print "var = ",var
    print " type of var ",type(var)
    print " id of var ",id(var)

if(__name__ == "__main__"):
        main()
