# wap print your full details when your age more than 18
def main():
    name = input("enter a name")
    age =input("enter your age")
    ph = input("enter your phone")
    if(age > 18):
        print "name = ",name
        print "age  = ",age
        print "ph   = ",ph
if(__name__ == "__main__"):
    main()
