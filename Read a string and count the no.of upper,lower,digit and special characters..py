# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:09:54 2023
Read a string and count the no.of upper,lower,digit and special characters.
@author: santh
"""
a=input('Enter the value of a: ')
n=len(a)
i=0
b=0
c=0
d=0
e=0
while i<=n-1:
    if a[i]>='A' and a[i]<='Z':
        b=b+1
    if a[i]>='a' and a[i]<='z':
        c=c+1
    if a[i]>='0' and a[i]<='9':
        d=d+1
    else:
        e=e+1
    i=i+1
print(b)
print(c)
print(d)
print(e)
    
Linsoft
