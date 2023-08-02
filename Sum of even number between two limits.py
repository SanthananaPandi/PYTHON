# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:03:31 2023
Sum of even number between two limits
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
d=0
while a<=b:
    c=a%2
    if c==0:
        d=d+a
    else:
        pass
    a=a+1
print(d)
    
