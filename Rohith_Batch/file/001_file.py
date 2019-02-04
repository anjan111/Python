# create the file sample.txt
def main():
    file_obj = open("sample.txt","w+")
    print file_obj.read() # we cant able to read 
    file_obj.write("i am anjan kumar \niam python and AI Engineer")
    file_obj.seek(0,0)
    print file_obj.read() # we cant able to read 
    file_obj.close()

if(__name__ =="__main__"):
    main()

