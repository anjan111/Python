# wap impliment movie tickets selection

movie= ['xyz','abc','123','496']
thr =['thr1','thr2','thr3']
print "at present the following movies are available"
print movie
mv=input("enter your interested movie ")
print "the followiing thr are avialble"
print thr
th=input("select thr")
seat=[1,2,3,4,5,6,7,8,9,10,11,12]
print "the following seats are aviable"
print seat
no_tk =input("enter how many tickets")#3
if(no_tk <len(seat)):
    st = input("select the seat numbers as in list")#[7,5,10]
    for c in range(len(st)):
        if(st[c] in seat):
            print" seat number ",st[c]," is confirmed"
            seat.remove(st[c])
        else:
            print "the ",st[c],"seat is not available"
        
    print "the following seats are aviable"
    print seat








            
    

