# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 18:16:47 2023
print the pattern  *
                  ***
                 *****
                *******
@author: santh
"""
x=3
y=1
a=1
while a<=4:
    b=1
    while b<=x:
        print(" ",end="")
        b=b+1
    c=1
    while c<=y:
        print("*",end="")
        c=c+1
    print()
    a=a+1
    x=x-1
    y=y+2
