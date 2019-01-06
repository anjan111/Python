# for more understanding string data type

var_s = " programming  langaubge "

a ="python"

print a+var_s  # concatnation of two strings
print (a + ' ') *3 # python python python

print max(a)  # 'y'
print min(a)  # 'h'
print ord('A') # 65
print chr(97) # 97


# indexing for string data type

# positive / forword indexing 
print a[0]  # 'p'
print a[1]  # 'y'
print a[2]  # 't'

# negative  / reverse indexing

print a[-1]  # 'n'
print a[-2]  # 'o'
print a[-3]  # 'h'

# string slicing
'''
we can access sub string from main string

vaar_name[ start_index : stop_index ]
default start ---> 0
defalut stop -----> len(str)
'''
print var_s  # "programming language "
print var_s[3 : 7] # 'gram'
print var_s[:] # "programming language "


# string dicing
'''
we can access periodic character from main string

vaar_name[ start_index : stop_index  : step_index]
default start ---> 0
defalut stop -----> len(str)
default step -----> 1
'''
print var_s  # "programming language "
print var_s[3 :10 :2] # 'gamn'
print var_s[::] # "programming language "




