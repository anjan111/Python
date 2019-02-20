# multipliction table

def main():
    num = input("enter any a mulication number")
    i =0
    while(i <=9):
        i =i + 1
        if( i == 5):
            break # pass # continue 
        print num," * ",i," = ",num*i
        
    else:
        print "else will execute when condition is false"

if(__name__ =="__main__"):
    main()

