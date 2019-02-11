file_obj = open("readfile.txt","w")
'''
file opened as write mode
if the file is not existed 1st create then open it"


file is existed then removes previous data
and open as fresh file

if the is open as write mode
we cant use read  methodes
'''


data =input("enter some data")
file_obj.write(data)
d =file_obj.read()
file_obj.close()
