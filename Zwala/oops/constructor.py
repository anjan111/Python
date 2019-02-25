class Car:
    def __init__(self,speed ,color):# parameter constructor
        print self
        self.speed =speed  # instance variable 
        self.color =color
    def __del__(self):
        print "i am distructor"
        
audi =Car("120KMPH","Black")
honda =Car("100KMPH","Blue")
print audi.speed
print audi.color
print honda.speed
print honda.color
del audi
del honda

