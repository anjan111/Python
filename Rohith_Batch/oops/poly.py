class Poly():
    var =19  #static variable  / class variable
    '''
     It can access by any object of the same class
    '''
    def __init__(self,a):
        self.v = a  # instance variable  / non static
        '''
        It can access that perticular object can access 
        '''
    def print1(self):
        print self.var
        print self.v

obj =Poly(89)
obj2=Poly(34)
obj.print1()
obj2.print1()

