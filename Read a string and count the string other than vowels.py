# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 19:05:55 2023
Read a string and count the string other than vowels
@author: santh
"""
a=input('Enter the value of a: ')
n=len(a)
i=0
b=0
while i<=n-1:
    if a[i]!='a' and a[i]!='e' and a[i]!='i' and a[i]!='o' and a[i]!='u' :
        b=b+1
    else:
        pass
    i=i+1
print(b)

