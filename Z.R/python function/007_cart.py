User_name =""
Password =""
def signup():
    global User_name
    global Password
    name =input("enter Full Name: ")
    mail =input("Enter Mail id  : ")
    Ph = input("enter Mobile No : ")
    User_name =input('enter User_name   : ')
    Password  =input("set your Password : ")
    print"Your Succussfuly=lu signup"
    print"press \n1---> Login"
    op=input("Select any one option")
    if(op==1):
        login()
    else:
        print"your select wron option"
    
def login():
    u_n =input("enter your user name ")
    p_s =input("enter your password  ")
    if(User_name =="" and Password ==""):
        print "There is no account available "
        print "Please signup First"
        signup()
        
    if(u_n ==User_name and p_s ==Password):
        print"Your succesfully login  My Cart Website "
        product_info()
    else:
        print "Password  or User Name not Matched"
        print"Login in again"
        login()
        
def product_info():
    dict ={"mobile" : ["sam","nokia","apple"],"lap":["apple","dell"]}
    dict1={"mobile" :15000,"lap":30000}
    for i in dict:
        print i
    print"select your product"
    pro=input(" : ")
    if(pro in dict):
        print dict[pro]
        sel =input("select any one above mobile")
        
        product_conf(sel,dict1[pro])
    else:
        print"product is not available"
        product_info()
        
def product_conf(pro,amount):
    print "Your product is confirmed"
    print "you have to pay ",amount


def main():
    print"------Welcome To MyCart Web site----"
    print"------------------------------------"

    print"Press \n0---> SignUP"
    print"press \n1---> Login"
    op=input("Select any one option")
    if(op ==0):
        signup()
    elif(op==1):
        login()
    else:
        print"your selected wrong option"
        
    
        
if(__name__ =="__main__"):
    main()

