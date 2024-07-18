# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 23:00:35 2023
Read a string and extract it to another string by upper case to lower case
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
    else:
        y=y+i
print(y)