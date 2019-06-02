fo = open("sample.txt",'r')
print("file open in read mode")
print("position : ",fo.tell())
print(fo.read(10))
print("position : ",fo.tell())
fo.seek(4,1)  # 14
print("position : ",fo.tell())
print(fo.read(10))
print("position : ",fo.tell())
fo.seek(0,2) # 
print("position : ",fo.tell())
fo.close()
