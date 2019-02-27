Python 2.7.15 (v2.7.15:ca079a3ea3, Apr 30 2018, 16:30:26) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> var = 123
>>> type(var)
<type 'int'>
>>> id(var)
39609472L
>>> var = -123
>>> type(var)
<type 'int'>
>>> var = 234.536575675343
>>> type(var)
<type 'float'>
>>> var =True
>>> type(var)
<type 'bool'>
>>> v = False
>>> type(v)
<type 'bool'>
>>> v = None
>>> type(v)
<type 'NoneType'>
>>> var = 45 +3j
>>> type(var)
<type 'complex'>
>>> v ='python'
>>> type(v)
<type 'str'>
>>> v ="Python"
>>> type(v)
<type 'str'>
>>> v ='''python'''
>>> type(v)
<type 'str'>
>>> v ="""python"""
>>> type(v)
<type 'str'>
>>> # what is difference between '' /"" /''' ''' /""" """  string representation
>>> v =[]
>>> type(v)
<type 'list'>
>>> v=''
>>> type(v)
<type 'str'>
>>> v = [12 ,34.56 , 67+6j]
>>> type(v)
<type 'list'>
>>> v =()
>>> type(v)
<type 'tuple'>
>>> v = (1)
>>> type(v)
<type 'int'>
>>> v=(1,)
>>> type(v)
<type 'tuple'>
>>> v =[1]
>>> type(v)
<type 'list'>
>>> v ={}
>>> type(v)
<type 'dict'>
>>> v ={,}
SyntaxError: invalid syntax
>>> v=set()
>>> v
set([])
>>> v={12,45,67}
>>> type(v)
<type 'set'>
>>> v= {45 : "soc" , 56 :"python"}
>>> v.keys()
[56, 45]
>>> v.values()
['python', 'soc']
>>> v={"soc" :"s"}
>>> v ={[1,2,3]:"cf"}

Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    v ={[1,2,3]:"cf"}
TypeError: unhashable type: 'list'
>>> a =[12,3,4]
>>> 
