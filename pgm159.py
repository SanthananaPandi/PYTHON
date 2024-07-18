# -*- coding: utf-8 -*-
"""
Created on Sun Nov 26 19:08:23 2023
Print the number between two limits and find its even or odd number
@author: santh
"""
a=int(input("Enter the value of a: "))
b=int(input("Enter the value of b: "))
for i in range(a,b):
    d=i%2
    if d==0:
        print(i,"is a even number")
    else:
        print(i,"is a odd number")
