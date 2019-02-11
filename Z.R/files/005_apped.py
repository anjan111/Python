file_obj = open("readfile11.txt","r")
'''
if the file is not existed  then its create new file 

file is existed  file opened successfully and
previous data is safe

file is not read  when file is open is append mode

'''
#file_obj.seek(10,0)
#d = file_obj.read(5)
#print d
print file_obj.readline()
file_obj.seek(0,0)
print file_obj.readlines()
#file_obj.write(" I am anjan Kumar ")
file_obj.close()
