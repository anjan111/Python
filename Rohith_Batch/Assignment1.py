def main():
    a= input("enter the a some value")
    x=a
    b= input("enter the b some value")
    print "a value is", a,"identity of a",id(a)
    print "b value is", b,"identity of b",id(b)
    print "a =",a, "+",b,"is",
    a=a+b
    print a,"identity of a",id(a)
    a=x
    print "a+=",b,"is",
    a+=b
    print a,"identity of a",id(a)
    
    print "a =",a, "-",b,"is",
    a=a-b
    print a,"identity of a",id(a)
    a=x
    print "a-=",b,"is",
    a-=b
    print a,"identity of a",id(a)
    
    print "a =",a, "*",b,"is",
    a=a*b
    print a,"identity of a",id(a)
    a=x
    print "a*=",b,"is",
    a*=b
    print a,"identity of a",id(a)
    
    print "a =",a, "/",b,"is",
    a=a/b
    print a,"identity of a",id(a)
    a=x
    print "a/=",b,"is",
    a/=b
    print a,"identity of a",id(a)
    
    print "a =",a, "%",b,"is",
    a=a%b
    print a,"identity of a",id(a)
    a=x
    print "a%=",b,"is",
    a%=b
    print a,"identity of a",id(a)

    print "a =",a, "**",b,"is",
    a=a**b
    print a,"identity of a",id(a)
    a=x
    print "a**=",b,"is",
    a**=b
    print a,"identity of a",id(a)
    
if __name__=="__main__":
    main()
    
