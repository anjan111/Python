# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 19:50:32 2019

@author: anjan kumar

This is the program is used for 
to understand  structure of the python program

"""
def add(x,y):
    return x+y
def main():
    a = int(input("enter a : "))
    b = int(input("enter b :" ))
    c = add(a,b)
    print("sum = ",c)
if(__name__ =="__main__"):
    main()
    print("program over")