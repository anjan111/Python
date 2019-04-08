# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 20:27:23 2019

@author: dell
"""

def fibo(n=10):
    past = 0
    pra = 1
    print(past,end =" , ")
    for i in range(1, n):
        print(pra,end = " , ")
        next =past+pra
        past = pra
        pra =next
def main():
    n = input("enter n od fibo terms ")
    n = int(n)
    fibo(n)
if(__name__ =="__main__"):
    main()