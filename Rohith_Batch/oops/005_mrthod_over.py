class Class1():
    def meth(self):
        print" i am not received any thing"
class Class2():
    def meth(self,a ):
        print "i can receive one argu"

class Class3():
    def meth(self,a,b):
        print " i  am class3 method"
    
obj2=Class2()
obj1 =Class1()
obj3=Class3()

obj3.meth(12,45)
obj2.meth(12)
obj1.meth()
    
