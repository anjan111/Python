# list data type

var_l = ( 1, 2,4.5 ,"str")
# hetro genious datatype
print var_l  # we are printing list of  var_1 elements
print len(var_l)  # no of elements in a list
print max(var_l) # maximum list element

print min(var_l) # minimum list element

print tuple("python")#('p','y','t','h','o','n')

# tuple indexing
# positive  / forwaord

print var_l[0] # 1
print var_l[1] # 2

# negatice / reverse
print var_l[-1] # "str"
print var_l[2]  # 4.5

# tuple slicing
print var_l[1 : 3]  # (2,4.5)
print var_l[:]  # (1,2,4.5,"str")
# tuple dicing
print var_l[0 : :2] # (1,4.5)


