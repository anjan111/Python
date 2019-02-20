#packing and unpacking
'''
def fun(*a): #packing 
    res =sum(a)
    print res

fun(1,4,5,6,2,10,56,34,90)
'''
def fun(a,b,c,d):
    print a
    print b
    print c
    print d

a=[1,2,3,4]
fun(*a)#unpacking 
