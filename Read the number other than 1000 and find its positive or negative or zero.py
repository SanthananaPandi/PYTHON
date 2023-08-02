# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:25:23 2023
Read the number other than 1000 and find its positive or negative or zero.
@author: santh
"""
a=int(input("Enter the value of a: "))
while a!=1000:
    if a>0:
        print("Positive")
    elif a<0:
        print("Negative")
    else:
        print("Zero")
    print(a)
    a=int(input("Enter the value of a:: "))    
