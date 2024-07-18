# -*- coding: utf-8 -*-
"""
Created on Mon Dec 11 22:32:28 2023
Read a string and count the number of upper,lower,digits and special character.
@author: santh
"""
a=input("Enter the value of a: ")
b=0
c=0
d=0
e=0
for i in a:
    if i>='A' and i<='Z' :
        b=b+1
    elif i>='a' and i<='z' :
        c=c+1
    elif i>='0' and i<='9':
        d=d+1
    else:
        e=e+1
print(b)
print(c)
print(d)
print(e)
