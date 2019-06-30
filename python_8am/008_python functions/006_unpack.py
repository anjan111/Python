# packing and un packing

def fun_unpack(x,y,z,w):
    print x+y+z+w

def main():
    a = [10,20,30,40]
    fun_unpack(*a)

if __name__ =="__main__":
    main()
