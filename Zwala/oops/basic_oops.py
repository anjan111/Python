class Car :
    var = 123 # class variable 
    def __init__(self,var1,var2):
        print" parameterized constructor"
        self.var1 = var1 # instance varibale
        self.var2 = var2 # instance varibale
    def access(self):
        print self.var1
        print self.var2
        print self.var
    def __del__(self):
        print"destroctor methode"

obj = Car(12,34)
obj.access()
del obj
