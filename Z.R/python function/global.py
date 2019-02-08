# global

var =10  # global
def fun():
    print var
    global var
    var =45 # local variable
    print var
    
fun()
print var
