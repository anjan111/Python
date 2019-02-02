# this script file used for to understand sequrn datatype

def main():
    num = input("enter multiple data elements ")
    print "len ",len(num)
    print "max ",max(num)
    print "min ",min(num)
    print "ord",ord('c')
    print "ch",chr(89)
    #print "num  = ",num
    #print "type of ",type(num)
    #print "id of ",id(num)
    '''
    indexing:-
    -----------
    positive  ---> from left to right characters we can access
                    from string using 0 to len-1 / forward
    
    print "num[0]",num[0]
    print "num[1]",num[1]
    print "num[2]",num[2]
    print "num[3]",num[3]
    l = len(num) 
    print "num[len-1]",num[l-1]
    
    Backward  ---> from right to left characters we can access
                    from string using -1 to -len / Negative
    
    print "num[-1]",num[-1]
    print "num[-2]",num[-2]
    print "num[-3]",num[-3]
    print "num[-4]",num[-4]
    l=len(num)
    print "num[",-l,"]",num[-l]
    ----------
    Dicing :
    --------
    we can access  group of character from  string with periodic
    elements as string


    syntax :-
    ------------
    var =[ start : stop : step ]
    start ---> 0
    stop ----> len of string
    step ---> 1
    print num[2 :12 :3]
    print num[3 : 10: 2]
    l=len(num)
    print num[0 : l :1]
    print num[ : : ]
    '''
    #Slicing :
    #--------

    #syntax :
    #    var[start :stop]
    '''
    print num[3:10]
    print num[8:15]
    l=len(num)
    print num[0 :l]
    print num[:]
    '''
    




        
    





    
    

if(__name__ =="__main__"):
    main()
    
