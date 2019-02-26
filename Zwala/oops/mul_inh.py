# inheritance

class para_class() : # Base class1
    def Caring(self):
        print " caring"

class Sis_class() : # Base class
    def fight(self):
        print"fightin"

class bro_class(Sis_class,para_class): # Deriver calss 2
    def suggest(self):
        print"suggestion"
    

obj = bro_class()
obj.Caring()
obj.fight()
obj.suggest()
