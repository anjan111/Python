#union  operation
a = {1,2,3,4}
b = {3,4,5,6}

print"******union operation**********"
print  a|b          # {1,2,3,4,5,6}
print a.__or__(b)   # {1,2,3,4,5,6}
print a.union(b)
# update menethod
'''
after union operation the result we can store that particular variable
'''
print "a : ",a
print "b : ",b
a.update(b)  # a = a|b
print "a : ",a
print "b : ",b
