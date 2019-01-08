'''
Program         : Find the Area and Circumference of Circle

Programmer      : Rohit
'''

def main():
    import math
    radius = input("Please enter the radius of the circle in meters ")
    area = (math.pi)*(radius**2)
    circum = 2*(math.pi*radius)
    print ('The area of the circle is ',area,'Sq.mts')
    print ('The circumference of the circle is ', circum, 'Mts')
    

if (__name__ == "__main__"):
    main()
