x = input("Enter a number: ")
c=0
for i in range(1, x + 1):
    if x%i ==0:
        print (i)
        c = c+1
print "Total factors of Given number ", x, "are ", c

