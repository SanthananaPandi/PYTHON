# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 11:48:05 2024
Biggest of three numbers using closure function
@author: santh
"""

def big():
    def inner(a,b,c):
        x=(a if a>c else c)if a>b else(b if b>c else c)
        print(x)
    return inner
#main
m=big()
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
m(a,b,c)

