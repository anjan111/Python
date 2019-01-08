'''
Program         : Find the Volume and Area of Cylinder

Programmer      : Rohit
'''

def main():
    import math
    radius = input("Please enter the radius of cylinder in centimeters ")
    height = input("Please enter the height of cylinder in centimeters ")
    area = (2*(math.pi)*radius*height)+(2*(math.pi)*(radius**2))
    volume = math.pi*(radius**2)*height
    print ('The area of the cylinder is ',round(area, 2),'sq.cm')
    print ('The volume of the cylinder is ', round(volume, 2), 'cm3')
    

if (__name__ == "__main__"):
    main()
