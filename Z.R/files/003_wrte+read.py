file_obj = open("read1.txt","w+")
'''
file opened as write mode
if the file is not existed 1st create then open it"


file is existed then removes previous data
and open as fresh file

if the is open as write mode
we can use read  methodes
'''


data =input("enter some data")
file_obj.write(data)
file_obj.seek(0,0) # set the cursor location to start of file
d =file_obj.read()
print d
file_obj.close()
