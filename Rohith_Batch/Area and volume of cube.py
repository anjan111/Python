'''
Program         : Find the Volume and Area of Cube

Programmer      : Rohit
'''

def main():
    import math
    edge = input("Please enter the length of edge of the cube in centimeters ")
    area = 6*(edge**2)
    volume = area**3
    print ('The area of the cube is ',area,'sq.cm')
    print ('The volume of the cube is ', volume, 'cm3')
    

if (__name__ == "__main__"):
    main()
