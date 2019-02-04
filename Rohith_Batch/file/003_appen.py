# open a file in append mode


with open("sample.txt") as fo:
    print fo.read(1)
    print fo.readline()
    fo.seek(0,0)
    print fo.readlines()
