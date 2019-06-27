#difference  operation
a = {1,2,3,4}
b = {3,4,5,6}

print"******intersection operation**********"
print  a-b          # {1,2}
print a.__sub__(b)   # {1,2}
print a.difference(b)#{1,2}
# difference_update menethod
'''
after difference operation the result we can store that particular variable
'''
print "a : ",a
print "b : ",b
a.difference_update(b)  # a = a-b
print "a : ",a
print "b : ",b
