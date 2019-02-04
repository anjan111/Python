# wap to understand predefined modules and packages
from math import sqrt , pow
#import time 
import time as t
def main():
    num =input("enter  a num")
    print "squar ", pow(num, 2)
    t.sleep(2)
    print "sqrt ", sqrt(num)
if( __name__ == "__main__"):
    main()
