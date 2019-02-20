file_obj = open("sample.txt","r")
cur_loc = file_obj.tell()
print cur_loc  #0
'''
for i in range(2):   
 data = file_obj.readline()
 print data
'''

#file_obj.seek(forward/back, 0/1/2)
#data = file_obj.read(4)
#data = file_obj.readlines()
#l =input("enter what line you need it ")
file_obj.seek(10, 0)  # 0 -------> bigging of the file
#print data
cur_loc = file_obj.tell()
print cur_loc       # 10

file_obj.seek(-5, 1)  # 1 ----> from the current loc of cursor
#print data
cur_loc = file_obj.tell()
print cur_loc        # 5
file_obj.seek(0, 2)   # 2 ----> from the end of the file 
#print data
cur_loc = file_obj.tell()
print cur_loc        # 56

file_obj.seek(-20, 2)
#print data
cur_loc = file_obj.tell()
print cur_loc     #   36


file_obj.close()
