Python 2.7.16 (v2.7.16:413a49145e, Mar  4 2019, 01:37:19) [MSC v.1500 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
=============================== RESTART: Shell ===============================
>>> 
KeyboardInterrupt
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :16.07
data with in var :  16.07
<type 'float'>
memory loc :  57717392
data with variable:
<type 'int'>
memory loc :  43409136
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :true

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 1, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined
>>> True
True
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :True
data with in var :  True
<type 'bool'>
memory loc :  1728884456
data with variable:
<type 'int'>
memory loc :  44064856
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :5+16L
data with in var :  21
<type 'long'>
memory loc :  40627440
data with variable:
<type 'int'>
memory loc :  40722040
>>> (5+6L)
11L
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :(5+16L)
data with in var :  21
<type 'long'>
memory loc :  15723472
data with variable:
<type 'int'>
memory loc :  15818360
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :7+16l
data with in var :  23
<type 'long'>
memory loc :  40299696
data with variable:
<type 'int'>
memory loc :  40394312
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : 5+6j
data with in var :  (5+6j)
<type 'complex'>
memory loc :  8973264

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
TypeError: can't convert complex to int
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type :7+16j
data with in var :  (7+16j)
<type 'complex'>
memory loc :  40496080

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
TypeError: can't convert complex to int
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : 'python'
data with in var :  python
<type 'str'>
memory loc :  43222880

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
ValueError: invalid literal for int() with base 10: 'python'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : 'Apoorva'
data with in var :  Apoorva
<type 'str'>
memory loc :  55692064

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
ValueError: invalid literal for int() with base 10: 'Apoorva'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : none

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 1, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'none' is not defined
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : list 1,2,3

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 1, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1
    list 1,2,3
         ^
SyntaxError: invalid syntax
>>> [1,2,3]
[1, 2, 3]
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : list [1,2,3]

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 1, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
TypeError: 'type' object has no attribute '__getitem__'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : [1,2,3]
data with in var :  [1, 2, 3]
<type 'list'>
memory loc :  60403144

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
TypeError: int() argument must be a string or a number, not 'list'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : (1,2,3)
data with in var :  (1, 2, 3)
<type 'tuple'>
memory loc :  64408384

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
TypeError: int() argument must be a string or a number, not 'tuple'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : {1,2,3}
data with in var :  set([1, 2, 3])
<type 'set'>
memory loc :  43613096

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 6, in <module>
    var = int (var)
TypeError: int() argument must be a string or a number, not 'set'
>>> 
============ RESTART: C:/Python27/Apoorva/int_function_assign1.py ============
enter any data type : {16: "Apoorva", n:"py"}

Traceback (most recent call last):
  File "C:/Python27/Apoorva/int_function_assign1.py", line 1, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'n' is not defined
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :16
data with in var :  16
<type 'int'>
memory loc :  46293296
data with variable:
<type 'float'>
memory loc :  61369664
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 16
data with in var :  16
<type 'int'>
memory loc :  47275760
data with variable:
<type 'float'>
memory loc :  47336112
>>> 78
78
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :78
data with in var :  78
<type 'int'>
memory loc :  40134832
data with variable:
<type 'float'>
memory loc :  40192736
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 16
data with in var :  16
<type 'int'>
memory loc :  55402224
data with variable:
<type 'float'>
memory loc :  70756056
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 23+3a

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1
    23+3a
        ^
SyntaxError: unexpected EOF while parsing
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 5+6j
data with in var :  (5+6j)
<type 'complex'>
memory loc :  48819152

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 8, in <module>
    var = float(var)
TypeError: can't convert complex to float
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 23+5a

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1
    23+5a
        ^
SyntaxError: unexpected EOF while parsing
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : True
data with in var :  True
<type 'bool'>
memory loc :  1728884456
data with variable:
<type 'float'>
memory loc :  44583648
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : true

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'true' is not defined
>>> True
True
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : True
data with in var :  True
<type 'bool'>
memory loc :  1728884456
data with var : 1.0
<type 'float'>
memory loc :  51137248
>>> programme changed to get output line 5
SyntaxError: invalid syntax
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : none

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'none' is not defined
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : [1,2,3]
data with in var :  [1, 2, 3]
<type 'list'>
memory loc :  60889032

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 8, in <module>
    var = float(var)
TypeError: float() argument must be a string or a number
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :(1,2,3)
data with in var :  (1, 2, 3)
<type 'tuple'>
memory loc :  60672832

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 8, in <module>
    var = float(var)
TypeError: float() argument must be a string or a number
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : {1,2,3}
data with in var :  set([1, 2, 3])
<type 'set'>
memory loc :  53967784

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 8, in <module>
    var = float(var)
TypeError: float() argument must be a string or a number
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : {23 : "apoorva", N : '"py"}

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1
    {23 : "apoorva", N : '"py"}
                              ^
SyntaxError: EOL while scanning string literal
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :{23 : "apoorva", n :"py"}

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
NameError: name 'n' is not defined
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type : 'apoorva'/'Leo'/'Grampi'/'grammi'/'uncle avi'

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 
==== RESTART: C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py ====
enter any data type :'apoorva'/"Leo"/'''Grampi'''/''''grammi''''/'''''uncle avi'''''

Traceback (most recent call last):
  File "C:/Python27/Apoorva/DataTypeandfunctions/Float_function.py", line 3, in <module>
    var = input("enter any data type :" )
  File "<string>", line 1, in <module>
TypeError: unsupported operand type(s) for /: 'str' and 'str'
>>> 
