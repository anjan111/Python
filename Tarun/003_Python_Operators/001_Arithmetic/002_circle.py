# WAP to find area and perimeter of circle
def main():
    r = input("enter  radius  of circle in meters ")
    pi = 22.0 /7
    area = pi * r * r
    peri = 2 * pi * r
    print " Area of circle is ",area ," sq. m when radius is ",r ,' m'
    print " peri of circle is ",peri ," m when radius is ",r ,' m'
if(__name__ == "__main__"):
    main()
