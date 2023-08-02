# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:30:00 2023
Read the number other than 1000 and find its count of positive,negative and zero.
@author: santh
"""
a=int(input("Enter the value of a: "))
b=c=d=0
while a!=1000:
    if a>0:
       b=b+1
    elif a<0:
        c=c+1
    else:
        d=d+1
    a=int(input("Enter the value of a:: "))    
print(b)
print(c)
print(d)
