# wap find the area  and perimeter  of rectangle 
def main():
    l  = input("enter len of rectangle  in meter")
    b  = input("enter bre of rectange in meters")
    area =l * b
    peri =2* (l + b) 
    print " area of rectangle  is ",area , "sq. m  when l  ",l," m"," b ",b," m"
    print " peri of rectangle  is ",peri , " meters  when l  ",l," m"," b ",b," m"
    
if(__name__ == "__main__"):
    main()
