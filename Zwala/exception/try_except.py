try :
    print "hello i am try block"
    #import ifngkfhbkjbhjbhjkb
    #open("jkhjkdhffkjdkd","r")
    raise IOError
    print "hai i was 3rd statement"

except ZeroDivisionError:
    print "Its zero devision Error"
except ValueError:
    print " Its for value error"
except IOError:
    print "its for File error"
except:
    print "i got exception"
else:
    print " no exception"

finally :
    print " i can execute in both the cases"
    
