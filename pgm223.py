# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 15:51:37 2023
Copy n characters from the right edge
@author: santh
"""
s=input("Enter the value of s: ")
n=int(input("Enter the value of n: "))
s1=s[-1:-n:-1]
print(s1)