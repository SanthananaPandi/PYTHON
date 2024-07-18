# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:02:24 2024
Biggest of three integer using function
@author: santh
"""

def big(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    return x
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
x=big(a,b,c)
print(x)