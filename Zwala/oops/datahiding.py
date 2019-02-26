# data hiding

class Car :
    __speed ="120KMPH"
    def meth(self):
        print self.__speed

obj = Car()
print obj._Car__speed # data encaplutation
obj.meth()
