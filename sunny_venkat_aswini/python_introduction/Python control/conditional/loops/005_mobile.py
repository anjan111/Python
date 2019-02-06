def main():
    mobile = input("enter no moble ")
    mobile=range(1,mobile+1)
    while(mobile):
        print mobile
        c= input(" i need mobile")
        mobile.remove(c)
    else:
        print "outoff stack"
if(__name__ =="__main__"):
    main()
        
    
