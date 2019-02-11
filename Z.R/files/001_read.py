file_obj = open("readfile.txt","r")
'''
if the file is not existed then its IO Error

file is existed  file opened successfully and
previous data is safe

file is not able to write when file is open is read mode

'''
d = file_obj.read()
print d

file_obj.close()
