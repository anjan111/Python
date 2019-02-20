# nested fnctions
def fun():
    print " i am fun statement"
    def sub_fun():
        print "i am sub_fun"
    print " i am fun statement after sub_fun defination"
    sub_fun()
    print " i am fun statement after sub_fun call"
fun()

