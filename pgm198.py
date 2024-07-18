# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:03:40 2023
Flip the characters(Alphabets)
@author: santh
"""
x=input("Enter the value of x: ")
y=''
for i in x:
    z=ord(i)
    if z>=65 and z<=90:
        d=z+32
        e=chr(d)
        y=y+e
    elif z>=97 and z<=122:
        f=z-32
        g=chr(f)
        y=y+g
    else:
        y=y+i
print(y)