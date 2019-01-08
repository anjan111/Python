'''
Program         : Find the Area and Perimeter of Square

Programmer      : Rohit
'''

def main():
    side = input("Please enter the lenght of side of the square in meters ")
    area = side**2
    peri = side*4
    print ('The area of the square is ',area,'Sq.mts')
    print ('The perimeter of the square is ', peri, 'Mts')
    

if (__name__ == "__main__"):
    main()
