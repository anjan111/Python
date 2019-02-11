file_obj = open("readfile1.txt","r+")
'''
if the file is not existed then its IO Error

file is existed  file opened successfully and
previous data is safe

file is able to write when file is open is read mode

'''
d = file_obj.read()
print d
file_obj.write(" I am Python and AI Developer")
file_obj.close()
