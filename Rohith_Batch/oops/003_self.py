# data hiding

class Name():
    __var =10 #data hiding
    def met(self):
        print self.__var

v=Name()
#print v.__var
v.met()
