# return keyword

def fun_ret(x =10):
    res =x**3
    return res

def main():
    a = input("enter a : ")
    r = fun_ret(a)
    print "res = ",r
if __name__ == "__main__":
    main()
