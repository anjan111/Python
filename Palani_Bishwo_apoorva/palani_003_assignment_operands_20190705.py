##1. wap find area and perimter of square
square_side=input("enter the lenght of the square side in meters:")
print "the area of the square is: ", square_side*square_side, " sq.m\n"
print "the perimeter of the square is: ", square_side*4, "m\n"
print "the surface area of the cube is: ", (square_side*square_side)*6, "sq.m\n"
print "the volume of the cube is: ", square_side**3, "cu.m\n"
##2. wap find area and perimter of rectangle
rect_l=input("enter the length of the rectangle side in meters:")
rect_w=input("enter the width of the rectangle side in meters:")
rect_h=input("enter the height of the rectangle side in meters:")
print "the area of the rectangle is: ", rect_l*rect_w, "sq.m\n"
print "the perimeter of the rectangle is: ", (rect_l+rect_w)*2, "m\n"
print "the surface area of the room is: ", ((rect_l*rect_h)*2) + ((rect_l*rect_w)*2)+((rect_w*rect_h)*2), "sq.m\n"
print "the volume of the rectangular room is: ", rect_l*rect_w*rect_h, "cu.m\n"
##3. wap find area and perimter of triangle
tri_side1=input("enter the length side1 of triangle in meters:")
tri_side2=input("enter the length side2 of triangle in meters:")
tri_base=input("enter the length of base of triangle in meters:")
tri_height=input("enter the height of triangle in meters:")
print "the area of a triangle is: ", 0.5*tri_base*tri_height, "sq.m\n"
print "the volume of the triangle is: ", tri_side1+tri_side2+tri_base, "m\n"
##6. wap find area and volume of cylender
cyl_radius=input("enter the radius of the cylinder in meters:")
cyl_height=input("enter the height of the cylinder in meters:")
print "the area of the cylinder is: ", (2*3.14*cyl_radius*cyl_height)+(2*3.14*cyl_radius**2), "sq.m\n"
print "the volume of the triangle is: ", 3.14*(cyl_radius**2)*cyl_height, "m\n"
##7. wap sum of 1st  N Natural Numbers
nat_num=input ("enter the N for upper limit for natural numbers:")
n=nat_num
sum1 = 0
while(n > 0):
    sum1=sum1+n
    n=n-1
print"The sum of first n natural numbers is",sum1
##8. wap sum of squares of N Natural numbers
o=nat_num
sum2 = 0
while(o > 0):
    sum2=sum2+(o**2)
    o=o-1
print"The sum of cube of first n natural numbers is",sum2
##9. wap sum of cubes of N natural numbers
o=nat_num
sum3 = 0
while(o > 0):
    sum3=sum3+(o**3)
    o=o-1
print"The sum of cube of first n natural numbers is",sum3
##10. wap find the ssimple interst and total amount
