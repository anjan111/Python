# sum of natural number
def main():
    ip =input("do you want to do sum of n natural 1 or 0")
    while(ip==1):
        num=input("enter any int")
        i=1
        su=0
        while(True):
            if(i == num+1):
                break
            su =su +i
            i=i+1
        else:
            print "else will execute when condition is false"
        print "sum =",su
        ip =input("do you want to do sum of n natural 1 or 0")
        
if(__name__ =="__main__"):
    main()
