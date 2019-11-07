# keyword
'''
===>>> predefined words  ( built-in word)
===>>> each and every keyword which can be used / dedicated to do specific task

>>> import keyword
>>> keyword.kwlist

['and', 'as', 'assert', 'break', 'class', 'continue',
'def', 'del', 'elif', 'else', 'except', 'exec', 'finally',
'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
'not', 'or', 'pass', 'print', 'raise', 'return', 'try', 'while',
'with', 'yield']


>>> len(keyword.kwlist)
31
>>> print "hello"
hello
>>> 

'''
# identifier
'''
===>> user defined word --->>programmer word
===>> To give the names for variable , functions , classes 
'''
# Rules
'''
===>> we can use alphabets a-z / A-Z
===>> we can use digits  0 - 9
===>> we can use underscore _
===>> don't start with digit
===>> don't use keywords
==>>  don't use special characters  , . +-)(&^$%#!@#~`
'''

# variable :
'''
===>>> variables are the identifiers
===>>> variables are used for to store data

identifier  =  data( any thing )


>>> var = 123
>>> var
123
>>> print var
123
>>> var_12 = 12
>>> print var_12
12
>>> 2var =123
SyntaxError: invalid syntax
>>> v@r =123
SyntaxError: invalid syntax
>>> class =123
SyntaxError: invalid syntax

'''



# datatypes
'''
==>> what type of data will holded by variable
==>> 2 types
'''
# 1. fundamental datatype
'''
===>>> A single variable can hold single data
1. int ---->>+ve/ -ve /0 --->>> all decimal numbers 
2. float--->> 12.34543
3. complex-->>  real + imgj --->>> 3 + 4j
4. bool  ---->>> True  /  False
5. Nonetype --->> None

examples :=--
=============

>>> var = 123
>>> type(var)
<type 'int'>
>>> var = 12.34334232
>>> type(var)
<type 'float'>
>>> var = 23 + 34j
>>> type(var)
<type 'complex'>
>>> var = True
>>> type(var)
<type 'bool'>
>>> var = False
>>> type(var)
<type 'bool'>
>>> var = None
>>> type(var)
<type 'NoneType'>
>>> 

'''
# sequnecial datatype
'''
====>>> A single variable can hold multiple data elements
====>>> 5types

1. str --->> collection of characters  " "

2. list--->> collection of fundamental & sequencial datatype elment  [ ]

3. tuple--->> collection of fundamental & sequencial datatype elment  ()

4. set--->> collection of fundamental& sequencial datatype elment  {}

5. dict--->>collection of fundamental& sequencial datatype item  {}


>>> var = "soc softech"
>>> type(var)
<type 'str'>
>>> var = ["soc" , 12,8.45,[1,2,2]]
>>> type(var)
<type 'list'>
>>> var =(12,34,12)
>>> type(var)
<type 'tuple'>
>>> var = {12,34,3}
>>> type(var)
<type 'set'>
>>> var = { 12 : "soc" , 78 :"s" }
>>> type(var)
<type 'dict'>
>>> 

'''



























