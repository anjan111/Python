fi = open('sample1.txt','w+')

data =input("enter the data")
fi.write(data)
fi.seek(0,0)
print fi.read()
fi.close()
