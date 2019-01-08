'''
Program         : Find the Area and Perimeter of Triangle

Programmer      : Rohit
'''

def main():
    import math
    a = input("Please enter the length of side a of Triangle in centimeters ")
    b = input("Please enter the length of side b of Triangle in centimeters ")
    c = input("Please enter the length of side c of Triangle in centimeters ")
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    perimeter = a+b+c
    print ('The area of the Triangle is ', round(area, 2),'sq.cm')
    print ('The perimeter of the Triangle is ', round(perimeter, 2),'cm')
    

if (__name__ == "__main__"):
    main()
