class Machine() :# this is class
    # attributes 
    cpu =""
    os =""
    RAM =""
    ROM =""
    def paint(self): # methide
        print "Machine can do paint"
    def doc(self):
        print "Machine can do documentation"
    def properties(self):
        print "self ",self
        print "cpu = ",self.cpu
        print "os  = ",self.os
        print "RAM = ",self.RAM
        print "ROM = ",self.ROM
VM_obj1 =Machine() # object creation in called instancation
VM_obj2 =Machine()
VM_obj1.cpu='i3'
VM_obj1.os ="ubuntu"
VM_obj1.RAM="4GB"
VM_obj1.ROM="1TB"

VM_obj2.cpu='i5'
VM_obj2.os ="windows"
VM_obj2.RAM="8GB"
VM_obj2.ROM="100TB"
VM_obj1.properties()
VM_obj2.properties()


    
    
    
