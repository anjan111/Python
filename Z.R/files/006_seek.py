file_obj = open("readfile11.txt","r")
print file_obj.tell() # 0
file_obj.seek(5 , 0)
print file_obj.tell() # 5
file_obj.seek(-2 , 1) 
print file_obj.tell() # 3
file_obj.seek(0 , 2)
print file_obj.tell() # len of the file
file_obj.close()
