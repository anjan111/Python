#!/usr/bin/python
def main():
  try :
    print "hello"
    #raise ValueError
    print "hai"
    #import lkfjgkljrhklh
    #print 10/0
    #a =int([1,2,3])
    print "njgnj"
  except ZeroDivisionError:
    print " ii am Zero Division Exception"
  except ValueError:
    print " I am Value Errror"
  except  ImportError:
    print "Import Errror"

  except:
    print "i can execute when exception occured "
  else:
    print "i can excute  when exception not occured "
  finally:
    print " i can execute in both cases"

if(__name__ =="__main__"):
     main()
