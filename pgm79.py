# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:07:22 2023
Count the no.of leap year between two limits
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
d=0
while a<=b:
    c=a%4
    if c==0:
        d=d+1
    else:
        pass
    a=a+1
print(d)
    

