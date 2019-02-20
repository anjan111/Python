per =input("enter per ")
fo =open("sample.txt","a")
if(per > 70):
    fo.write("A Grade ")
elif(per > 60):
    fo.write(" B grade")
elif(per > 50):
    fo.write(" C Grade")
elif(per > 40):
    print " D Grade"
else:
    print " your failed "
fo.close()
    
