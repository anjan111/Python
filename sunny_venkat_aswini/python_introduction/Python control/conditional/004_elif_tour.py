# elif ladder

def main():
    print"Are  you interested for travelling "
    op =input("enter 1 or 0")
    if(op ==1):
        name= input("Enter your name")
        emp_id =input("enter your emp id")
        amount =input("enter your spending amount")
        if(amount >=5000):
            print "Your registered for Goa"
        elif(amount >= 4000):
            print "Your registered for Vizag"
        elif(amount >=3000):
            print "Your registered for Vijayawada"
        elif(amount >=2000):
            print "Your registered for Warangal"
        else:
            print "Your Registered for Zoo Park"
        print" Thanks for registered "
    print"Thanks for speding the time here"
if(__name__ =="__main__"):
    main()
    
