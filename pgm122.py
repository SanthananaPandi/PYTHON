# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 23:20:24 2023
Flip the alphabets
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
    elif c>=97 and c<=122:
        f=c-32
        g=chr(f)
        b=b+g
    else:
        b=b+a[i]
    i=i+1
print(b)
