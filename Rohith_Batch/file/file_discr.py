# this is used for to understand open method

open() # to create the file / open the file
# open is a function which is used for to  create file object by file class
#which is having 3 argumets
'''
1. file name with path ---->  file name ---> which current 

2. mode of the operation ----> which mode we are open the file

------------

1. write ---> w
----------------
w :-
-----
    file is not existed  then create the file
    file is existed  with some data then  data will lost then open
    we can't able read it
w+ :-
-----
    file is not existed  then create the file
    file is existed  with some data then  data will lost then open
    we can able read it 


2. read ----> r ---> default mode

r :-
-----
    file is not existed  then its error [ IOError]
    file is existed  with some data then  data will safe  open
    we can't able write it

r+:-
-----
    file is not existed  then its error [ IOError]
    file is existed  with some data then  data will safe  open
    we can able write it


3. append ---> a

----------------------

    file is not existed  then create the file
    file is existed  with some data then  data will safe and then open
    we can't able read it
    we can't able to modify previous data 


















3. encoding ----> ascii based on os ----> python interpreter
'''
