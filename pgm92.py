# -*- coding: utf-8 -*-
"""
Created on Wed Jul 26 19:09:44 2023
Smallest of ten numbers
@author: santh
"""
a=1
b=999
while a<=10:
    x=int(input("Enter the value of x: "))
    if x<b:
        b=x
    else:
        pass
    a=a+1
print(b)
    
