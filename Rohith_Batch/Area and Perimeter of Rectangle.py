'''
Program         : Find the Area and Perimeter of Rectangle

Programmer      : Rohit
'''

def main():
    length = input("Please enter the lenght of the rectangle in meters ")
    width = input("Please enter the width of the rectangle in meters ")
    area = length*width
    peri = 2*(length+width)
    print ('The area of the rectangle is ',area,'Sq.mts')
    print ('The perimeter of the rectangle is ', peri, 'Mts')
    

if (__name__ == "__main__"):
    main()
