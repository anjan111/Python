# recursive function
def fun_rec(x =1):
    print x
    if(x < 10):
        fun_rec(x+1)
    print x
def main():
    fun_rec()
if __name__ == "__main__":
    main()
