# Registration form fot traveling

def main():
    print (" are you intersted for goa trip if interster")
    op =input("Press 1  if not press 0")
    if(op ==1):
        amount = input("enter how much you can spend to go goa INR")
        if(amount >=5000):
            name =input("enter your name")
            emp_id =input("enter your emp id")
            print "thank for your interest to go for  goa"
        else:
            print "your spending ",amount ,"it is not sufficient"
            print " Minimum you have to spend 5000 Rs/-"
            print "If you are interested then go registration"

    print"Thanks for spending the time here"
   
    

if(__name__ =="__main__"):
    main()
