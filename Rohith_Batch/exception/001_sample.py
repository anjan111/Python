try :
    import math
    print math.sqrt(89)
    a =10
    b =2
    print a/b
    fo=open("samplle","w")
    fo.close()
    a =int(12.34)

except ImportError:
    print "please try import required module"
except TypeError :
    print "Please use float or int while sqrt"
except ZeroDivisionError:
    print "please use non zero value "
except IOError:
    print " please give proper file"
except ValueError:
    print " you give proper value"
except:
    print "this default exception"
else:
    print "program having no exception"
finally:
    print" important task we should write over here"
    

