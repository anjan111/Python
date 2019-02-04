'''
#Fibonacci Sequence

num = 10
first_num = 0
secon_num = 0
for i in range(0,num+1):
    first_num = i
    secon_num = i+first_num
    print secon_num
'''
# change this value for a different result
nterms = 10

# uncomment to take input from the user
#nterms = int(input("How many terms? "))

# first two terms
n1 = 0
n2 = 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence upto",nterms,":")
   while count < nterms:
       print n1
       nth = n1 + n2
       # update values
       n1 = n2
       n2 = nth
       count += 1
