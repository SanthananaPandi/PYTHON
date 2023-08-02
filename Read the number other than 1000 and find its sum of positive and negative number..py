# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:33:21 2023
Read the number other than 1000 and find its sum of positive and negative number.
@author: santh
"""
a=int(input("Enter the value of a: "))
b=c=0
while a!=1000:
    if a>0:
       b=b+a
    elif a<0:
        c=c+a
    else:
      pass
    a=int(input("Enter the value of a:: "))    
print(b)
print(c)

