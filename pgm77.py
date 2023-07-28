# -*- coding: utf-8 -*-
"""
Created on Fri Jul 21 22:49:31 2023
Count the Number of even number between two limits
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
d=0
while a<=b:
    c=a%2
    if c==0:
        d=d+1
    else:
        pass
    a=a+1
print(d)
1