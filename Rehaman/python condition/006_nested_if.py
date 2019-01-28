def main():
    a =input("enter a ")
    b = input("enter b")
    c=input("enter c")
    if(a < b):
        big =b
        if(big < c):
            big =c
    else:
        big =a
        if(big < c):
            big =c
    print "big = ",big
if(__name__ =="__main__"):
    main()
# wrt find smallest value
#find given year is leap year or not 
