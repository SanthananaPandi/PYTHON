# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 23:08:19 2024
Biggest and smallest of three integer number using function
@author: santh
"""

def big_low(a,b,c):
    x=(a if a>c else c)if a>b else(b if b>c else c)
    y=(a if a<c else c)if a<b else(b if b<c else c)
    return x,y
#main
a=int(input("Enter the value of a : "))
b=int(input("Enter the value of b : "))
c=int(input("Enter the value of c : "))
m=big_low(a,b,c)
print(m)