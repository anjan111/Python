# wap grading system of student marks

def main():
    s1 = input("enter s1 suj mark")
    s2 = input("enter s2 suj mark")
    s3 = input("enter s3 suj mark")
    s4 = input("enter s4 suj mark")
    s5 = input("enter s5 suj mark")
    s6 = input("enter s6 suj mark")
    t_m =s1+s2+s3+s4+s5+s6
    print t_m
    avg =float(t_m) / 600
    print avg
    per =avg * 100
    print per
    
    if(per > 70):
        print " Distinction  with A Grade"
    elif(per > 60):
        print " A Grade"
    elif(per > 50):
        print " B Grade"
    elif(per > 40):
        print " C Grade"
    else:
        print " you Failed "
    
if(__name__ =="__main__"):
    main()
