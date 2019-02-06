def main():
    print "MAX WRONG PASSWORD ATTEMPTED ARE 5 TIMES"
    password="ANJAN123"
    pswd =input("enter password in str")
    C=5
    while(password !=pswd):
        C=C-1
        print "you have only ",C," chances left"
        if(C== 0):
            break
        print "password is not match"
        pswd =input("enter proper passoword  in str")
    else:
        print "password is matched "
        print "your in windows 10 os"
if(__name__ =="__main__"):
    main()
    
