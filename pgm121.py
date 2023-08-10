# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:14:00 2023
Extract it to another string and change upper case to lower case
@author: santh
"""
a=input("Enter the value of a: " )
n=len(a)
b=''
i=0
while i<=n-1:
    c=ord(a[i])
    if c>=65 and c<=90:
        d=c+32
        e=chr(d)
        b=b+e
    else:
        b=b+a[i]
    i=i+1
print(b)
