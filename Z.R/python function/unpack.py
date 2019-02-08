# unpacking
def fun(a,b,c):
    l=[1,2,4,4]
    return *l

a=[1,2,3]
v =fun(*a)
print v
