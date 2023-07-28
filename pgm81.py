# -*- coding: utf-8 -*-
"""
Created on Mon Jul 24 22:12:36 2023
Read and display the number other than 1000 and find its sum
@author: santh
"""
a=int(input("Enter the value of a: "))
b=0
while a!=1000:
    b=b+a
    a=int(input("Enter the value of a:: "))
print(b)