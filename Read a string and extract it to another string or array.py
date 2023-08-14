# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:04:55 2023
Read a string and extract it to another string or array
@author: santh
"""
s=input("Enter the value of s: " )
n=len(s)
z=''
i=0
while i<=n-1:
    z=z+s[i]
    i=i+1
print(z)

