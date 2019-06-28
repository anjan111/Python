'''
This is the program is used for to understand the function
'''
# wap print your details


def details( ):
    name = input("entwer name : ")
    phone= input("enter phone : ")
    mail = input("enter mail  : ")
    print "name = ",name
    print "phone= ",phone
    print "mail = ",mail

def main():
    print"i am at main"
    details( )
    print "i am at exiting from main block"
print __name__
'''
if __name__ =="__main__" :
    print" i ma at main block"
    main()  # main block calling
    print" i am exiting from main block"
'''
