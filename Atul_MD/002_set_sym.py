#symmetric_difference  operation
a = {1,2,3,4}
b = {3,4,5,6}

print"******symmetric_difference operation**********"
print (a|b) - (a&b)  #{1,2,5,6}
print  a^b          # {1,2,5,6}
print a.__xor__(b)   # {1,2,5,6}
print a.symmetric_difference (b)#{1,2,5,6}
# symmetric_difference _update menethod
'''
after symmetric_difference  operation the result we can store that particular variable
'''
print "a : ",a
print "b : ",b
a.symmetric_difference_update(b)  # a = a^b
print "a : ",a
print "b : ",b
