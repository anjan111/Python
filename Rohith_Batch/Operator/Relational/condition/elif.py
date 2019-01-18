# grading system for student marks

def main():
    s1 = input("enter sub marks")
    s2 = input("enter sub marks")
    s3 = input("enter sub marks")
    s4 = input("enter sub marks")
    s5 = input("enter sub marks")
    g_m =s1+s2+s3+s4+s5
    avg =(float(g_m)/500)
    per =avg * 100
    if(per > 70):
        print "A Grade"
    elif(per > 60):
        print " B Grade"
    elif(per > 50):
        print "C Grade"
    elif(per > 40):
        print "D Grade"
    else:
        print " Failed"
if(__name__ =="__main__"):
    main()
# WAP Based on the experience display the salay range 
