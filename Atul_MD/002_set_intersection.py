#intersection  operation
a = {1,2,3,4}
b = {3,4,5,6}

print"******intersection operation**********"
print  a&b          # {3,4}
print a.__and__(b)   # {3,4}
print a.intersection(b)#{3,4}
# intersection_update menethod
'''
after intersection operation the result we can store that particular variable
'''
print "a : ",a
print "b : ",b
a.intersection_update(b)  # a = a&b
print "a : ",a
print "b : ",b
