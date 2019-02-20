# wap to find biggest number from three numbers

def main():
    a = input("enter some data")
    b = input("enter some data")
    c = input("enter some data")
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
