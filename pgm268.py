# -*- coding: utf-8 -*-
"""
Created on Sat Jan 13 18:42:54 2024
Read and display a biodata using tuple
@author: santh
"""
a = [[ input("Enter the Name: "),int(input("Enter the age :")),input("Enter the gender : ")] for i in range(5)]
x = tuple(a)
print(x)
