# methode  over ridding support 

class Car:
    def meth(self):
        print"i have no parameters"
    def meth(self,a =10):
        print"i have one parameters"
    def meth(self,a =10,b=20):
        print"i have two parameters"

obj = Car()
obj.meth()
#obj.meth(20)
#obj.meth(45,67)
